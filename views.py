from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ScrumyGoals, GoalStatus, SignUpForm, MoveGoalForm, AddGoalForm, AdminChangeGoalForm, QAChangeGoalForm
from django.contrib.auth.models import User, Group
from random import randint

def index(request):
  if request.method == 'POST':
      form = SignUpForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
          forminfo = request.POST.copy()
          username = forminfo.get('username')
          form.save()
          user = User.objects.get(username=username)
          s = Group.objects.get(name='Developer')
          s.user_set.add(user)
          return HttpResponseRedirect('success/')
  else:
      form = SignUpForm()
  return render(request, 'samsonadejoroscrumy/signup.html', {'form': form})


'''
def add_goal(request):
    if request.user.is_authenticated:
        name_goal = request.POST.get('name', None)
        group_name = request.user.groups.all()ed[0].name
        status_start = 0
        if group_name == 'Admin':
            status_start = 1
        elif group_name == 'Quality_Analyst':
            status_start = 2
        goal = ScrumyGoals(user=request.user.username, name=name_goal, status=status_start)
        goal.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/samsonadejoroscrumy/goalsuccess/')
    else:
        return HttpResponseRedirect('')
        # 'goal_id': goalname.goal_id
'''

'''
def add_goal(request):
    current_user = request.user
    if current_user.is_authenticated:
            if request.method == 'POST':
                form = CreateGoalForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    goal_id = randint(1000, 9999)
                    status_name = GoalStatus(id=1)
                    post.created_by = current_user.first_name
                    post.moved_by = current_user.first_name
                    post.owner = current_user.first_name
                    post.goal_id = goal_id
                    post.goal_status = status_name
                    post.user = current_user
                    post.save()
            else:
                form = CreateGoalForm()
            return render(request, 'samsonadejoroscrumy/home.html', {'form': form})'''


def add_goal(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddGoalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            goal_id = randint(1000, 9999)
            status_name = GoalStatus(id=1)
            post.created_by = current_user.first_name
            post.moved_by = current_user.first_name
            post.owner = current_user.first_name
            post.goal_id = goal_id
            post.user = current_user
            post.goal_status = status_name
            post.save()
            return HttpResponseRedirect('/samsonadejoroscrumy/goalsuccess/')
    else:
        form = AddGoalForm()
    return render(request, 'samsonadejoroscrumy/addgoal.html', {'form': form})



def success_page(request):
    success = 'Your account has been successfully created'
    context = {'success': success}
    return render(request, 'samsonadejoroscrumy/success.html', context)

def success_goal(request):
    success2 = 'Your goal has been successfully added'
    context = {'success2': success2}
    return render(request, 'samsonadejoroscrumy/goalsuccess.html', context)


def scrumy_goals(request):
    response = ScrumyGoals.objects.all()
    return HttpResponse(response)


def specific_goal(request):
    q = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(q)


def move_goal(request, goal_id):
        current_user = request.user
        usr_grp = request.user.groups.all()[0]
        goals = get_object_or_404(ScrumyGoals, pk=goal_id)
        if usr_grp == Group.objects.get(name='Developer') and current_user == goals.user:
            if request.method == 'POST':
                form = MoveGoalForm(request.POST)
                if form.is_valid():
                    selected_status = form.save(commit=False)
                    selected = form.cleaned_data['goal_status']
                    get_status = selected_status.goal_status
                    choice = GoalStatus.objects.get(id=int(selected))
                    goals.goal_status = choice
                    goals.save()
                    return HttpResponseRedirect('/samsonadejoroscrumy/movegoalsuccess')
            else:
                form = MoveGoalForm()

        elif usr_grp == Group.objects.get(name='Admin') or usr_grp == Group.objects.get(name='Owner'):
            if request.method == 'POST':
                form = AdminChangeGoalForm(request.POST)
                if form.is_valid():
                    selected_status = form.save(commit=False)
                    get_status = selected_status.goal_status
                    goals.goal_status = get_status
                    goals.save()
                    return HttpResponseRedirect('/samsonadejoroscrumy/movegoalsuccess')
            else:
                form = AdminChangeGoalForm()

        elif usr_grp == Group.objects.get(name='Quality Assurance'):
            if request.method == 'POST':
                form = QAChangeGoalForm(request.POST)
                if form.is_valid():
                    selected_status = form.save(commit=False)
                    selected = form.cleaned_data['goal_status']
                    # get_status = selected_status.goal_status
                    choice = GoalStatus.objects.get(id=int(selected))
                    goals.goal_status = choice
                    goals.save()
                    return HttpResponseRedirect('/samsonadejoroscrumy/movegoalsuccess')
                form = QAChangeGoalForm()
        else:
            return HttpResponseRedirect('/samsonadejoroscrumy/error')
        return render(request, 'samsonadejoroscrumy/movegoal.html',
                      {'form': form, 'goals': goals, 'current_user': current_user})



def home(request):
    goalname = ScrumyGoals.objects.get(goal_name='Django Template')
    user = User.objects.all()
    goalid = ScrumyGoals.objects.get(goal_id=3919)
    goal_status1 = GoalStatus.objects.get(status_name='Weekly Goal')
    weekly_goal = goal_status1.scrumygoals_set.all()
    goal_status2 = GoalStatus.objects.get(status_name='Daily Target')
    daily_goal = goal_status2.scrumygoals_set.all()
    goal_status3 = GoalStatus.objects.get(status_name='Verify Goal')
    verify_goal = goal_status3.scrumygoals_set.all()
    goal_status4 = GoalStatus.objects.get(status_name='Done Goal')
    done_goal = goal_status4.scrumygoals_set.all()
    current_user = request.user
    current_group = request.user.groups.all()
    goalie = ScrumyGoals.objects.get(id=3)

    context = {'user': user, 'weekly_goal': weekly_goal, 'daily_goal': daily_goal, 'verify_goal': verify_goal,
               'done_goal': done_goal, 'current_user': current_user,
               'current_group': current_group, 'goalie': goalie, 'goal_id': goalname.goal_id }
    return render(request, 'samsonadejoroscrumy/home.html', context)



def error(request):
    current_user = request.user
    return render(request, 'samsonadejoroscrumy/error.html', {'current_user': current_user})

def move_goal_success(request):
    current_user = request.user
    return render(request, 'samsonadejoroscrumy/movegoalsuccess.html', {'current_user': current_user})
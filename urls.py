from django.urls import path, include
from . import views

app_name = 'samsonadejoroscrumy'
urlpatterns = [
    path('',views.index, name='index'),
    path('scrumygoals/', views.scrumy_goals, name='scrumy_goals'),
    path('movegoal/<int:goal_id>/', views.move_goal, name='movegoal'),
    path('specificgoal', views.specific_goal, name='specific_goal'),
    path('home/', views.home, name='home'),
    path('addgoal/', views.add_goal, name='add_goal'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('success/', views.success_page, name='success'),
    path('goalsuccess/', views.success_goal, name='goalsuccess'),
    path('error/', views.error, name='error'),
    path('movegoalsuccess/', views.move_goal_success, name='movegoalsuccess')
]


'''
def add_goal(request):
    current_user = request.user
    form = AddGoalForm()
    if current_user.is_authenticated:
        if request.method == 'GET':
            context = {'form': form}
            return render(request, 'samsonadejoroscrumy/addgoal.html', context)
        elif request.method == 'POST':
            form = AddGoalForm(request.POST)
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
                return HttpResponseRedirect('success/')
            return render(request, 'samsonadejoroscrumy/addgoal.html', {'form': form})
'''

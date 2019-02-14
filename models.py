from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm
from django import forms


class GoalStatus(models.Model):
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='samsonadejoroscrumy')
    goal_name = models.CharField(max_length=200)
    goal_id = models.IntegerField(default=0)
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.created_by


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class MoveGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset[:5]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']


class AdminChangeGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_status']


class QAChangeGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('-id')[:2][::-1]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']


class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']


class AddGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name']
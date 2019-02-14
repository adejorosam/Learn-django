from django.contrib import admin
from .models import GoalStatus
from .models import ScrumyGoals
from .models import ScrumyHistory

admin.site.register(GoalStatus)
admin.site.register(ScrumyHistory)
admin.site.register(ScrumyGoals)



from django.contrib import admin
from .models import govtProjects,ongoingProgrammes,comingEvents

admin.site.register(govtProjects)
admin.site.register(ongoingProgrammes)
admin.site.register(comingEvents)
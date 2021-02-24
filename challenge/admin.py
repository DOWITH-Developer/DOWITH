from django.contrib import admin
from .models import Challenge, Enrollment, EnrollmentDate
from .forms import ChallengeForm

# Register your models here.
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    form = ChallengeForm
    list_display = ['title', 'private', 'status']
    list_display_links = ['title', 'private', 'status']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['challenge', 'player']
    list_display_links = ['challenge', 'player']

@admin.register(EnrollmentDate)
class EnrollmentDateAdmin(admin.ModelAdmin):
    list_display = ['enrollment', 'date']
    list_display_links = ['enrollment', 'date']



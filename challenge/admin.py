from django.contrib import admin
from .models import Challenge, Enrollment, EnrollmentDate

# Register your models here.
@admin.register(Challenge)
class FriendshipAdmin(admin.ModelAdmin):
    pass

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    pass

@admin.register(EnrollmentDate)
class EnrollmentDateAdmin(admin.ModelAdmin):
    pass
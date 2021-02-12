from django.contrib import admin
from .models import Challenge, Enrollment, EnrollmentDate

# Register your models here.
@admin.register(Challenge)
class FriendshipAdmin(admin.ModelAdmin):
    pass

@admin.register(Enrollment)
class FriendshipAdmin(admin.ModelAdmin):
    pass

@admin.register(EnrollmentDate)
class FriendshipAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

from accounts.models import UserProfileModel
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
  list_display = ['user', 'career', 'bio', 'location', 'clients']

admin.site.register(UserProfileModel, UserProfileAdmin)

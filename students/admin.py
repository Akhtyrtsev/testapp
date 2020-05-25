from django.contrib import admin
from students.models import User, Course


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('users', )
# Register your models here.


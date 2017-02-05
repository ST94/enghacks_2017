from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "uw_id", "category", "course_number")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class OptionAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Option, OptionAdmin)

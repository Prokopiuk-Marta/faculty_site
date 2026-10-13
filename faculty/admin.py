from django.contrib import admin

from .models import Department, ExchangeProgram, MainPage, Program, Teacher


class ProgramAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "department", "coordinator_name"]
    list_filter = ["department"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "degree", "department"]
    list_filter = ["department"]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "head"]


class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ["university", "country", "languages", "places_count", "deadline"]
    list_filter = ["country"]


admin.site.register(MainPage)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ExchangeProgram, ExchangeProgramAdmin)

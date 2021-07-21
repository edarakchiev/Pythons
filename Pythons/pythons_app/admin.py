from django.contrib import admin

from Pythons.pythons_app.models import Python


@admin.register(Python)
class PythonAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
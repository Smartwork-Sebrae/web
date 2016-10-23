from django.contrib import admin

from desk.models import Desk


class DeskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Desk, DeskAdmin)

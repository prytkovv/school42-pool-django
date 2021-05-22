from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Tip, Vote


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 3


class TipAdmin(admin.ModelAdmin):
    inlines = [VoteInline]


class UserAdminCustom(UserAdmin):
    pass

admin.site.register(Tip, TipAdmin)

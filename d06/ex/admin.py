from django.contrib import admin

from .models import Tip, Vote


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 3


class TipAdmin(admin.ModelAdmin):
    inlines = [VoteInline]


admin.site.register(Tip, TipAdmin)

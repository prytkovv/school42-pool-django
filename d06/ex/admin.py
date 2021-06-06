from django.contrib import admin

from .models import Tip, Vote


class VoteInline(admin.TabularInline):
    model = Vote


class TipAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'publication_date')
    inlines = [VoteInline]


admin.site.register(Tip, TipAdmin)

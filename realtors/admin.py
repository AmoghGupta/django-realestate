from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp')
    list_display_links = ('id', 'name')
    list_filter = ('email',)
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 25


# Register your models here.
admin.site.register(Realtor, RealtorAdmin)

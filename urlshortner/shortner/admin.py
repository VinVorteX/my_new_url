from django.contrib import admin
from .models import Url

# Register your models here.

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['link', 'clicks']
    search_fields = ['link', 'uuid']
    list_filter = ['clicks']
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ['link']
    list_select_related = ['link']
    list_display_links_details = ['link']
    list_display_links_editable = ['link']
    list_display_links_select_related = ['link']
    list_display_links_details_editable = ['link']
    list_display_links_details_select_related = ['link']
    list_display_links

from django.contrib import admin

from pages import models


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    pass


class ContentAdmin(admin.ModelAdmin):
    search_fields = ['title']
    def get_search_results(self, request, queryset, search_term):
        pass


admin.site.register(models.Page)
admin.site.register(models.Content, ContentAdmin)
admin.site.register(models.Audio)
admin.site.register(models.Video)
admin.site.register(models.Text)



from django.contrib import admin
from rango.models import Category, Page, PageAdmin

# Register your models here.

# Add in this class to customise the Admin interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

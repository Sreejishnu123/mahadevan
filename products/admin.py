from django.contrib import admin
from .models import Item  # Change this line to match your model name

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

admin.site.register(Item, ItemsAdmin)  # Change this line to match your model name
# Register your models here.

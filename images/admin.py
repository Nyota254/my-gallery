from django.contrib import admin
from .models import Tag,Image,Category,Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image,ImageAdmin)

# Register your models here.

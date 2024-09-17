from django.contrib import admin
from .models import Slider,Product


class SliderAdmin(admin.ModelAdmin):
    list_display= ('caption','enabled','image_order')
    search_fields = ('caption',)

admin.site.register(Slider,SliderAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name','price')
    search_fields = ('name',)

admin.site.register(Product,ProductAdmin)

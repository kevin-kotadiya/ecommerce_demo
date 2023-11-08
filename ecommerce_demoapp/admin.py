from django.contrib import admin
from .models import*
from django.utils.html import format_html
# Register your models here.

class user_data_get(admin.ModelAdmin):
    list_display = ['id','fname','lname','email','password']

admin.site.register(user_data,user_data_get)

class product_get(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html('<img src="{}" height="120" width="100"></img>'.format(obj.image.url))

    list_display = ['id','product_name','image_tag','price']

admin.site.register(product,product_get)

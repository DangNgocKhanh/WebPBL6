from django.contrib import admin
from django.contrib import auth

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from .models import *

class User_Admin(BaseUserAdmin):
    list_display = ('id','email', 'username','Name','Phone','Address',
                    'Birthday','is_active','is_staff','is_superuser')
    search_fields = ('id','email', 'username','Name','Phone','Address',
                    'Birthday','is_active','is_staff','is_superuser',)

    fieldsets = BaseUserAdmin.fieldsets
    fieldsets[0][1]['fields'] = fieldsets[0][1]['fields'] + (
        'Name','Avatar','Phone','Address'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username', 'password1', 'password2','Name','Avatar','Phone','Address')}
        ),
    )
    readonly_fields = ["Show_Avatar"]
    def Show_Avatar(self,Product):
        return mark_safe("<img src='/{img_url}' alt='Image' style='width:120px;'/>".format(img_url=User.Avatar.name))
    
admin.site.register(User,User_Admin)
admin.site.unregister(auth.models.Group)

class Category_Admin(admin.ModelAdmin):
    list_display = ('id','Name','Url','Creation_time','Update_time')
    search_fields = ('id','Name','Url','Creation_time','Update_time',)

admin.site.register(Category,Category_Admin)

class Trademark_Admin(admin.ModelAdmin):
    list_display = ('id','Name','Url','Creation_time','Update_time')
    search_fields = ('id','Name','Url','Creation_time','Update_time',)

    readonly_fields = ["Show_Avatar"]
    def Show_Avatar(self,Trademark):
        return mark_safe("<img src='/{img_url}' alt='Image' style='width:120px;'/>".format(img_url=Trademark.Avatar.name))

admin.site.register(Trademark,Trademark_Admin)

class Made_Admin(admin.ModelAdmin):
    list_display = ('id','Name','Url','Creation_time','Update_time')
    search_fields = ('id','Name','Url','Creation_time','Update_time',)

    readonly_fields = ["Show_Avatar"]
    def Show_Avatar(self,Made):
        return mark_safe("<img src='/{img_url}' alt='Image' style='width:120px;'/>".format(img_url=Made.Avatar.name))

admin.site.register(Made,Made_Admin)

class Product_Admin(admin.ModelAdmin):
    list_display = ('id','Name','Code','Category','Trademark','Made','Price','Percent_discount','Price_has_decreased','Describe','Guarantee','Url','Creation_time','Update_time')
    search_fields = ('id','Name','Code','Category','Trademark','Made','Price','Percent_discount','Price_has_decreased','Describe','Guarantee','Url','Creation_time','Update_time',)

admin.site.register(Product,Product_Admin)

class Stock_Admin(admin.ModelAdmin):
    list_display = ('id','Product','Amount','Creation_time','Update_time')
    search_fields = ('id','Product','Amount','Creation_time','Update_time',)

admin.site.register(Stock,Stock_Admin)

class Goods_received_note_Admin(admin.ModelAdmin):
    list_display = ('id','Stock','Product','Code','input','Total','Creation_time','Update_time')
    search_fields = ('id','Stock','Product','Code','input','Total','Creation_time','Update_time',)

admin.site.register(Goods_received_note,Goods_received_note_Admin)

class Cart_Admin(admin.ModelAdmin):
    list_display = ('id','User','Total_amount','Total_money','Creation_time','Update_time')
    search_fields = ('id','User','Total_amount','Total_money','Creation_time','Update_time',)

admin.site.register(Cart,Cart_Admin)

class Cart_detail_Admin(admin.ModelAdmin):
    list_display = ('id','Cart','Product','Amount','Creation_time','Update_time')
    search_fields = ('id','Cart','Product','Amount','Creation_time','Update_time',)

admin.site.register(Cart_detail,Cart_detail_Admin)


class Oder_Admin(admin.ModelAdmin):
    list_display = ('id','Code','User','Total_amount','Total_money','Url','Creation_time','Update_time')
    search_fields = ('id','Code','User','Total_amount','Total_money','Url','Creation_time','Update_time',)

admin.site.register(Oder,Oder_Admin)

class Oder_detail_Admin(admin.ModelAdmin):
    list_display = ('id','Oder','Product','Amount','Creation_time','Update_time')
    search_fields = ('id','Oder','Product','Amount','Creation_time','Update_time',)

admin.site.register(Oder_detail,Oder_detail_Admin)


from django.contrib import admin
from .models import Pizza, Size

# Register your models here.
admin.site.register(Pizza)


#lets add model access control to the size model, just as an example :)

class ReadOnlyAdminMixin:
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser== True:
            return True
        else:
            return False
        

    def has_change_permission(self, request, obj=None):
        if request.user.has_perm('size.change_size'):

            return True
        else:
            return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser== True:
            return True
        else:
            return False
        
    def has_view_permission(self, request, obj=None):
        return True
      
    

@admin.register(Size)
class SizeAdmin(ReadOnlyAdminMixin,admin.ModelAdmin):

    list_display=("title",)



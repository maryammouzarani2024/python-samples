from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

#add some customized access control to the User model

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    
    def get_form(self, request, obj=None, **kwargs):
        form=super().get_form(request, obj, **kwargs)
        if request.user.is_superuser==False:
            form.base_fields['username'].disabled=True
            return form
            
        else:
            return form
            

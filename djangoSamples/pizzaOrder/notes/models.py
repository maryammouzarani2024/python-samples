from django.db import models
from django.contrib.auth.models import User

#access control
from django.dispatch import receiver
from django.db.models.signals import post_save
from guardian.shortcuts import assign_perm 



class Notes(models.Model):

    title=models.CharField(max_length=200)
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)# the data is automatically set after creating a new note
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
@receiver(post_save, sender=Notes)
def set_notes_permissions(sender, instance, **kwargs):
    user=User.objects.get(username=instance.user.username)
    assign_perm('notes.change_notes', user)
    assign_perm('notes.change_notes', user, instance)
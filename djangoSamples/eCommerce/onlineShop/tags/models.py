from django.db import models
from django.contrib.contenttypes.models  import ContentType
from django.contrib.contenttypes.fields  import GenericForeignKey

# Create your models here.

# class Tag(models.Model):
#     label=models.CharField(max_length=255)
    
# class TaggedItem(models.Model):
#     tag=models.ForeignKey(Tag, on_delete=models.CASCADE)
#     #to make the tag operation general for every object, instead of using product as a foreign key I get the type,id and a genericForeignkey to refer to the tagged item
#     content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     content_id=models.PositiveIntegerField()
#     content_object=GenericForeignKey()
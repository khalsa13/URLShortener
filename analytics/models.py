from django.db import models

# Create your models here.
from shortener.models import deepURL


class ClickEventManager(models.Manager):
    def create_instance(self,instance):
        if isinstance(instance,deepURL):
            obj,created=self.get_or_create(deep_url=instance)
            obj.count+=1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    deep_url=models.OneToOneField(deepURL)
    count=models.IntegerField(default=0)
    objects=ClickEventManager()
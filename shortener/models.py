from django.db import models
import string, random
from django.conf import settings

from .utils import code_generator,create_shortcode
from django_hosts.resolvers import reverse
from .validators import validate_dot_com,validate_Url
# Create your models here.


SHORTCODE_MAX=getattr(settings,"SHORTCODE_MAX",15)

class deepURLManager(models.Manager):
    def refresh_allcode(self):
        qs=deepURL.objects.filter(id__gte=1)
        newcodes=0
        for q in qs:
            q.shortcode=create_shortcode(q)
            print(q.shortcode)
            q.save()
            newcodes+=1
        return "NewCodes Made: {i}".format(i=newcodes)


class deepURL (models.Model):
    Url = models.CharField(max_length=254,validators=[validate_Url,validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects=deepURLManager()

    def __str__(self):
        return str(self.Url)


    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=="":
             self.shortcode =create_shortcode(self)
        super(deepURL, self).save(*args, **kwargs)


    def small_url(self):
        url_path=reverse("scode",kwargs={'shortcode':self.shortcode},host='127',scheme='http')
        return  url_path
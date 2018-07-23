from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

def upload_location (instance, filename):
    return "%$/%$" % (instance.id, filename)


class House (models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="upload_location", null=True, blank=True,
                              width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("houses:detail", kwargs={"id": self.id})
    class Meta:
        ordering = ["-timestamp", "-updated"]


# Create your models here.

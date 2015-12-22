#conding=utf-8

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    real_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, null=True, blank=True)

    def __unicode__(self):
        return self.real_name

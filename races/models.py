from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
from django.db import models

class Counter(models.Model):
    name = models.CharField(max_length=16,null=False)
    count = models.IntegerField(default=0)

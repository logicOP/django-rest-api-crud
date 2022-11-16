from django.db import models


class Components(models.Model):
    name = models.CharField(unique=True, max_length=40)
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField()


class AdvantageAndDisadvantage(models.Model):
    component = models.ForeignKey(Components, on_delete=models.CASCADE)
    text = models.TextField()
    is_advantage = models.BooleanField(default=True)


class BriefDescription(models.Model):
    component = models.ForeignKey(Components, on_delete=models.CASCADE)
    text = models.TextField()


class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

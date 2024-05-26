from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Platform(models.Model):
    name = models.CharField(max_length=255)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    webhook_url = models.URLField()

class Webhook(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    payload = models.JSONField()
    sent_at = models.DateTimeField(auto_now_add=True)

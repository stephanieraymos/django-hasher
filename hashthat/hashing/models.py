from django.db import models

class Hash(models.Model):
    text = models.TextField()
    hash = models.CharField(max_length=64) # hashes are always 64 characters long

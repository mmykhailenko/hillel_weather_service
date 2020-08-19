from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    flag = models.CharField(max_length=512, null=True, blank=True)
    wiki_page = models.CharField(max_length=512, null=True, blank=True)

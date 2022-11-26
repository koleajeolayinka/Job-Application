from django.db import models

# Create your models here.

NEWSLETTER_OPTION = [
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly')
]


class Subscribe(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    option = models.CharField(max_length=10, choices=NEWSLETTER_OPTION, default='weekly')

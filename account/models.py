from django.db import models
from hashlib import sha256

# Create your models here.

# TODO: Add validators later
# TODO: Add date of expiry stuff later

class Account(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    account_number = models.BigIntegerField()
    card_number = models.BigIntegerField()
    csv = models.IntegerField()
    date_of_account_creation = models.DateTimeField(auto_now=True)
    address = models.TextField()

    def __str__(self):
        return self.username

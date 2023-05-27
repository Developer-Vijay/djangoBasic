from django.db import models

# Create your models here.
# make migrations  Create changes and store in a file
#  migrate - apply the pending changes  created by making migrations
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=122)
    date =models.DateField()

    def __str__(self) -> str:
        return self.name;
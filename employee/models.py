from django.db import models

# Employee details model
class Employee(models.Model):
    name = models.CharField(max_length=60)
    designation = models.CharField(max_length=60)
    address = models.TextField()
    nid = models.CharField(max_length=60, default='Not given yet!')
    contact = models.CharField(max_length=15)
    joining_date = models.DateField(blank=True)

    def __str__(self):
        return self.name

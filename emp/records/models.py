from django.db import models

class data(models.Model):
    empname = models.CharField(max_length=200)
    role = models.TextField()
    salary= models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    
    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name
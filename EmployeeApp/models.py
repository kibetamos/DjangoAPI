
from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    id_number = models.CharField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=500)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name="employees"
    )
    date_of_joining = models.DateField()
    photo_file_name = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

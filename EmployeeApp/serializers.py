from rest_framework import serializers
from EmployeeApp.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['EmployeeId','EmployeeName']
        fields = '__all__'


    # EmployeeId = models.AutoField(primary_key=True)
    # EmployeeName = models.CharField(max_length=500)
    # Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    # DateOfJoining = models.DateField()
    # PhotoFileName = models.CharField(max_length=500)

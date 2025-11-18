from rest_framework import viewsets
from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


#viewset allows use have the crud funbctionality

class EmployeeViewSet(viewsets.ModelViewSet):

    #selects all the data from the model
    queryset = Employee.objects.all()

    #controls whats seen on the api endpoint
    serializer_class = EmployeeSerializer

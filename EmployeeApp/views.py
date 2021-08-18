from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSersilizer


# Create your views here.
@csrf_exempt
def departmentAPI(request, id=0):
    if request.method == 'GET':
        department = Department.objects.all()
        department_serializer = DepartmentSerializer(deoartments, many=true)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(requests)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializeris_valid():
            department_serializer.save()
            return JsonResponse("saved successfully")
        return JsonResponse("Failed", safe=False)
    elif request.method =='PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId= department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department,data =department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("update successful", safe=False)
        return JsonResponse("Failed")
    elif request.method == 'DELETE':
        Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted successfully", safe=False)





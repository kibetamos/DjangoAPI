from django.urls import path, include
from rest_framework.routers import DefaultRouter
from EmployeeApp.views import DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'department', DepartmentViewSet)
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

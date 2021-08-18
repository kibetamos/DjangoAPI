from django.config.urls import urls
from django.urls import path, include
from EmployeeApp import views

urlpatterns = [
    url(r'^department$', views.departmentAPI),
    url(r'^department/([0-9]+)$')

]

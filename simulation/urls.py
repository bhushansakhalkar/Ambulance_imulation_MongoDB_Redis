from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("test/",views.redisConnection),
    path("addPatient/",views.AddPatient),
    path("findHospitals/",views.findHospitals),
]

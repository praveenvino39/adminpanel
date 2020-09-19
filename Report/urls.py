from django.urls import path
from .views import shipping_report, petrol_report, envelop_report, case_report, refered_report, production_report

urlpatterns = [
    path('/shipping/', shipping_report),
    path('/petrol/', petrol_report),
    path('/envelope/', envelop_report),
    path('/case/', case_report),
    path('/refered/', refered_report),
    path('/production/', production_report),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^pay/', views.create_payment_req, name="payment"),
    url(r'^list/', views.list_payments, name="list")
]

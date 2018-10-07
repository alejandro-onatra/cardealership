from django.conf.urls import url
import views

urlpatterns = [

    url( r'^cars/$', views.car_list),
    url( r'^cars/(?P<pk>[0-9]+)/$', views.rental_detail),
    url( r'^rentals/$', views.rental_list),
    url( r'^rentals/(?P<pk>[0-9]+)/$', views.rental_detail),
]
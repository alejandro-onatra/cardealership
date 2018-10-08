from django.conf.urls import url
import views

urlpatterns = [

    url( r'^api/cars?/$', views.CarList.as_view()),
    url( r'^api/cars/(?P<pk>[0-9]+)?/$', views.CarDetail.as_view()),
    url( r'^api/rentals?/$', views.RentalList.as_view()),
    url( r'^api/rentals/(?P<pk>[0-9]+)?/$', views.RentalDetail.as_view()),
]
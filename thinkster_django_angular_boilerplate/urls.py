from django.conf.urls import url

from thinkster_django_angular_boilerplate.views import IndexView

urlpatterns = [
    '',
    url('^.*$', IndexView.as_view(), name='index'),
]

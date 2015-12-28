from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^login/$',views.my_login, name="my_login"),
    url('^logout/$',views.my_logout, name="my_logout"),
    url('^register/$',views.my_user_register, name= "my_user_register"),
]
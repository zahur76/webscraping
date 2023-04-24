from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("send_mail", views.send_mail_to, name="send_mail"),
]

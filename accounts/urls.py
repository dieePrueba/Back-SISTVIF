from django.urls import path
from . import views


urlpatterns = [
    path('list_usuarios/', views.listUserAccount),

]
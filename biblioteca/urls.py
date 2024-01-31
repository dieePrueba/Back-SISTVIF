from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registroObra),
    path('list/categoria_obra/', views.listCategoria_obras),
    path('list/tipo_obras/', views.listTipo_obras),
    path('list/tipo_material/', views.listTipo_material),

]
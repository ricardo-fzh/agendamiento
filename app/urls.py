from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('mantenedor-fechas/', mantenedor_fecha, name='mantenedor-fechas'),
]

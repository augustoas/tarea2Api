
from django.urls import path
from .views import hamburguer_list, hamburguer_detail, ingredient_list, ingredient_detail, hamburguer_ingredient

urlpatterns = [
    path('hamburguesa/', hamburguer_list),
    path('hamburguesa', hamburguer_list),
    path('hamburguesa/<pk>/', hamburguer_detail),
    path('hamburguesa/<pk>', hamburguer_detail),
    path('ingrediente/', ingredient_list),
    path('ingrediente', ingredient_list),
    path('ingrediente/<pk>/', ingredient_detail),
    path('ingrediente/<pk>', ingredient_detail),
    path('hamburguesa/<pk_h>/ingrediente/<pk_i>/',hamburguer_ingredient),  
    path('hamburguesa/<pk_h>/ingrediente/<pk_i>',hamburguer_ingredient)
]

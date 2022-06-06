from django.urls import path
from .views import  home, inicio, formulario2, GaleriaDeFotos, quienesSomos, forms_persona, mostrar, form_mod_persona, nose
urlpatterns = [
    path('home',home,name="home"),
    path('ini',inicio,name="ini"),
    path('', nose, name="nose"),
    path('form2', formulario2,name="form2"),
    path('Galeria', GaleriaDeFotos,name="Galeria"),
    path('quienes', quienesSomos,name="quienes"),
    path('mostrar2', mostrar,name="mostrar2"),
    path('forms-persona', forms_persona, name="forms-persona"),
    path('form_mod_persona/<id>', form_mod_persona, name="form_mod_persona"),
    
    
]
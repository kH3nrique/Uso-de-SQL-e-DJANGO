from django.urls import path
from app_Patrocinador import views

urlpatterns = [
    #rota, view, nome referencial 
    path('', views.home, name='home'),

    #cadastro/
    path('cadastro/', views.cadastros, name='listagem_patrocinadores')
]
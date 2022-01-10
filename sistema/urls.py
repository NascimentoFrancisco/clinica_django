from django.urls import path
from . import views #arquivo views que ainda não utilizamos

urlpatterns = [
    path('', views.home, name='home'),
    #Cadastros
    path('cliente/new/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('medico/new/', views.cadastrar_medico, name='cadastrar_medico'), 
    path('especialidade/new/', views.cadastrar_epecialidade, name='cadastrar_epecialidade'),
    path('horarios/new/', views.inserir_horarios, name='inserir_horarios'),
    path('agenda/new/', views.criar_nova_agenda, name='criar_nova_agenda'),
    #Listagem
    path('listar_agendas', views.listar_agendas, name='listar_agendas'),
    path('detalhar_agenda/<int:id>/', views.detalhar_agenda, name='detalhar_agenda'),
    #Login, autenticação e loout do administrador e clientes da clinica
    path('login_adm',views.login_adm, name='login_adm'),
    path('autenticar_administrador', views.autenticar_administrador,name='autenticar_administrador'),
    path('administracao/<int:id>/',views.administracao, name='administracao'),
    path('autenticar_cliente', views.autenticar_cliente, name='autenticar_cliente'),
    path('area_do_cliente/<int:id>/',views.area_do_cliente, name= 'area_do_cliente'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
    #Marcação da consulta
    path('marcar_consulta/<int:id>/<int:pk>/', views.marcar_consulta, name='marcar_consulta'),
]
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from sistema.models import  Especialidade, Medico, Horarios, Agenda, Cliente
from sistema.forms import ClienteForm ,MedicoForm, EspecialidadeForm, HorariosForm, AgendaForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'sistema/home.html')

def listar_agendas(request):
    agendas = Agenda.objects.all()
    return render(request, 'sistema/listar_agendas.html', {'agendas':agendas})

def detalhar_agenda(request, id):
    agenda = get_object_or_404(Agenda, pk=id)
    return render(request, 'sistema/detalhar_agenda.html', {'agenda':agenda})

def marcar_consulta(request, id, pk):
    agenda = get_object_or_404(Agenda, pk=id)
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.consulta.add(agenda)
    return render(request, 'sistema/area_do_cliente.html', {'cliente':cliente})


    ###### CADASTROS  ######

def cadastrar_epecialidade(request):
    if request.method == "POST":
        form = EspecialidadeForm(request.POST, request.FILES)
        if form.is_valid():
            especialidade = form.save(commit=False)
            form.save()
            return redirect('cadastrar_epecialidade')
    else:
        form = EspecialidadeForm()
    
    return render(request,'sistema/cadastrar_epecialidade.html', {'form': form})

def cadastrar_medico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST, request.FILES)
        if form.is_valid():
            medico = form.save(commit=False)
            form.save()
            return redirect('cadastrar_medico')
    else:
        form = MedicoForm()

    return render(request, 'sistema/cadastrar_medico.html', {'form': form})

def inserir_horarios(request):
    if request.method == 'POST':
        form = HorariosForm(request.POST, request.FILES)
        if form.is_valid():
            horarios = form.save(commit=False)
            form.save()
            return redirect('inserir_horarios')
    else:
        form = HorariosForm()
    return render(request, 'sistema/inserir_horarios.html',{'form':form})

def criar_nova_agenda(request):
    if request.method == "POST":
        form = AgendaForm(request.POST, request.FILES)
        if form.is_valid():
            agenda = form.save(commit=False)
            form.save()
            return redirect('listar_agendas')
    else:
        form = AgendaForm()
    return render(request, 'sistema/criar_nova_agenda.html',{'form':form})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'sistema/cadastrar_cliente.html',{'form': form})

    ###### LOGINS E AUTENTICAÇÕES ######

def login_adm(request):
    return render(request, 'sistema/login_adm.html', {})

def administracao(request, id):
    adm = get_object_or_404(User, id=id)
    return render(request, 'sistema/administracao.html',{'adm': adm})

def autenticar_administrador(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_superuser:
        login(request, user)
        id = user.id
        adm = get_object_or_404(User, pk=id)
        return render(request, 'sistema/administracao.html',{'adm':adm})
    else:
        return render(request, 'sistema/login_adm.html',{})

def area_do_cliente(request,id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'sistema/area_do_cliente.html',{'cliente':cliente})

def autenticar_cliente(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        id = user.id
        cliente = get_object_or_404(Cliente, pk=id)
        return render(request, 'sistema/area_do_cliente.html', {'cliente':cliente})
    else:
        return render(request, 'sistema/home.html',{})

def logout_usuario(request):
    logout(request)
    return render(request, 'sistema/home.html',{})


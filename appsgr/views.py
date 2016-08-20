from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appsgr.forms import *
from django.forms import formset_factory
from django.http.request import QueryDict
from django.contrib import messages
from appsgr.models import *
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here..

@login_required(login_url='login')
def home(request):
    return render(request,'base.html')

@login_required(login_url='login')
def erro_permissao(request):
    return render(request,'utils/permissao.html')

@permission_required('appsgr.view_requerimento',login_url='erro_permissao')
def requerimento_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        requerimento=Requerimento.objects.filter(descricao__contains=criterio).order_by('tipo_requerimento','-data_solicitacao_requerimento')
    else:
        requerimento=Requerimento.objects.all().order_by('tipo_requerimento','-data_solicitacao_requerimento')
        criterio=""
    #Cria o mecanimos de paginação
    paginator=Paginator(requerimento,10)
    page=request.GET.get('page')
    try:
        requerimento=paginator.page(page)
    except PageNotAnInteger:
        requerimento=paginator.page(1)
    except EmptyPage:
        requerimento=paginator.page(paginator.num_pages)

    dados={'requerimento':requerimento,'criterio':criterio,'paginator':paginator,'page_obj':requerimento}
    return render(request, 'requerimento/requerimento_list.html', dados)

@permission_required('appsgr.detail_requerimento',login_url='erro_permissao')
def requerimento_detail(request, pk):
    requerimento=Requerimento.objects.get(id=pk)
    return render(request, 'requerimento/requerimento_detail.html', {'requerimento':requerimento})

@permission_required('appsgr.new_requerimento',login_url='erro_permissao')
def requerimento_new(request):
    if (request.method=="POST"):
        form=RequerimentoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('requerimento_list')
    else:
        form=RequerimentoForm()
    dados={'form':form}
    return render(request, 'requerimento/requerimento_form.html', dados)

@permission_required('appsgr.update_requerimento',login_url='erro_permissao')
def requerimento_update(request,pk):
    requerimento=Requerimento.objects.get(id=pk)
    if (request.method=="POST"):
        form=RequerimentoForm(request.POST,instance=requerimento)
        if (form.is_valid()):
            form.save()
            return redirect('requerimento_list')
    else:
        form=RequerimentoForm(instance=requerimento)
    dados={'form':form,'requerimento':requerimento}
    return render(request, 'requerimento/requerimento_form.html', dados)

@permission_required('appsgr.delete_requerimento',login_url='erro_permissao')
def requerimento_delete(request,pk):
    requerimento=Requerimento.objects.get(id=pk)
    try:
        requerimento.delete()
    except IntegrityError:
        messages.error(request, 'Requerimento Vinculado a um Aluno')
        return redirect('requerimento_list')
    return redirect('requerimento_list')

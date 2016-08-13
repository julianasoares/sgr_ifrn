from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appsgr.forms import *
from django.forms import formset_factory
from django.http.request import QueryDict
from django.contrib import messages
from appsgr.models import *
# Create your views here..

def home(request):
    return render(request,'base.html')

def requerimento_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        requerimento=Requerimento.objects.filter(descricao__contains=criterio).order_by('descricao')
    else:
        requerimento=Requerimento.objects.all().order_by('descricao')
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

def requerimento_detail(request, pk):
    requerimento=Requerimento.objects.get(id=pk)
    return render(request, 'requerimento/requerimento_detail.html', {'requerimento':requerimento})

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

def requerimento_update(request,pk):
    requerimento=Requerimento.objects.get(id=pk)
    if (request.method=="POST"):
        form=RequerimentoForm(request.POST,instance=requerimento)
        if (form.is_valid()):
            form.save()
            return redirect('unidade_list')
    else:
        form=RequerimentoForm(instance=requerimento)
        dados={'form':form,'requerimento':requerimento}
        return render(request, 'requerimento/requerimento_form.html', dados)

def requerimento_delete(request,pk):
    requerimento=Requerimento.objects.get(id=pk)
    try:
        requerimento.delete()
    except IntegrityError:
        messages.error(request, 'Requerimento Vinculado a um Aluno')
        return redirect('requerimento_list')
    return redirect('requerimento_list')

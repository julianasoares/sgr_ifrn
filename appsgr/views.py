from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appsgr.forms import *
from django.forms import modelform_factory
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
    tipo_requerimento=Tipo_Requerimento.objects.all().order_by('nome')
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

    dados={'requerimento':requerimento,'criterio':criterio,'paginator':paginator,'page_obj':requerimento, "tipo_requerimento":tipo_requerimento}
    return render(request, 'requerimento/requerimento_list.html', dados)

@permission_required('appsgr.detail_requerimento',login_url='erro_permissao')
def requerimento_detail(request, pk):
    requerimento=Requerimento.objects.get(id=pk)
    return render(request, 'requerimento/requerimento_detail.html', {'requerimento':requerimento})

@permission_required('appsgr.add_requerimento',login_url='erro_permissao')
def requerimento_new(request):

    if (request.method=="GET"):
        id_tipo_requerimento = request.GET.get("id_tipo_requerimento")
        request.session[0]=id_tipo_requerimento
    else:
        id_tipo_requerimento=request.session['0']

    if(id_tipo_requerimento=="1"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="2"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('disciplina_cursada','disciplina_curso_atual','observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="3"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="4"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="5"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('data_realizacao_certificacao','disciplina_certificacao','observacoes',))
    elif(id_tipo_requerimento=="6"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="7"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="8"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="9"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('data_falta_dia','observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="10"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('data_faltas_de','data_faltas_ate','observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="11"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="12"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="13"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('curso_destino','observacoes',))
    elif(id_tipo_requerimento=="14"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('turma_destino','observacoes',))
    elif(id_tipo_requerimento=="15"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('turno_destino','observacoes',))
    elif(id_tipo_requerimento=="16"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="17"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="18"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="19"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="20"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('professor_atividade','tipo_atividadea','observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="21"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="22"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('observacoes','documentos_apresentados','documentos_files',))
    elif(id_tipo_requerimento=="23"):
        RequerimentoFormNovo=modelform_factory(Requerimento,fields=('tranferencia_escola_origem','tranferencia_escola_destino','tranferencia_curso_origem','tranferencia_curso_destino','observacoes','documentos_apresentados','documentos_files',))

    if (request.method=="POST"):
        form=RequerimentoFormNovo(request.POST)
        if (form.is_valid()):
            requerimento=form.save(commit=False)
            requerimento.tipo_requerimento=Tipo_Requerimento.objects.get(id=id_tipo_requerimento)
            if(id_tipo_requerimento==13):
                pass
            if(id_tipo_requerimento==14):
                pass
            if(id_tipo_requerimento==15):
                pass
            requerimento.aluno = Aluno.objects.get(username=request.user.username)
            requerimento.save()
            return redirect('requerimento_list')
    else:
        form=RequerimentoFormNovo()
    if (id_tipo_requerimento=="13"):
        curso=Aluno.objects.get(username=request.user.username).curso #Localiza qual o curso do aluno
        #Modifica a propriedade queryset do campo curso_destino, para incluir cursos da mesma modalidade, porém diferente o curso atual
        form.fields['curso_destino'].queryset=Curso.objects.filter(modalidade=curso.modalidade).exclude(pk=curso.pk)
        '''
            Referências para essa implementação
            http://stackoverflow.com/questions/4880842/how-to-dynamically-set-the-queryset-of-a-models-modelchoicefield-on-a-forms-form
            https://docs.djangoproject.com/pt-br/1.10/ref/models/querysets/#django.db.models.query.QuerySet.exclude
        '''
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

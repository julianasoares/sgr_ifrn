from django.db import models

#Modelo campus
class Campus(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    endereco = models.CharField("Endereço", max_length=100, null=False)
    bairro = models.CharField("Bairro", max_length=100, null=False)
    cidade = models.CharField("Cidade", max_length=100, null=False)
    numero = models.IntegerField("Número", null=False)
    telefone = models.CharField("Telefone", max_length=11, null=False)


#Modelo modalidades de curso
class ModalidadeCurso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = models.CharField("Nível", max_length=50, null=False)

#Modelo turno
class Turno(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = models.CharField("Nível", max_length=50, null=False)


#Modelo realcao professor com disciplina
class ProfessorDisciplina(models.Model):
    relacao_ativa = models.BooleanField("Professor ativo na disciplina", null=False, default=True)

#Modelo permissao
class Permissao(models.Model):
    nome = models.CharField("Permissao", max_length=50, null=False)

#Modelo pessoa
class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=250, null=False)
    data_nascimento = models.DateField("Data de Nascimento", null=False, blank=False)
    cpf = models.CharField("CPF", max_length=14, unique=True, null=False)
    email = models.EmailField("E-Mail", max_length=150, blank=True)
    telefone = models.CharField("Telefone", max_length=11)
    matricula = models.CharField("Matrícula", max_length=14, null=False, primary_key=True)
    senha = models.CharField("Matrícula", max_length=15, null=False)

#Modelo coordenador
class Coordenador(Pessoa):
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")
    ativo = models.BooleanField("Coordenador Ativo", null=False, default=True)

#Modelo diretor
class Diretor(Pessoa):
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")
    ativo = models.BooleanField("Diretor Ativo", null=False, default=True)

#Modelo relação diretor com campus
class DiretorCampus(models.Model):
    diretor = models.ForeignKey(Diretor, on_delete=models.PROTECT, verbose_name="Coordenador")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name="Campus")
    class Meta:
        unique_together = ('diretor',)

#Modelo curso
class Curso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    periodos = models.IntegerField("Períodos", null=False, default=0)
    anos = models.DecimalField("Anos",max_digits=2,decimal_places=2)
    ativo = models.BooleanField("Curso Ativo", null=False, default=True)
    modalidade = models.ForeignKey(ModalidadeCurso, on_delete=models.PROTECT, verbose_name="Modalidade")
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT, verbose_name="Turno")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name="Modalidade")
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT, verbose_name="Coordenador")
    class Meta:
       unique_together = (('nome', 'modalidade', 'turno','campus'),)

#Modelo aluno
class Aluno(Pessoa):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")

#Modelo turma
class Turma(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    alunos = models.ManyToManyField(Aluno)


#Modelo professor
class Professor(Pessoa):
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")
    ativo = models.BooleanField("Professor Ativo", null=False, default=True)

#Modelo disciplina
class Disciplina(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    ativa = models.BooleanField("Disciplina Ativa", null=False, default=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    professores= models.ManyToManyField(Professor)

#Modelo tecnico administrativo
class Tecnico_Administrativo(Pessoa):
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")

#Modelo documento
class Documento(models.Model):
    nome = models.CharField("Nome", max_length=100, null=False)

#Modelo tipo requerimento
class Tipo_Requerimento(models.Model):
    nome = models.CharField("Nome", max_length=100, null=False)

#Modelo requerimento
class Requerimento(models.Model):
    id = models.BigIntegerField("id", unique=True, primary_key=True)
    data_solicitacao_requerimento = models.DateTimeField("Data da solicitação", null=False, blank=False, auto_now_add=True, editable=False)
    tipo_requerimento = models.ForeignKey(Tipo_Requerimento, on_delete=models.PROTECT, verbose_name="Tipo de Requerimento")
    disciplina_cursada = models.CharField("Disciplina Cursada", max_length=150, null=False)
    disciplina_curso_atual = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name="Disciplina_do_Curso_Atual", null=True)
    observacoes = models.TextField("Observações", blank=True)
    data_realizacao_certificacao=models.DateField("Data da realização da certificação", null=False, blank=False)
    encaminhamentos = models.TextField("Encaminhamentos", blank=True)
    mudanca_de = models.CharField("De", max_length=100, null=False)
    mudanca_para = models.CharField("Para", max_length=100, null=False)
    data_faltas_de = models.DateField("Faltas de", null=False, blank=False)
    data_faltas_ate = models.DateField("Faltas até", null=False, blank=False)
    data_falta_dia = models.DateField("Faltas dia", null=False, blank=False)
    curso_origem = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="Curso_de_Origem", null=True)
    curso_destino = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="Curso_de_Destino", null=True)
    turma_origem = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name="Turma_de_Origem", null=True)
    turma_destino = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name="Turma_de_Destino", null=True)
    turno_origem = models.ForeignKey(Turno, on_delete=models.PROTECT, related_name="Turno_de_Origem", null=True)
    turno_destino = models.ForeignKey(Turno, on_delete=models.PROTECT, related_name="Turno_de_Destino", null=True)
    periodo_trancamento = models.IntegerField("Período de Trancamento", null=True)
    outros = models.TextField("Outros", blank=True)
    justificava = models.TextField("Justificativa", blank=True)
    observacoes_analise_aproveitamento = models.TextField("Observações da análise do aproveitamento", blank=True)
    observacoes_documentos_apresentados = models.TextField("Observações dos documentos apresentados", blank=True)
    resultado = models.NullBooleanField("Resultado")
    data_atividade = models.DateField("Data da atividade", null=False, blank=False)
    tipo_atividade = models.CharField("Tipo de atividade", max_length=50, null=False)
    tranferencia_escola_origem = models.CharField("Escola de origem", max_length=50, null=False)
    tranferencia_escola_destino = models.CharField("Escola de destino", max_length=50, null=False)
    tranferencia_curso_origem = models.CharField("Curso de origem", max_length=50, null=False)
    tranferencia_curso_destino = models.CharField("Curso de destino", max_length=50, null=False)
    apto_avaliacao = models.NullBooleanField("Apto para avalição")
    disciplina_certificacao = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name="Disciplina_Certificação")

#Modelo documentos apresentados
class Documento_Apresentado(models.Model):
    id = models.BigIntegerField("id", unique=True, primary_key=True)
    documento = models.ForeignKey(Documento, on_delete=models.PROTECT, verbose_name="Documento")
    requerimento = models.ForeignKey(Requerimento, on_delete=models.PROTECT, verbose_name="Requerimento")
    class Meta:
       unique_together = (('requerimento', 'documento'))
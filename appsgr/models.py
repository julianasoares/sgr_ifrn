from django.db import models

#Modelo campus
class Campus(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    endereco = models.CharField("Endereço", max_length=100, null=False)
    bairro = models.CharField("Bairro", max_length=100, null=False)
    cidade = models.CharField("Cidade", max_length=100, null=False)
    numero = models.IntegerField("Número", max_length=100, null=False)
    telefone = models.CharField("Telefone", max_length=11, null=False)


#Modelo modalidades de curso
class ModalidadeCurso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = nome = models.CharField("Nível", max_length=50, null=False)

#Modelo turno
class Turno(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = nome = models.CharField("Nível", max_length=50, null=False)


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
    matricula = models.CharField("Matrícula", max_length=14, null=False, unique=True)
    senha = models.CharField("Matrícula", max_length=15, null=False, unique=True)

#Modelo coordenador
class Coordenador(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Coordenador", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")
    ativo = models.BooleanField("Coordenador Ativo", null=False, default=True)

#Modelo diretor
class Diretor(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Diretor", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")
    ativo = models.BooleanField("Diretor Ativo", null=False, default=True)

#Modelo relação diretor com campus
class DiretorCampus(models.Model):
    diretor = models.ForeignKey(Diretor, on_delete=models.PROTECT, verbose_name="Coordenador", unique=True)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name="Campus")

#Modelo cuso
class Curso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    periodos = models.IntegerField("Períodos", null=False, default=0)
    anos = models.DecimalField("Anos",max_digits=2,decimal_places=2)
    ativo = models.BooleanField("Curso Ativo", null=False, default=True)
    modalidade = models.ForeignKey(ModalidadeCurso, on_delete=models.PROTECT, verbose_name="Modalidade")
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT, verbose_name="Turno")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name="Modalidade")
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT, verbose_name="Coordenador")
    #class Meta:
     #   unique_together = (('nome', 'modalidade', 'turno','campus'),)

#Modelo aluno
class Aluno(Pessoa):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Aluno", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")

#Modelo turma
class Turma(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    alunos = models.ManyToManyField(Aluno,through="AlunosTurma")


#Modelo professor
class Professor(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Professor", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")
    ativo = models.BooleanField("Professor Ativo", null=False, default=True)

#Modelo disciplina
class Disciplina(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    ativa = models.BooleanField("Disciplina Ativa", null=False, default=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    professores= models.ManyToManyField(Professor,through="ProfessorDisciplina")

#Modelo tecnico administrativo
class Tecnico_Administrativo(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Tecnico_Administrativo", unique=True)
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
    disciplina_curso_atual = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name="Disciplina do Curso Atual")
    observacoes = models.TextField("Observações", blank=True)
    data_realizacao_certificacao=models.DateField("Data da realização da certificação", null=False, blank=False)
    encaminhamentos = models.TextField("Encaminhamentos", blank=True)
    mudanca_de = models.CharField("De", max_length=100, null=False)
    mudanca_para = models.CharField("Para", max_length=100, null=False)
    data_faltas_de = models.DateField("Faltas de", null=False, blank=False)
    data_faltas_ate = models.DateField("Faltas até", null=False, blank=False)
    data_falta_dia = models.DateField("Faltas dia", null=False, blank=False)
    curso_origem = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso de Origem")
    curso_destino = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso de Destino")
    turma_origem = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turma de Origem")
    turma_destino = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turma de Destino")
    turno_origem = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turno de Origem")
    turno_destino = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turno de Destino")
    periodo_trancamento = models.IntegerField("Período de Trancamento", null=False, default=0)
    outros = models.TextField("Outros", blank=True)
    justificava = models.TextField("Justificativa", blank=True)
    observacoes_analise_aproveitamento = models.TextField("Observações da análise do aproveitamento", blank=True)
    observacoes_documentos_apresentados = models.TextField("Observações dos documentos apresentados", blank=True)
    resultado = models.BooleanField("Resultado", null=True)
    data_atividade = models.DateField("Data da atividade", null=False, blank=False)
    tipo_atividade = models.CharField("Tipo de atividade", max_length=50, null=False)
    tranferencia_escola_origem = models.CharField("Escola de origem", max_length=50, null=False)
    tranferencia_escola_destino = models.CharField("Escola de destino", max_length=50, null=False)
    tranferencia_curso_origem = models.CharField("Curso de origem", max_length=50, null=False)
    tranferencia_curso_destino = models.CharField("Curso de destino", max_length=50, null=False)
    apto_avaliacao = models.BooleanField("Apto para avalição", null=True)
    disciplina_certificacao = models.ForeignKey(Disciplina, on_delete=models.PROTECT, verbose_name="Disciplina")

#Modelo documentos apresentados
class Documento_Apresentado(models.Model):
    id = models.BigIntegerField("id", unique=True, primary_key=True)
    documento = models.ForeignKey(Documento, on_delete=models.PROTECT, verbose_name="Documento")
    requerimento = models.ForeignKey(Requerimento, on_delete=models.PROTECT, verbose_name="Requerimento")
    #class Meta:
     #   unique_together = (('requerimento', 'documento'))



































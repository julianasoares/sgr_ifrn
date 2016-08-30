from django.db import models
from django.contrib.auth.models import User, Group


class Grupo(Group):
    descricao = models.CharField("Grupo", max_length=20)

#Modelo pessoa
class Pessoa(User):
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)
    cpf = models.CharField("CPF", max_length=14, unique=True, null=False)
    telefone = models.CharField("Telefone",max_length=11, blank=True, null=True)
    grupos = models.ManyToManyField(Grupo)

#Modelo diretor
class Diretor(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT, verbose_name="Pessoa", null=False, primary_key=True)
    ativo = models.BooleanField("Diretor Ativo", null=False, default=True)

    def __str__(self):
        return self.pessoa.first_name

#Modelo campus
class Campus(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    endereco = models.CharField("Endereço", max_length=100, null=False)
    bairro = models.CharField("Bairro", max_length=100, null=False)
    cidade = models.CharField("Cidade", max_length=100, null=False)
    numero = models.IntegerField("Número", null=False)
    telefone = models.CharField("Telefone", max_length=11, null=False)
    diretores = models.ManyToManyField(Diretor)
    def __str__(self):
        return self.nome


#Modelo modalidades de curso
class ModalidadeCurso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = models.CharField("Nível", max_length=50, null=False)

    def __str__(self):
        return self.nome


#Modelo turno
class Turno(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)

    def __str__(self):
        return self.nome



#Modelo realcao professor com disciplina
class ProfessorDisciplina(models.Model):
    relacao_ativa = models.BooleanField("Professor ativo na disciplina", null=False, default=True)







#Modelo coordenador
class Coordenador(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT, verbose_name="Pessoa", null=False, primary_key=True)
    ativo = models.BooleanField("Coordenador Ativo", null=False, default=True)

    def __str__(self):
        return self.pessoa.first_name





#Modelo professor
class Professor(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT, verbose_name="Pessoa", null=False, primary_key=True)
    ativo = models.BooleanField("Professor Ativo", null=False, default=True)

    def __str__(self):
        return self.pessoa.first_name

#Modelo disciplina
class Disciplina(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    ativa = models.BooleanField("Disciplina Ativa", null=False, default=True)
    professores= models.ManyToManyField(Professor)

    def __str__(self):
        return self.nome

#Modelo curso
class Curso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    periodos = models.IntegerField("Períodos", null=False, default=0)
    anos = models.DecimalField("Anos",max_digits=2,decimal_places=1)
    ativo = models.BooleanField("Curso Ativo", null=False, default=True)
    modalidade = models.ForeignKey(ModalidadeCurso, on_delete=models.PROTECT, verbose_name="Modalidade")
    turnos = models.ManyToManyField(Turno)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name="Modalidade")
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT, verbose_name="Coordenador")
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome+' - Campus: '+self.campus.nome

#Modelo turma
class Turma(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT, verbose_name="Turno")

    def __str__(self):
        return self.nome


#Modelo aluno
class Aluno(Pessoa):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, verbose_name="Turma")

    def __str__(self):
        return self.first_name


#Modelo tecnico administrativo
class Tecnico_Administrativo(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.PROTECT, verbose_name="Pessoa", null=False, primary_key=True)
    campus_atuante = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name="Campus Atuação", null=False)
    def __str__(self):
        return self.pessoa.first_name

#Modelo documento
class Documento(models.Model):
    nome = models.CharField("Nome", max_length=100, null=False)

    def __str__(self):
        return self.nome

#Modelo tipo requerimento
class Tipo_Requerimento(models.Model):
    nome = models.CharField("Nome", max_length=100, null=False)

    def __str__(self):
        return self.nome


def aluno_directory_path(instance, filename):
    return 'func_{0}/{1}'.format(instance.aluno.username, filename)

#Modelo requerimento
class Requerimento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, related_name="Aluno", null=False)
    data_solicitacao_requerimento = models.DateTimeField("Data da solicitação", null=True, blank=True, auto_now_add=True, editable=False)
    tipo_requerimento = models.ForeignKey(Tipo_Requerimento, on_delete=models.PROTECT, verbose_name="Tipo de Requerimento", null=False)
    disciplina_cursada = models.CharField("Disciplina Cursada", max_length=150, null=True, blank=True)
    disciplina_curso_atual = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name="Disciplina_do_Curso_Atual", null=True, blank=True)
    observacoes = models.TextField("Observações", blank=True, null=True)
    data_realizacao_certificacao=models.DateField("Data da realização da certificação", null=True, blank=True)
    disciplina_certificacao = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name="Disciplina_Certificacao", null=True, blank=True)
    resultado_certificacao = models.NullBooleanField("Resultado", default="null")
    encaminhamentos = models.TextField("Encaminhamentos", null=True ,blank=True)
    data_faltas_de = models.DateField("Faltas de", null=True, blank=True)
    data_faltas_ate = models.DateField("Faltas até", null=True, blank=True)
    data_falta_dia = models.DateField("Falta dia", null=True, blank=True)
    curso_origem = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="Curso_de_Origem", null=True, blank=True)
    curso_destino = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="Curso_de_Destino", null=True, blank=True)
    turma_origem = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name="Turma_de_Origem", null=True, blank=True)
    turma_destino = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name="Turma_de_Destino", null=True, blank=True)
    turno_origem = models.ForeignKey(Turno, on_delete=models.PROTECT, related_name="Turno_de_Origem", null=True, blank=True)
    turno_destino = models.ForeignKey(Turno, on_delete=models.PROTECT, related_name="Turno_de_Destino", null=True, blank=True)
    periodo_trancamento = models.IntegerField("Período de Trancamento", null=True, blank=True)
    outros = models.TextField("Outros", blank=True, null=True)
    justificava = models.TextField("Justificativa", blank=True, null=True)
    observacoes_analise_aproveitamento = models.TextField("Observações da análise do aproveitamento", blank=True, null=True)
    observacoes_documentos_apresentados = models.TextField("Observações dos documentos apresentados", blank=True, null=True)
    resultado = models.NullBooleanField("Resultado", blank=True, null=True, default="null")
    data_atividade = models.DateField("Data da atividade", null=True, blank=True)
    tipo_atividade = models.CharField("Tipo de atividade", max_length=50, null=True, blank=True)
    professor_atividade = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name="Professor_Atividade", null=True, blank=True)
    tranferencia_escola_origem = models.CharField("Escola de origem", max_length=50, null=True, blank=True)
    tranferencia_escola_destino = models.CharField("Escola de destino", max_length=50, null=True, blank=True)
    tranferencia_curso_origem = models.CharField("Curso de origem", max_length=50, null=True, blank=True)
    tranferencia_curso_destino = models.CharField("Curso de destino", max_length=50, null=True, blank=True)
    apto_avaliacao = models.NullBooleanField("Apto para avalição", default="null")
    disciplina_certificacao = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name="Disciplina_Certificação", null=True, blank=True)
    documentos_apresentados = models.ManyToManyField(Documento, null=True, blank=True)
    documentos_files = models.FileField(upload_to=aluno_directory_path,default="null", null=True)
    tecnico_responsavel = models.ForeignKey(Tecnico_Administrativo,on_delete=models.PROTECT, related_name="Tecnico_Responsavel", null=True, blank=True)
    encaminhado_para = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name="Avaliador", null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name="Turma", null=True, blank=True)

    def __str__(self):
            return self.id
    class Meta:
        permissions = (("view_requerimento","Can see requerimento"),("detail_requerimento","Can see detail requerimento"),)





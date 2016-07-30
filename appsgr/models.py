from django.db import models

class Campus(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = nome = models.CharField("Nível", max_length=50, null=False)


class ModalidadeCurso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = nome = models.CharField("Nível", max_length=50, null=False)

class Turno(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    nivel = nome = models.CharField("Nível", max_length=50, null=False)


class Curso(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    modalidade = models.ForeignKey(ModalidadeCurso, on_delete=models.PROTECT, verbose_name="Modalidade")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name="Modalidade")
    class Meta:
        unique_together = ('field1', 'field2',)

class Turma(models.Model):
    nome = models.CharField("Nome", max_length=50, null=False)
    campus = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso")


class Permissao(models.Model):
    nome = models.CharField("Permissao", max_length=50, null=False)


class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=250, null=False)
    data_nascimento = models.DateField("Data de Nascimento", null=False, blank=False)
    cpf = models.CharField("CPF", max_length=14, unique=True, null=False)
    email = models.EmailField("E-Mail", max_length=150, blank=True)
    telefone = models.CharField("Telefone", max_length=11)
    matricula = models.CharField("Matrícula", max_length=14, null=False, min_length=14, unique=True)
    senha = models.CharField("Matrícula", max_length=15, null=False, unique=True)


class Aluno(Pessoa):
    curso = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name="Curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Aluno", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")

class Coordenador(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Coordenador", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")

class Diretor(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Diretor", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")

class Professor(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Diretor", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")

class Tecnico_Administrativo(Pessoa):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, verbose_name="Tecnico_Administrativo", unique=True)
    permissao = models.ForeignKey(Permissao, on_delete=models.PROTECT, verbose_name="Permissao")






































from appsgr.models import *

dir1=Aluno(nome='Luan Medeiros Macena',cpf='11122233345',email='luan@luan.com',data_nascimento='1992-02-22',matricula='20142148000001', permissao=per1, telefone='84988887777', senha='123456')
dir1.save()
#Curso
cur1=Curso(nome='Sistemas Para Internet', )

#Permissões
per1=Permissao(nome='Aluno')
per2=Permissao(nome='Diretor')
per3=Permissao(nome='Coorcenador')
per4=Permissao(nome='Professor')
per5=Permissao(nome='Tecnico')

per1.save()
per2.save()
per3.save()
per4.save()
per5.save()

#Aluno
al1=Aluno(nome='Luan Medeiros Macena',cpf='11122233345',email='luan@luan.com',data_nascimento='1992-02-22',matricula='20142148000001', permissao=per1, telefone='84988887777', senha='123456')
al1.save()
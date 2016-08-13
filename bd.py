from appsgr.models import *



#Permissões
per1=Permissao(nome='Aluno')
per2=Permissao(nome='Diretor')
per3=Permissao(nome='Coordenador')
per4=Permissao(nome='Professor')
per5=Permissao(nome='Tecnico')

per1.save()
per2.save()
per3.save()
per4.save()
per5.save()




dir1=Diretor(nome='Felipe Quintaes',cpf='22233344456',email='felipe@felipe.com',data_nascimento="1979-02-20",matricula='20132148000001', permissao=per2, telefone='84977776666', senha='123456')
dir1.save()

cor1=Coordenador(nome='Givanaldo Rocha',cpf='33344455567',email='givanaldo@givanaldo.com',data_nascimento="1973-05-30",matricula='20122148000001', permissao=per2, telefone='84955556666', senha='123456')
cor1.save()

cam1 = Campus(nome='Parnamirim', telefone='40054108', cidade='Parnamirim', endereco='Rua Boa Esperança', bairro='Nova Esperança', numero=75, )
cam1.save()

mod1 =  ModalidadeCurso(nivel='Superior', nome='Superior')
mod1.save()

turn1 = Turno(nome='Matutino')
turn2 = Turno(nome='Verpertino')
turn3 = Turno(nome='Noturno')
turn1.save()
turn2.save()
turn3.save()

cur1=Curso(nome='Sistemas Para Internet', coordenador=cor1, ativo=True, campus=cam1, anos=3, modalidade=mod1, periodos=6, turno=turn2)
cur1.save()

al1=Aluno(nome='Luan Medeiros Macena',cpf='11122233345',email='luan@luan.com',data_nascimento='1992-02-22',matricula='20142148000001', permissao=per1, telefone='84988887777', senha='123456', curso=cur1)
al1.save()

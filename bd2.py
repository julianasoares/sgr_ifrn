from appsgr.models import *





#TEstando requerimento

doc1 = Documento(nome="CPF")
doc1.save()
doc2 = Documento(nome="RG")
doc2.save()

req = Requerimento()
req.save()
req.documento.add(doc1, doc2)


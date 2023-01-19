from django.db import models
from datetime import datetime
# Create your models here.

class Usuario(models.Model):
	username= models.CharField(
		max_length=50,
		blank=False,
		null=False,
		unique=True
	)
	nome = models.CharField(
		max_length = 50,
		blank = False,
		null = False
	)

	sobrenome = models.CharField(
		max_length = 50,
		blank = False,
		null = False
	)
	email = models.EmailField(
		max_length = 70,
		blank = False,
		unique = True
	)

	def __str__(self):
		return "%s %s" % (self.nome, self.sobrenome)


class Local(models.Model):
	cep = models.CharField(
		max_length = 9,
		blank = True,
		null = True
	)
	cidade = models.CharField(
		max_length = 50,
		blank = False,
		null = False
	)
	bairro = models.CharField(
		max_length = 50,
		blank = False,
		null = False
	)
	logradouro = models.CharField(
		max_length = 50,
		blank = False,
		null = False
	)
	uf = models.CharField(
		max_length = 2,
		blank = False,
		null = False
	)

	def __str__(self):
		return "%s, %s, %s, %s, %s" % (
			self.logradouro,
			self.bairro,
			self.cidade,
			self.uf,
			self.cep
		)

class Alagamento(models.Model):
	LEVE = 'LEVE'
	MODERADO = 'MODERADO'
	GRAVE = 'GRAVE'
	INTENSIDADE = (
		(LEVE,LEVE),
		(MODERADO,MODERADO),
		(GRAVE,GRAVE)
	)
	LOCALIZADO = 'LOCALIZADO'
	INTRANSITAVEL = 'INTRANSITAVEL'
	CLASSIFICACAO = (
		(LOCALIZADO,LOCALIZADO),
		(INTRANSITAVEL,INTRANSITAVEL)
	)

	reg_date = models.DateTimeField( 
		auto_now_add=True,

	)

	intensidade = models.CharField(
		max_length=20, 
		choices = INTENSIDADE, 
		default=LEVE
	)

	classificacao = models.CharField(
		max_length=20,
		choices = CLASSIFICACAO,
		default = LOCALIZADO
	)

	img1 = models.ImageField(null=True,blank=True)

	img2 = models.ImageField(null=True,blank=True)

	local = models.ForeignKey(Local, on_delete=models.CASCADE)

	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.local) + "(" +self.intensidade + "), " + str(self.reg_date)


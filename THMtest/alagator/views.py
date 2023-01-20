from django.shortcuts import render, redirect
from .form import RegistroUsuario, LoginUsuario
from .model import Usuario, Local, Alagamento
# Create your views here.

class Home(View):
	context = {}

	def get(self,request):
		valido =False
		form = LoginUsuario()
		self.context['valido'] = valido
		self.context['form']= form
		self.context['alagamento'] = Alagamento.objects.all()
		return render(request,'index.html',self.context)

	def post(self,request):
		valido = False

		form = LoginUsuario(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			for usuario in Usuario.objects.all():
				if(usuario.username == username && usuario.email == email):
					valido = True
					user = usuario
		self.context['form'] = form
		self.context['valido'] = valido
		self.context['alagamento'] = Alagamento.objects.all()
		self.context['user'] = user
		return render(request, 'index.html', self.context)


class Registro(View):
	context={}
	def get(self,request):
		form = RegistroUsuario()
		self.context['form'] = form
		return render(request,'registro.html',self.context)
	def post(self,request):
		form = RegistroUsuario(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('/'))

		self.context['form'] = form
		return render(request,"registro.html", self.context)


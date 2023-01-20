from django import forms
from .model import Usuario,Local,Alagamento

class LoginUsuario(form.ModelsForm):
	template_name = "index.html"
	class Meta:
		model = Usuario
		fields = ('username','email')

class RegistroUsuario(form.ModelForm):
	class Meta:
		model = Usuario
		fields = ('username', 'nome','sobrenome','email')
from django import forms
from .model import Usuario,Local,Alagamento

class RegistroUsuario(form.ModelForm):
	class Meta:
		model = Usuario
		fields = ('username', 'nome','sobrenome','email')
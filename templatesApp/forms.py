from django import forms
from templatesApp.models import Profesor
from templatesApp.models import Alumnos
from templatesApp.models  import Apoderado

class FormProfesor(forms.ModelForm):
    class Meta:
        model=Profesor
        fields='__all__'

class FormAlumnos(forms.ModelForm):
    class Meta:
        model=Alumnos
        fields='__all__'

class FormApoderado(forms.ModelForm):
    class Meta:
        model=Apoderado
        fields='__all__'

def clean_email(self):
    inputEmail=self.cleaned_data['correo']
    if inputEmail.find('@')==-1:
        raise forms.ValidationError("El correo debe contener @")
    return inputEmail



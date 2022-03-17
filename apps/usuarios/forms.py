from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from apps.usuarios.models import Usuario


class FormularioLogin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'

#Formulario para los usuarios normales importados a travez de un modelo(Usuario)
class FormularioUsuario(forms.ModelForm):
    """ Formulario de registro de un usuario en la base de datos

    se define variables:
                -password1: contraseña
                -password2: verificacion de la contraseña
    """
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Ingrese la contraseña...',
            'id' : 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Contraseña de Confirmacion', widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente la contraseña...',
            'id' : 'password2',
            'required': 'required',
        }
    ))
     

    class  Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        Widget ={
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'label':'Correo Electronico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese sus apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su nombre de usuario',
                }
            ),
        }


    def clean_password2(self):
        """VALIDACION DE LA CONTRASEÑA

        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base de datos y retorna la contraseña valida

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra el mensaje del error
        """
      
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('contraseñas no coinciden!')
        return password2

# Definimos el constructor interno que tiene la clase e invocamos el metodo save del modelo y encriptamos el password 
    def save(self, commit = True):
        user = super().save(commit= False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
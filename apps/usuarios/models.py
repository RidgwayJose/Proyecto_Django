from django import forms
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Definir 2 funciones donde se crea 2 usuarios: el normal y el administrador
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres,apellidos,password= None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        # El metodo normalize significa proporcionar una representación canónica, de modo que dos cadenas de correo electrónico equivalentes se normalicen a lo mismo.
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos
        )
        
        #este metodo sirve para encriptar la contraseña y guardarlo bajo el mismo parametro password
        #este metodo se encuentra en el modelo Abastractbaseuser
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,username,email,nombres,apellidos,password):
        usuario = self.create_user(
            email,
            username= username,
            nombres = nombres,
            apellidos= apellidos,
            password= password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

#Modelo del usuario
class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)

    # usuario normal y el usuario administrador
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['email', 'nombres', 'apellidos']


    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'
    
#Se define para que se pueda utilizar el modelo en el administrador usuarios y genera los permisos para administrador

    def has_perm(self,perm,obj = None):
        return True 
    
#Se define la etiqueta para la aplicacion 
    def has_module_perms(self, app_label):
        return True
    
#verifica y autoriza si un usuario es administrador
    @property
    def is_staff(self):
        return self.usuario_administrador


    """def clean_password2(self):
      
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit= False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user"""
  
    """VALIDACION DE LA CONTRASEÑA

        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base de datos y retorna la contraseña valida

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra el mensaje del error
        """
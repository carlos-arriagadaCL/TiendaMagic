from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CuentaManager(BaseUserManager):
    def create_user(self, nombre, apellido, username, email, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener un email válido.')

        if not username:
            raise ValueError('Los usuarios deben tener un username válido.')

        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, apellido, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Cuenta(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=9, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultimo_ingreso = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre', 'apellido']

    objects = CuentaManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.nombre + ' ' + self.apellido

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
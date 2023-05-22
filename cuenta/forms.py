from django import forms
from .models import Cuenta

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Contraseña',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar contraseña',
    }))
    class Meta:
        model = Cuenta
        fields = ('nombre', 'apellido', 'email', 'telefono', 'password')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Las contraseñas no coinciden.'
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['apellido'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['telefono'].widget.attrs['placeholder'] = 'Teléfono'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
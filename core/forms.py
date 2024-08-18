from django import forms
from .models import *
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField

class ContactoForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contacto
        fields = '__all__'


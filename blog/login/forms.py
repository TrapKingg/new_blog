import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=_("Username"), error_messages={'invalid': _("This value must be contain only letters, number and undescores.!")})
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Email Address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label=_("Type your password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label=_("Retype your password"))
    #photo = forms.ImageField(required=False)

    def clean_username(self):
        ##Comprueba que no exista un usuario igual en la db
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError(_("Username already exist, please try another one."))
        return username

    def clean_email(self):
        ##Comprueba que no exista otro email igual en la db
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError(_("Email already exist, please try another one."))
        return email

    def clean_password2(self):
        ##Comprueba que las dos contrasenas seas iguales
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError(_("Passwords didn't match, please try again."))
        return password2

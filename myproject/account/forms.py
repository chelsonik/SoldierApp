from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Haslo", widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Nie ma takiego uzytkownika')
            if not user.check_password(password):
                raise forms.ValidationError('Zle haslo')
            if not user.is_active:
                raise forms.ValidationError('Uzytkownik nieaktywny')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='Imie')
    last_name = forms.CharField(label='Nazwisko')
    username = forms.CharField(label='Login')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Haslo', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potwierdz haslo', widget=forms.PasswordInput)


    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'password2'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasla nie sa identyczne!')
        return cd['password2']

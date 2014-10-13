
from django import forms

def pass_match(pass1,pass2):
    if pass1 != pass2:
        return True
    else:
        return False

class SignInForm(forms.Form):
    username = forms.CharField(label="Enter username")
    password = forms.CharField(label="Enter password",widget=forms.PasswordInput())

class UserSignUpForm(forms.Form):
    name = forms.CharField(label="Enter your name")
    username = forms.CharField(label="Set a user name")
    pass1 = forms.CharField(label="Enter password",widget=forms.PasswordInput())
    pass2 = forms.CharField(label="ReEnter password",widget=forms.PasswordInput())
    college = forms.CharField(label="Enter your college name")

'''Data owner forms'''

class DOSignUpForm(forms.Form):
    name = forms.CharField(label="Enter your name")
    username = forms.CharField(label="Set a user name")
    pass1 = forms.CharField(label="Enter password",widget=forms.PasswordInput())
    pass2 = forms.CharField(label="ReEnter password",widget=forms.PasswordInput())
    pass_match(pass1,pass2)

class FileUploadForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

class TPA(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput())





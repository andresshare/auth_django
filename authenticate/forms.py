from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email Adress'}))
    first_name = forms.CharField( help_text="<strong>Enter your first name here </strong>", label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'forms-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<span class="form-text text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>"

        self.fields['password1'].widget.attrs['class'] = 'forms-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password2'].help_text = "<span class="form-text text-muted"><small><ul><li></li><li></li><li></li><li></li> </ul></small></span>"

        self.fields['password2'].widget.attrs['class'] = 'forms-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = "<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>"

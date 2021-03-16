from testapp.models import Comment,Video,Profile
from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('user','comment')

class SignUpform(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','last_name','email','password')

class PostcreateForm(forms.ModelForm):
    class Meta:
        model=Video
        fields='__all__'

class ProfilecreateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'                  

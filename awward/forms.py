from .models import Profile,Post,Rate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio','location']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254,help_text=False)
    class Meta:
        model = User
        fields = ('username','email')

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content', 'interface', 'content', 'experience' ]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)

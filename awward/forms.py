from .models import Profile,Post,Rate
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','bio']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254,help_text=False)
    class Meta:
        model = User
        fields = ('username','email')

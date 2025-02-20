from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, University

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        help_text='This is the name other users will see. Choose wisely!',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your preferred username'})
    )
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES, required=False)
    school = forms.ModelChoiceField(
        queryset=University.objects.all(),
        widget=forms.Select(attrs={'class': 'select2'}),
        required=False
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'birth_date', 'gender', 'school']

    def save(self, commit=True):
        user = super().save(commit=True)
        profile = user.profile
        profile.gender = self.cleaned_data.get('gender')
        profile.school = self.cleaned_data.get('school')
        profile.birth_date = self.cleaned_data.get('birth_date')
        profile.bio = self.cleaned_data.get('bio')
        if commit:
            profile.save()
        return user

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        help_text='This is the name other users will see. Choose wisely!',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your preferred username'})
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    school = forms.ModelChoiceField(
        queryset=University.objects.all(),
        widget=forms.Select(attrs={'class': 'select2'}),
        required=False
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['bio', 'birth_date', 'gender', 'school']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        } 
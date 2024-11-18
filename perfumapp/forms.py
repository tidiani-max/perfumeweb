# shop/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Perfume, Testimony

class OwnerSignupForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Profile.objects.create(user=user, is_owner=True)
        return user


class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfume
        fields = ['name', 'description', 'price', 'image', 'whatsapp_link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'whatsapp_link': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['name', 'testimony','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'testimony': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

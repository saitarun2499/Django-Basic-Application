from django import forms
from .models import Profiledetails

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiledetails
        fields = '__all__'
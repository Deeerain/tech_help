from django import forms
from .models import Work


class NewWorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        exclude = ('user', )

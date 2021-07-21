from django import forms

from Pythons.pythons_app.models import Python


class CreatePythonForm(forms.ModelForm):
    class Meta:
        model = Python
        fields = '__all__'

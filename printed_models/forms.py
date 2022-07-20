from django import forms
from django.forms import ModelForm

from .models import PrintedModel, PrintedModelImage


class PrintedModelForm(ModelForm):

    class Meta:
        model = PrintedModel
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class PrintedModelImageForm(ModelForm):

    class Meta:
        model = PrintedModelImage
        fields = '__all__'

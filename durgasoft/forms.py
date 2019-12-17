from django import forms
from django.core import validators
class StudentForm(forms.Form):
    #name=forms.CharField(widget=forms.Textarea)
    marks=forms.IntegerField()
    name = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(4)])
    def clean_name(self):
        print('validating name')
        a=self.cleaned_data['name']
        if len(a)>4:
            raise forms.ValidationError(message="Nothing use")
        return a

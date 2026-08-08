from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:

        model = Job

        fields = [
            "title",
            "company",
            "location",
            "remote",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Job Title",
                }
            ),

            "company": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Company Name",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Location",
                }
            ),

            "remote": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
from django import forms
from .models import Components, BriefDescription, AdvantageAndDisadvantage, Users


class ComponentsForm(forms.ModelForm):
    class Meta:
        model = Components

        fields = [
            "name",
            "image",
            "description"
        ]


class UsersForm(forms.ModelForm):
    name = forms.CharField(label="Name")

    class Meta:
        model = Users

        fields = '__all__'


class AdvantageAndDisadvantageForm(forms.ModelForm):
    class Meta:
        model = AdvantageAndDisadvantage

        fields = [
            "component",
            "text",
            "is_advantage"
        ]


class BriefDescriptionForm(forms.ModelForm):
    class Meta:
        model = BriefDescription

        fields = [
            "component",
            "text"
        ]

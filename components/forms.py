from django import forms
from .models import Components, BriefDescription, AdvantageAndDisadvantage


class ComponentsForm(forms.ModelForm):
    class Meta:
        model = Components

        fields = [
            "name",
            "image",
            "description"
        ]


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

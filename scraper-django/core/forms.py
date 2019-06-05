from django import forms


class ScraperForm(forms.Form):
    identifier = forms.CharField(max_length=200)

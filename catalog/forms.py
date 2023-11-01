from django import forms

class SongSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)

from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=255, label='Search Keyword', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter keyword',
        'aria-label': 'Search',
    }))

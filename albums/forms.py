from django import forms

class AlbumForm(forms.Form):
    title = forms.CharField(label='Your name', max_length=100)
    artist = forms.CharField(label='Artist', max_length=100)

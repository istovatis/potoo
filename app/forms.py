from django import forms

class NewPot(forms.Form):
    pot_text = forms.CharField(label='Do you have something to pot?', widget=forms.Textarea, max_length=140)

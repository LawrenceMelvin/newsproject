from django import forms
NEWS = [('bcc','BCC'),('hindu','The Hindu'),('verge','The Verge')]
class newsform(forms.Form):
    news = forms.ChoiceField(choices=NEWS)
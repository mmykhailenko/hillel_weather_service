from django import forms


class NameForm(forms.Form):
    city = forms.CharField(max_length=100)


class CoordForm(forms.Form):
    lon = forms.FloatField()
    lat = forms.FloatField()

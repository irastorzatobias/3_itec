from django import forms


class CarreraForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={'class': 'p-1 border border-gray-200 rounded-md w-1/2'}))
    duracion = forms.IntegerField(label='Duracion', min_value=1, max_value=5, widget=forms.NumberInput(
        attrs={'class': 'p-1 border border-gray-200 rounded-md inline-flex'}))

from django import forms

class StockForm (forms.Form):
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'date','placeholder':'01/01/1990','type':'date'}))
from django.shortcuts import render
from django.http import HttpResponse
from .forms import StockForm
import pickle
import yfinance as yf


def home(request):
 #   filename='/home/ms/Projects/Stock_Price_Prediction/stock-price-prediction/notebook/prediction.sav'
   # model=pickle.load(open(filename,'rb'))
    form=StockForm()
    if request.method=='POST':
        form=StockForm(request.POST)
        if form.is_valid():
            print('***************************************************************************************************************')
            date=form.cleaned_data['date']
            print(date)
            data=yf.download('AAPL',start=date,end=date)
            print(data)
    context={'form':form}
    return render(request,'home.html', context=context)


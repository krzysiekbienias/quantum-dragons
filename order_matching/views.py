from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request,"order_matching/landing_page.html")

def trade_book(request):
    return render(request,'order_matching/trade_book.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import customerReview
# Create your views here.
def generate(request):
    return render(request,'template1.html')

def proceed(request):
    """This function is for taking input from the form fields and to create a new user review in thr row of table database"""
    #cusre=customerReview()
    #cusre.bran_name="nokia"
    use_name=str(request.GET["user_name"])
    br_name=str(request.GET["brand_name"])
    pro_name=str(request.GET["product_name"])
    revi_text=str(request.GET["review_text"])
    customerReview.objects.create(user_name=use_name,bran_name=br_name,produ_name=pro_name,review_data=revi_text) #command that creates the new user row for product review in the database
    cusres=customerReview.objects.all() #the operation thta calls the all rows in table
    return render(request,'products.html',{'dests':cusres})
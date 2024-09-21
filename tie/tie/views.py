from django.shortcuts import render,redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == "GET":
         return render(request,"signup.html")
    else:
         firstname = request.get['firstname']
         lastname = request.get['lastname']
         email = request.get['email']
         password = request.get['pssword']
         cpassword = request.get['confirmpassword']
         print(firstname,lastname,email,password,cpassword)
         return render(request,"signup.html")

         

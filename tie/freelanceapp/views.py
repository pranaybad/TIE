from django.shortcuts import render

# Create your views here.


# Create your tests here.
def home(request):
    return render(request, 'freelanceapp/home.html')
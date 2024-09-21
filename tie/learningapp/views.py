from django.shortcuts import render

# Create your views here.
def learningapp(request):
    return render(request,'learningapp/learningapp.html')
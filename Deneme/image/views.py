from django.shortcuts import render
from .form import fileForm
from django.contrib import messages
# def home_view(request):
# 		return render(request, 'Home.html')
def home_view(request):
    form = fileForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'Başarılı Bir Şekilde Oluşturdunuz.')
    else:
        form  = fileForm()
    return render(request, 'home.html', {'form':form})

from django.shortcuts import render, HttpResponse

# Create your views here.

def hom_page(request):
  return render(request=request,template_name='index.html')

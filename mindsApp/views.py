from django.shortcuts import render
from .models import blogPage
from .models import dynamicPage
from .models import sliderPage


def index(request):
   sliderPagedata = sliderPage.objects.all()
   context = {
      'sliderPage' : sliderPagedata
   }
   return render(request, 'minds/index.html',context)

def agensy(request):
   return render(request, 'minds/agensy.html')

def blog(request):
   blogPagedata = blogPage.objects.all()[0]
   dynamicPagedata = dynamicPage.objects.all()
   context = {
      'blogPage' : blogPagedata,
      'dynamicPage' : dynamicPagedata
   }
   return render(request, 'minds/blog.html',context)

def contact(request):
   return render(request, 'minds/contact.html')

def cases(request):
   return render(request, 'minds/cases.html')

def case_detail(request):
   return render(request, 'minds/case-detail.html')

def blog_single(request):
   return render(request, 'minds/blog-single.html')

#def blog_single(request):
   #return render(request, 'minds/blog-single.html')
# Create your views here.

def login(request):
   return render(request, 'minds/login.html')
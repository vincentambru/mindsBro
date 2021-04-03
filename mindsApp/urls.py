from django.urls import path


from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('agensy/',views.agensy,name='agensy'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('cases/',views.cases,name='cases'),
    path('case_detail/',views.case_detail,name='case_detail'),
    path('blog_single/',views.blog_single,name='blog_single'),
    path('login/',views.login,name='login'),
]
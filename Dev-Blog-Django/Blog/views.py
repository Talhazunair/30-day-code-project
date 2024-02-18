from django.shortcuts import render,get_object_or_404
from . models import Post
from django.core.paginator import Paginator, Page
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.db.models import Q
# Create your views here.
def index(request):
    query = request.GET.get('q')
    all_posts=Post.objects.all().order_by('-published_date')
    if query:
        all_posts = all_posts.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    paginator=Paginator(all_posts,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'Blog/index.html',{
        'page_obj':page_obj
    })

def view_blog(request,slug):
    post=get_object_or_404(Post,slug=slug)
    return render(request,'Blog/view_blog.html',{
        'post':post
    })
    
def contact_page(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        send_mail(
            f"New Contact Form Submission from {name} {email}",
            message,
            email,
            ['talhazunair37@gmail.com'],
            fail_silently=False
        )
        return HttpResponseRedirect('/Thankyou')
    return render(request,'Blog/contact.html')

def about_page(request):
    return render(request,'Blog/about.html')

def thankyou_page(request):
    return render(request,'Blog/thankyou.html')

def search(request):
    title_to_search_by
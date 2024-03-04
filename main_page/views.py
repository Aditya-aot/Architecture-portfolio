from django.shortcuts import render
from .models import blogs_models , portfolio_models
# Create your views here.

def home(request) :
    all_blog      = blogs_models.objects.all()
    top_blog_view = all_blog.filter(top_blog=True)

    all_portfolio = portfolio_models.objects.all()
    top_portfolio= all_portfolio.filter(top_portfolio=True)

    context = {
        'top_blog' : top_blog_view[::-1] ,
        'top_portfolio' : top_portfolio
    }
    print(top_blog_view)
    return render(request, 'main_page/index.html',context)

def single_blog(request ,pk) :
    all_blog = blogs_models.objects.all()
    blog_detail = all_blog.filter(id=pk)

    context = {
        "blog_detail":blog_detail
    }
    return render(request, 'main_page/single-blog.html',context)

def all_blog(request) :
    all_blog = blogs_models.objects.all()
    top_blog_view = all_blog.filter(top_blog=True)

    context = {
        "all_blog" :all_blog ,
        "top_blog" : top_blog_view
    }
    return render(request, 'main_page/all_blog.html', context)


def single_portfolio(request , pk) :
    all_portfolio = portfolio_models.objects.all()
    portfolio_detail= all_portfolio.filter(id=pk)

    context = {
        "portfolio_detail" : portfolio_detail
    }
    return render(request, 'main_page/single-portfolio.html',context)

def all_portfolio(request) :
    all_portfolio = portfolio_models.objects.all()

    context = {
        "all_portfolio" :all_portfolio
    }
    return render(request, 'main_page/all_portfolio.html', context)

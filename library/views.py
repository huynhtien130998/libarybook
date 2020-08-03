from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Category, Book, Borrower, BorrowBook, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    bookitem = Book.objects.all()
    cateitem = Category.objects.all()

    paginator = Paginator(bookitem,3)
    page_Number = request.GET.get('page',1)
    try:
        bookpage = paginator.page(page_Number)
    except PageNotAnInteger:
        bookpage = paginator.page(1)
    except EmptyPage:
        bookpage = paginator.page(paginator.num_pages)

    context ={
        'book' : bookitem,
        'category' : cateitem,
        'paging' : bookpage,
        'cateview':cate_view,
    }
    return render(request, "library/index.html",context)


def cate_view(request, category_id):
    cate_view= Category.objects.get(pk = category_id)
    cateitem = Category.objects.all()

    context1={
        'cate':cate_view,
        'catename': cateitem,
    }
    return render(request, "library/cateview.html", context1)

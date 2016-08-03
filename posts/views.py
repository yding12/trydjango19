from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib import quote_plus

# Create your views here.
def post_detail(request,slug=None):
    # instance = Post.objects.get(slug=slug)
    instance = get_object_or_404(Post, slug=slug)
    # building up a query string to go into a URL
    context = {
        "title":"detail",
         "instance":instance,

    }
    return render(request, "post_detail.html", context)

def post_delete(request, slug=None):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "delete successfully")
    # return redirect("posts:list")
    return redirect("posts:list")

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Success Created", extra_tags="some_tags")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list,3)#show 5 psots every page
    page_request_var = "aaa"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context_data = {
        "title":"The Sweet Moment between Them",
        "object_list":queryset,
        "page_request_var": page_request_var

    }
    return render(request,"post_list.html",context_data)

def post_update(request, slug=None):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"update successfully")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title":instance.title,
        "instance":instance,
        "form":form
    }
    return render(request,"post_form.html", context)
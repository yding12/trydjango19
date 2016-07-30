from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def post_detail(request,id=None):
    #instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":"detail",
         "instance":instance
    }
    return render(request, "post_detail.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "delete successfully")
    # return redirect("posts:list")
    return redirect("posts:list")

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Success Created", extra_tags="some_tags")
    # if request.method == 'POST':
    #     print request.POST.get("content")
    #     print request.POST.get("title")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list,2)#show 5 psots every page
    page_request_var = "aaa"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context_data = {
        "title":"detail",
        "object_list":queryset,
        "page_request_var": page_request_var

    }
    return render(request,"post_list.html",context_data)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
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
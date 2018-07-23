
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import House
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render



from .forms import HouseForm


def houses_create(request):
    form = HouseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print (form.cleaned_data.get("title"))
        instance.save()

        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render (request, "house_form.html", context)


def houses_detail(request, id=None):
    instance = get_object_or_404(House, id =id)
    context = {
        "title": "instance.title",
        "instance": instance,
    }
    return render (request, "house_detail.html", context)
    #return HttpResponse("<h1>detail</h1>")

def houses_list(request):

    queryset_list = House.objects.all()
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
    page_request_var = "page"

    page = request.GET.get('page_request_var')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render (request, "house_list.html", context)
    #return HttpResponse("<h1>list</h1>")



def houses_update(request, id=None):
    instance = get_object_or_404(House, id =id)
    form = HouseForm(request.POST or None,request.FILES or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
        }
    return render (request, "house_form.html", context)

def houses_delete(request, id=None):
    instance = get_object_or_404(House, id =id)
    instance.delete()
    return redirect("houses:list")



from django.shortcuts import render, redirect, get_object_or_404
from .models import Soldier
from .forms import RawSoldierForm
# Create your views here.
def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Soldier, id=id)
    context = {
        "object": obj
    }
    return render(request, "soldiers/soldier_detail.html", context)

def soldier_list_view(request):
    queryset = Soldier.objects.all()
    context = {
            "object_list": queryset
        }
    return render(request, "soldiers/soldier_list.html", context)

def soldier_delete_view(request, id):
    obj = get_object_or_404(Soldier, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('/..')
    context = {
        "object": obj
    }
    return render(request, "soldiers/soldier_delete.html", context)


def soldier_create_view(request):
    my_form = RawSoldierForm()
    if request.method == "POST":
        my_form = RawSoldierForm(request.POST)
        if my_form.is_valid():
            Soldier.objects.create(**my_form.cleaned_data)
            return redirect('../')
    context ={
        "form": my_form
    }
    return render(request, "soldiers/soldier_create.html", context)

def soldier_detail_view(request):
    obj = Soldier.objects.get(id=2)
    context = {
        'object':obj
    }
    return render(request, "soldiers/soldier_detail.html", context)
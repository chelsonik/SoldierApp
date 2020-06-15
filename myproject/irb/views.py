from django.shortcuts import render, redirect
from cassandra.cluster import Cluster

from .forms import Presenceform


def presence_create_view(request):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('irb')
    my_form = Presenceform(request.POST or None)
    if my_form.is_valid():
        soldier_id = my_form.cleaned_data.get('soldier_id')
        name = my_form.cleaned_data.get('name')
        place = my_form.cleaned_data.get('place')
        date_w = my_form.cleaned_data.get('date_w')
        date_p = my_form.cleaned_data.get('date_p')
        stay = my_form.cleaned_data.get('stay')
        session.execute(
            "insert into presence(nr_ksiazeczki, imie_nazwisko, obecny, data_wyjazdu, data_powrotu, miejsce_pobytu) values ('" + str(soldier_id) + "','"+str(name)+"','" + str(place) + "','"+str(date_w)+"','"+str(date_p)+"','"+str(stay)+"');")
        return redirect('../')
    context = {
        "form": my_form
    }
    return render(request, "irb/presence_create.html", context)

def presence_list_view(request):
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('irb')
    command = "select * from irb.presence"
    results = session.execute(command)
    irb_list = []
    for result in results:
        irb_list.append(result)
    context = {
        "irb_list": irb_list
    }
    return render(request, "irb/presence_list.html", context)
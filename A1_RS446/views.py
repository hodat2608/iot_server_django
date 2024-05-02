from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from A1_RS446.models import A1,category
from server.models import server_test

def detail_date(request,id):
    date = A1.objects.filter(client_id = id)
    name_space_id = server_test.objects.get(id=id)
    name_space = name_space_id.name_client
    print(name_space)
    context = {'date': date,'name_space':name_space}
    return render(request, 'static/A1/index_date.html', context)

def detail_data(request,id):
    data = category.objects.filter(date_id = id)
    context = {'data': data}
    return render(request, 'static/A1/index_data.html', context)
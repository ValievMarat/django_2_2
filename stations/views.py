from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination.settings import BASE_DIR

list_stations = []
file_name = str(BASE_DIR) + '/data-398-2018-08-30.csv'
with open(file_name, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_stations.append(row)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_stations, 10)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page = paginator.get_page(page_number)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)

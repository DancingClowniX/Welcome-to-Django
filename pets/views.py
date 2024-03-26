from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

#def cat(request):
 #   return render(request,template_name="animals.html")

# def cats(request):
#     return HttpResponse("<h2>Коты</h2>")
#
# def dogs(request):
#     return HttpResponse("<h2>Собаки</h2>")
#
def pet(request, pet_slug):
    # будем делать обращение к БД " существует ли pet_slug ?"
    if pet_slug in ['cats', 'dogs']:
        return render(request, "animals.html")
    return render(request, template_name="NotFound.html", status=404)

def petGET(request):
    title = request.GET.get('title')# лучше примернять когда есть форма
    return HttpResponse(f"<h2>{title}</h2>")



def categories(request, categorie_id):
    return HttpResponse(f"<h2>Категории</h2><p>id:{ categorie_id }</p>")


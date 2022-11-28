from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def index(request):
    school = "Ганиев Даниль Ранилевич"
    group = "215-9"
    spec = "Программист"
    next = "Программистом"
    return render(request, "index.html", {
        "school": school, "group": group, "spec": spec, "next":next
    })

def about(request):
    name = "Ганиев Даниль Ранилевич"
    height = '184 см'
    weight = "65 кг"
    age = "16 человеческих лет"
    return render(request, "about.html", {
        "name": name, "height": height, "weight":weight, "age": age
    })

def contacts(request):
    teleg = "@turbo3009"
    number = "89370026208"
    return render(request, "contacts.html", {
        "info": {"teleg": teleg, "number": number}
    })
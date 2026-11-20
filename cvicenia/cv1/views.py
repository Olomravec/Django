from django.shortcuts import render

def cv1_index(request):
    kontext = {
            "meno": "Oliver",
    }
    return render(request, "cv1/cv1_index.html", kontext)

def cv1_obchod(request):
    produkt = [
        {"nazov": "čaj", "cena": 4 },
        {"nazov": "koláč", "cena": 6},
        {"nazov": "čokoláda", "cena": 2},
        {"nazov": "zemiaky", "cena": 7},
    ]
    max_cena = request.GET.get("max_cena", "")
    if max_cena != "":
        max_cena = float(max_cena)

        produkt = [
            p for p in produkt
            if p["cena"] <= max_cena
        ]
    return render(request, "cv1/cv1_obchod.html", {"cv1_obchod": produkt,"max_cena": max_cena,})

def cv1_body(request):
    vysledok = None
    if request.method == "POST":
        body = float(request.POST["body"])
        maximum = float(request.POST.get("maximum"))
        percenta = (body / maximum) * 100
        if percenta >= 90:
            znamka = 1
        elif percenta >= 75:
            znamka = 2
        elif percenta >= 50:
            znamka = 3
        elif percenta >= 30:
            znamka = 4
        else:
            znamka = 5
        vysledok = {
            "body": body,
            "maximum": maximum,
            "percenta": round(percenta, 1),
            "znamka": znamka
        }
    return render(request, "cv1/cv1_body.html", {"vysledok": vysledok})

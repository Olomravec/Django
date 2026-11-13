from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse("Ahoj svet")

def o_mne(request):
    kontext = {
        "meno": "Oliver",
        "vek": 17,
        "zaluby": ["bit sa a potom pozerat na ostatnych ktory sleduju","Futbalik","sufurki",],
    }
    return render(request, "ulohy/o_mne.html", kontext)
def rozvrh(request):
    hodiny = [
        {"cislo":1,"predmet":"Programovanie"},
        {"cislo":2,"predmet":"Programovanie"},
        {"cislo":3,"predmet":"Matematika"},
        {"cislo":4,"predmet":"Prax"},
        {"cislo":5,"predmet":"Prax"},
        {"cislo":6,"predmet":"ANJ"},
    ]
    return render(request, "ulohy/rozvrh.html", {"den": "Pondelok","hodiny": hodiny})
def pozdrav(request):
    meno = request.GET.get("meno","")# . get nájde a vráti hodnotu prvku z indexom (kľúčom) meno, ak ho nenájde vloží prázdny strin
    return render(request, "ulohy/pozdrav.html",  {"meno": meno})
def sucet(request):
    vysledok = None
    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        vysledok = a + b
    return render(request,"ulohy/sucet.html",{"vysledok": vysledok})
def kalkulacka(request):
    vysledok = None
    if request.method == "POST":
        a = int(request.POST["a"])
        znamienko = (request.POST["znamienko"])
        b = int(request.POST["b"])
        if znamienko == "+":
            vysledok = int(a) + int(b) 
        if znamienko == "-":
            vysledok = int(a) - int(b)
        if znamienko == "*":
            vysledok = int(a) * int(b) 
    return render(request,"ulohy/kalkulacka.html",{"vysledok": vysledok})
def obdlznik(request):
    obsah = None
    obvod = None
    if request.method == "POST":
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        obsah = round(a * b,2)
        obvod = round(2*(a+b),2)
    return render(request,"ulohy/obdlznik.html",{"obsah": obsah , "obvod": obvod})
        

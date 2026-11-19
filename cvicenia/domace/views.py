from django.shortcuts import render

def o_mne(request):
    kontext = {
        "meno": "Oliver",
        "vek": 17,
        "zaluby": ["bit sa a potom pozerat na ostatnych ktory sleduju","Futbalik","sufurki",],
    }
    return render(request, "domace/o_mne.html", kontext)

def ulohy(request):
    kontext = {
        "ulohy": "Programovanie",
    }
    return render(request, "domace/ulohy.html", kontext)

def vizitka(request):
    kontext = {
        "meno": "Oliver",
        "vek": 17,
        "trieda": "3.AT",
        "oblubeny_predmet": ["Programovanie", "matematika", "fyzika"],
        }
    return render(request, "domace/du2_vizitka.html", kontext)

def du3_teplota(request):
    ans = None
    if request.method == 'POST':
        teplota = float(request.POST["tep"])
        strana = request.POST["smer"]

        if strana == 'c>f':
            ans = str(round(teplota * 9 / 5 + 32, 1)) + " °F"
        elif strana == 'f>c':
            ans = str(round((teplota - 32) * 5 / 9, 1)) + " °C"

    return render(request, 'domace/du3_teplota.html', {'ans': ans})

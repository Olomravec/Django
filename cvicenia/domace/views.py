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

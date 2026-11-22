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

from django.shortcuts import render


def du3_teplota(request):
    vysledok = None
    jednotka = ""
    hodnota = ""
    smer = "c_na_f"

    if request.method == "POST":
        hodnota = request.POST.get("teplota", "").strip()
        smer = request.POST.get("smer", "c_na_f")
        cislo = float(hodnota.replace(",", "."))

        if smer == "c_na_f":
            vysledok = round(cislo * 9 / 5 + 32, 1)
            jednotka = "°F"
        elif smer == "f_na_c":
            vysledok = round((cislo - 32) * 5 / 9, 1)
            jednotka = "°C"

    return render(request, "domace/du3_teplota.html", {
        "vysledok": vysledok,
        "jednotka": jednotka,
        "hodnota": hodnota,
        "smer": smer,
    })
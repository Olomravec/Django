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
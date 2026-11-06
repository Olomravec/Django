from django.shortcuts import render, Httpresponse

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

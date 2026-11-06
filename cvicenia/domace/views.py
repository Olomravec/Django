from django.shortcuts import render

def o_mne(request):
    kontext = {
        "meno": "Oliver",
        "vek": 17,
        "zaluby": ["bit sa a potom pozerat na ostatnych ktory sleduju","Futbalik","sufurki",],
    }
    return render(request, "domace/o_mne.html", kontext)

def ulohy(request):
    kontexd = {
        "ulohy": "Programovanie",
    }
    return render(request, "domace/ulohy.html", kontexd)

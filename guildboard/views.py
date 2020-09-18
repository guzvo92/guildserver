from django.shortcuts import render, HttpResponse, redirect
from guildboard.services import *
#guildboard VIEWS

#solo renderiza la pagina con los registros
def guildboard(request):
    charlist = Renderguildmatrix.objects.all()
    return render(request,'guildboard.html',
        {'charlist':charlist})

#usa internet
def request(request):
    guildclockapi()
    return redirect(guildboard)


#analyzer no ocupa internet revisa los registros ya hechos
def analyzer(request):
    Renderguildmatrix.objects.all().delete()
    scopedmat_last = Scopedmatrix.objects.last()
    lastnum_scopedmat = int(scopedmat_last.mcharcounter)
    for x in range(lastnum_scopedmat):

        lvlayzer(HG2[x],x) # el analyzer es hacia una DB
    return redirect(guildboard)

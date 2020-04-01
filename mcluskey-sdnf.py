import math

def indeks_broja(b):
    return "{0:b}".format(b).count('1')

def stepen_od_dva(b):
    if b<=0: return False;
    return math.log(b, 2).is_integer()

def je_li_nova_impl(g, d):
    for i in range(len(g)): #da su iste razlike
        if d[i]-d[0]!=g[i]-g[0] or not stepen_od_dva(g[i]-d[i]): return False
    d_zadnji=d[len(d)-1]
    for i in range(len(g)): #provjera rastuceg poretka
        if g[i]<=d_zadnji: return False
    return True

def implikanta_unutar(impl, nove_implikante):
    for i in range(len(nove_implikante)):
        for k in range(len(impl)):
            if impl[k] in nove_implikante[i]:
                if k==len(impl)-1: return True
                else: continue
            else: break;
    return False;

def binarno(d, n):
    x="{0:b}".format(d)
    return ((n-len(x))*"0")+x;

def mc_cluskey(k_jedinice, b_slova):
    stare_impl=[]; nove_impl=[]; razlike=[]; proste_impl=[];
    
    for i in range(b_slova+1): stare_impl.append([])
    for i in range(len(k_jedinice)):
        stare_impl[indeks_broja(k_jedinice[i])].append([k_jedinice[i]])

    while 1:
        for i in range(len(stare_impl)-1):
            donji=stare_impl[i]; gornji=stare_impl[i+1]
            nove_impl.append([])
            razlike.append([])
            for j in range(len(donji)):
                for k in range(len(gornji)):
                    if je_li_nova_impl(gornji[k],donji[j]):
                        nove_impl[i].append(donji[j]+gornji[k])
        for i in range(len(nove_impl)):
            for j in range(i+2):
                for k in range(len(stare_impl[j])):
                    if stare_impl[j][k]!=None and implikanta_unutar(stare_impl[j][k], nove_impl[i]): #PAZI UNUTAR
                        stare_impl[j][k]=None #Štrihiranje

        for i in range(len(stare_impl)):
            for j in range(len(stare_impl[i])):
                if stare_impl[i][j]!=None: proste_impl.append(stare_impl[i][j])

        if len(nove_impl)==0: break;
        stare_impl=nove_impl
        nove_impl=[]
        
    vrati=""
    for i in range(len(proste_impl)):
        b=binarno(proste_impl[i][0], b_slova)
        slovo=0; za_dodati=[]
        for x in b:
            if x=='1': za_dodati.append(chr(ord("A")+slovo))
            else: za_dodati.append(chr(ord("A")+slovo)+"'")
            slovo+=1
        for j in range(len(proste_impl[i])):
            if stepen_od_dva(proste_impl[i][j]-proste_impl[i][0]):
                za_dodati[-((int)(math.log(proste_impl[i][j]-proste_impl[i][0], 2))+1)]=""
        vrati=vrati+"".join(za_dodati)
        if i<len(proste_impl)-1: vrati=vrati+" v "

    return vrati



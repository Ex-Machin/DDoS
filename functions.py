from math import pi

def licz_kolo(r):
    return pi * r[0] ** 2

def licz_kwadrat(bok):
    return bok[0] ** 2

def licz_prostokat(boki):
    return boki[0] * boki[1]

def licz_trapezu(boki):
    return ((boki[0] + boki[1]) * boki[2]) / 2


figury = {
    'kwadrat': licz_kwadrat,
    'prostokąt': licz_prostokat,
    'trapez': licz_trapezu,
    'koło': licz_kolo
}
    
def licz_pola_figur(figura, *boki):
    return figury[figura](boki)


    


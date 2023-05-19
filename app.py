from functions import licz_pola_figur 

wyniki = {
    'kwadrat': [],
    'prostokąt': [],
    'trapez': [],
    'koło': []
}

def wyświetł_dane(figura, *boki):
    pole= licz_pola_figur(figura, boki)
    print(f"Pole {figura} wynosi: {pole}")
    wyniki[figura].append(pole)

start = True

while start:
    pytanie = input('Co chcesz zrobić? \n1. Licz pole kwadratu \n2. Licz pole prostokąta \n3. Licz pole trapezu \n4. Licze pole koła \n5. Zakońc program \nWpisz numer: ')

    if pytanie == '1':
        a = float(input("Podaj długość boku kwadratu: "))
        if a > 0:
            wyświetł_dane('kwadrat', a)

    elif pytanie == "2":
        a = float(input("Podaj dłigość pierwszego boku"))
        b = float(input("Podaj dłigość drugiego boku"))

        if a > 0 and b > 0:
            wyświetł_dane('prostokąt', a, b)

    elif pytanie == "3":
        a = float(input("Podaj dłigość pierwszej podstawy: "))
        b = float(input("Podaj dłigość drugiego podstawy: "))
        h = float(input("Podaj wysokość: "))

        if a > 0 and b > 0 and h > 0:
            wyświetł_dane('trapez', a, b, h)

    if pytanie == '4':
        r = int(input('Podaj promień: '))
        if r < 0:
            pole_trapezu = licz_pola_figur('kolo', r)

    if pytanie == '5':
        start = False

with open('results.txt', 'w', encoding='utf-8') as file:
    file.write('Wyniki z programu: \n')
    for klucz in wyniki.keys():
        for pole in wyniki[klucz]:
            file.write(f"Pole {klucz}: {pole} \n")




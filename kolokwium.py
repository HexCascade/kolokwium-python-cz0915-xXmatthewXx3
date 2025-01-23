# Numer indeksu: 281146
# Grupa: 2 

# Miejsce na Twój kod:

import math

def pobierz_promien_w_mm(lista_promieni):
    '''Funkcja pobiera od użytkownika wartości promienia koła w mm i dodaje je do listy lista_promieni. 
    Funkcja kończy działanie po wpisaniu 'koniec' i zwraca listę promieni.'''

    while True:
        try:
            promien = input("Podaj promień koła w mm (lub wpisz 'koniec' aby zakończyć): ")
            if promien.lower() == 'koniec':
                break
            promien = float(promien)
            if promien <= 0:
                raise ValueError
            lista_promieni.append(promien)
        except ValueError:
            print('Niepoprawne dane, podaj dodatnią wartość promienia w mm lub zakończ wprowadzanie wpisując polecenie "koniec"')
    return lista_promieni


def max_pole_kola(prom):
    '''Funkcja przyjmuje LISTĘ promieni jako argument -> (prom) i zwraca pole koła dla największego promienia w liście.'''
    if not prom:
        return 0
    max_prom = max(prom)
    return math.pi * max_prom ** 2



if __name__ == '__main__':
    war_promieni = [94.5, 22.4, 3.1415]
    pobierz_promien_w_mm(war_promieni)
    # Uzupełnij program o brakujące elementy tak aby działał zgodnie z poleceniem

    # Obliczamy pole koła dla największego promienia w liście
    max_pole = max_pole_kola(war_promieni)

    # Wyświetlamy listę promieni
    print(f'Lista promieni: {war_promieni}')
    # Wyświetlamy pole koła dla największego promienia w liście
    print(f'Pole dla największego promienia to: {round(max_pole, 3)} mm^2.')
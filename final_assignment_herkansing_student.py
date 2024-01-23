#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment: herkansing

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = ""
klas = ""
studentnummer = -1

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme voor een lijst `lst` van natuurlijke getallen:
    1. Bepaal het grootste getal k in de lijst.
    2. Maak een nieuwe lijst van lengte k+1, waarbij elk element in deze tweede lijst begint met de waarde 0.
    3. Tel het aantal voorkomens van elk getal in de originele lijst en sla deze frequentie op in de tweede lijst.
    4. Maak een derde, lege lijst
    5. Voeg elke index van de tweede lijst zo vaak toe aan de derde lijst als zij geteld is in stap 3.
    6. Retourneer de derde lijst: zij is een gesorteerde versie van de originele lijst.

    1a. Handmatig toepassen van stap 3.
        Gegeven is de lijst lst = [ 1, 0, 4, 1 ]. Geef de waardes die de *tweede* lijst aanneemt bij
        álle tussenstappen van stap 3. hierboven.
"""
#       TODO: [geef hier je antwoord]
"""

    1b. Handmatig toepassen van stap 5.
        Geef nu de waardes die de *derde* lijst aanneemt bij álle tussenstappen van stap 5. hierboven.
"""
#       TODO: [geef hier je antwoord]
"""

    1c. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie hieronder genaamd my_sort(lst).

    1d. Best en worst case
        -   Stel, je hebt de lijst met waarden lst = [ 1, 0, 4, 1 ], zoals hierboven. Door hoeveel elementen
            moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
#           TODO: [geef hier je antwoord]
"""

        -   Stel, je hebt de lijst met waarden lst = [ 7, 5, 9 ]. Door hoeveel elementen
            moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
#           TODO: [geef hier je antwoord]
"""

        -   Stel, je hebt de lijst met waarden lst = [ 42, 0 ]. Door hoeveel elementen
            moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
#           TODO: [geef hier je antwoord]
"""

        -   Stel, je hebt de lijst met n waarden (dus len(lst) = n), met daarin als maximum waarde k. Door
            hoeveel elementen moet je dan stappen in het *hele* algoritme om tot een gesorteerde lijst te komen?
"""
#           TODO: [geef hier je antwoord]
"""

        -   Concluderend: wanneer werkt dit algoritme efficiënt? En wanneer niet?
"""
#           TODO: [geef hier je antwoord]
"""


"""


def my_sort(lst):
    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode hierboven.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    sorted_lst = []  # stap 4.
    return sorted_lst  # stap 6.


def max_linear_recursive(lst):
    """
    Vind het grootste element in de gegeven lijst door middel van recursief lineair zoeken.

    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met gehele getallen.

    Returns:
        int: Het grootste element dat in de lijst voorkomt.
    """


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_max_linear_recursive():
    for _ in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        actual_max = max(lst_test)
        lst_copy = lst_test.copy()

        found_max = max_linear_recursive(lst_test)
        assert found_max == actual_max, \
            f"Fout: max_linear_recursive({lst_test}) geeft {found_max} in plaats van {actual_max}"
        assert lst_copy == lst_test, "Fout: binary_search_recursive(lst, target) verandert de inhoud van lijst lst"


def test_my_sort():
    lst_test = [random.choice(range(10)) for _ in range(10)]
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"



def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_max_linear_recursive()
        print("Je functie test_max_linear_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()
    
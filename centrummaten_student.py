#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: zoeken

(c) 2023 Hogeschool Utrecht,
Peter van den Berg (petervandenberg@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def mediaan(lst):
    """
    Bepaal de mediaan van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De mediaan van de gegeven getallen.
    """

def gemiddelde(lst):
    """
    Bepaal het gemiddelde van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het gemiddelde van de gegeven getallen.
    """

def freq(lst):
    """
    Bepaal de frequenties van alle getallen in een lijst.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        dict: Een dictionary met als 'key' de waardes die voorkomen in de lijst
            en als 'value' het aantal voorkomens (de frequentie) van die waarde.

    Examples:
        >> freq([0, 0, 4, 7, 7])
        {0: 2, 4: 1, 7: 2}

        >> freq([1, 1, 2, 3, 2, 1])
        {1: 3, 2: 2, 3: 1}
    """
    freqs = dict()
    return freqs

def modi(lst):
    """
    Bepaal alle modi van een lijst getallen.

    Hint: maak gebruik van `freq()`.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        list: Een gesorteerde lijst van de modi van de gegeven getallen.

    Examples:
        >> modi([0, 0, 4, 7, 7])
        [0, 7]

        >> modi([1, 1, 2, 3, 2, 1])
        [1]
    """
    modi = []
    return sorted(modi)


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import os
import sys

def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_mediaan():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 4, 6, 4, 2],), 3.5),
        (([1, 3, 4, 6, 2, 4, 2],), 3.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.5)
    ]

    for case in testcases:
        __my_assert_args(mediaan, case[0], case[1])


def test_mediaan_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(mediaan, (lst_test,), statistics.median(lst_test), False)


def test_gemiddelde():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 3.0)
    ]

    for case in testcases:
        __my_assert_args(gemiddelde, case[0], case[1])


def test_gemiddelde_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(gemiddelde, (lst_test,), statistics.mean(lst_test), False)


def test_freq():
    testcases = [
        (([4, 2, 5, 8, 6],), {2: 1, 4: 1, 5: 1, 6: 1, 8: 1}),
        (([1, 3, 4, 6, 4, 2],), {1: 1, 2: 1, 3: 1, 4: 2, 6: 1}),
        (([1, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        (([1, 4, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1})
    ]

    for case in testcases:
        __my_assert_args(freq, case[0], case[1])


def test_modi():
    testcases = [
        (([4, 2, 5, 8, 6],), [2, 4, 5, 6, 8]),
        (([1, 3, 4, 6, 4, 2],), [4]),
        (([1, 3, 4, 6, 2, 4, 2],), [2, 4]),
        (([1, 3, 2, 4, 6, 2, 4, 2],), [2])
    ]

    for case in testcases:
        __my_assert_args(modi, case[0], case[1])

def test_modi_simulated():
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
        import random
        import statistics
        for lst_size in range(1, 11):
            lst_test = [random.choice(range(5)) for _ in range(lst_size)]
            __my_assert_args(modi, (lst_test,), sorted(statistics.multimode(lst_test)))


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_mediaan()
        test_mediaan_simulated()
        print("Je functie mediaan(lst) werkt goed!")

        test_gemiddelde()
        test_gemiddelde_simulated()
        print("Je functie gemiddelde(lst) werkt goed!")

        test_freq()
        print("Je functie freq(lst) werkt goed!")

        test_modi()
        test_modi_simulated()
        print("Je functie modi(lst) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

        def hist(freqs):
            v_min = min(freqs.keys())
            v_max = max(freqs.keys())

            histo = str()
            for i in range(v_min, v_max + 1):
                histo += "{:5d} ".format(i)
                if i in freqs.keys():
                    histo += "█" * freqs[i]
                histo += '\n'

            return histo

        print("\x1b[0m")
        s = input("Geef een reeks van gehele getallen (gescheiden door een spatie): ")
        userlst = [int(c) for c in s.split()]

        print("\nHet gemiddelde is {:.2f}".format(gemiddelde(userlst)))
        print("De modi zijn {}".format(modi(userlst)))
        print("De mediaan is {:.2f}".format(mediaan(userlst)))

        print("\nHistogram (gekanteld):\n\n" + hist(freq(userlst)))

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
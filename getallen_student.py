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

def floor(real):
    """
    Bepaal het grootste gehele getal (int), dat kleiner dan of gelijk is aan het gegeven reeel getal (float).

    Args:
        real (float): Een reeel getal.

    Returns:
        int: Het grootste gehele getal (int), dat kleiner dan of gelijk is aan het gegeven reeel getal.
    """


def ceil(real):
    """
    Bepaal het kleinste gehele getal (int), groter dan of gelijk aan het gegeven reeele getal (float).

    Args:
        real (float): Een reeel getal.

    Returns:
        int: Het kleinste gehele getal (int), groter dan of gelijk aan het gegeven reeele getal (float).
    """
    

def round(real):
    """
    Bepaal het gehele getal (int) dat het dichtst bij het gegeven reeele getal (float) zit.

    Args:
        real (float): Een reeel getal.

    Returns:
        int: Het gehele getal (int) dat het dichtst bij het gegeven reeele getal (float) zit.
    """


def is_even(n):
    """
    Bepaal of een geheel getal even is.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als even, False als oneven.
    """

def is_uneven(n):
    """
    Bepaal of een geheel getal oneven is.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als oneven, False als even.
    """

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


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


def test_floor():
    testcases = [
        ((1.05,), 1),
        ((1.95,), 1),
        ((-1.05,), -2),
        ((-1.95,), -2),
        ((0.05,), 0),
        ((-0.05,), -1),
        ((0.0, ), 0),
        ((1.0, ), 1),
        ((-1.0, ), -1)
    ]

    for case in testcases:
        __my_assert_args(floor, case[0], case[1])


def test_ceil():
    testcases = [
        ((1.05,), 2),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -1),
        ((0.05,), 1),
        ((-0.05,), 0),
        ((0.0, ), 0),
        ((1.0, ), 1),
        ((-1.0, ), -1)
    ]

    for case in testcases:
        __my_assert_args(ceil, case[0], case[1])

def test_round():
    testcases = [
        ((1.05,), 1),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -2),
        ((0.05,), 0),
        ((-0.05,), 0),
        ((0.0, ), 0),
        ((1.0, ), 1),
        ((-1.0, ), -1)
    ]

    for case in testcases:
        __my_assert_args(round, case[0], case[1])

def test_is_even():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), False),
        ((4,), True),
        ((-1,), False),
        ((-2,), True)
    ]

    for case in testcases:
        __my_assert_args(is_even, case[0], case[1])

def test_is_uneven():
    testcases = [
        ((1,), True),
        ((2,), False),
        ((3,), True),
        ((4,), False),
        ((-1,), True),
        ((-2,), False)
    ]

    for case in testcases:
        __my_assert_args(is_uneven, case[0], case[1])

if __name__ == '__main__':
    try:
        print("\x1b[32m")

        test_floor()
        print("Je functie floor() werkt goed!")
        test_ceil()
        print("Je functie ceil() werkt goed!")
        test_round()
        print("Je functie round() werkt goed!")
        test_is_even()
        print("Je functie is_even() werkt goed!")
        test_is_uneven()
        print("Je functie is_oneven() werkt goed!")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur
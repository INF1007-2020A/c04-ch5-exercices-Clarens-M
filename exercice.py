#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number >= 0:
        nombre = number
    else:
        nombre = -1 * number
    return nombre


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = []
    i = 0
    for c in prefixes:
        liste.append(c + suffixe)
    return liste

def is_prime(number):
    for i in range(2, number//2, 1):
        if number % i == 0:
            return False
    return True

def prime_integer_summation() -> int:
#    compteur = 0
#    somme = 0
#    départ = 1
#    while compteur <= 100:
#        départ += 1
#        if départ == 2:
#            somme = 2
#        else:
#            for i in range(2, départ, 1):
#                reste = départ % i
#                if reste == 0:
#                    break
#                elif i == départ:
#                    somme += i
#                    compteur += 1
#                else:
#                    continue
    prime = [2, 3, 5]
    nombre = 6
    while len(prime) < 100:
        if is_prime(nombre):
            prime.append(nombre)
        nombre += 1
        
            
    return sum(prime)


def factorial(number: int) -> int:
    facto = 1
    for i in range(number, 0, -1):
        facto = facto * i
    return facto


def use_continue() -> None:
    for i in range(1, 11, 1):
        if i == 5:
            continue
        else:
            print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acc = []
    for i in range(1, len(groups)):
        if 25 in groups[i]:
            acc.append(True)
        else:
            if (len(groups[i]) > 10) or (len(groups[i]) <= 3):
                acc.append(False)
            elif max(groups[i]) < 18:
                acc.append(False)
            elif (max(groups[i]) > 70) and (50 in groups[i]):
                acc.append(False)
            else:
                acc.append(True)
                    
    return acc


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

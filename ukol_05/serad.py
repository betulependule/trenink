#! /usr/bin/env python3

cisla = [8, 10, 5, 1, 6, 100]


def serad(cisla):
    a = sorted(cisla)
    b = list(reversed(a))
    print("Poskladany list je: {}".format(b))


serad(cisla)

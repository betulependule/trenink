#! /usr/bin/env python3

text = """Jednoho krasneho dne se Adam probral a dal si salek kavy.
    Byl to vskutku krasny den a Adam se rozhodl pozorovat sve sluhy,
    jak na zahrade pletou cervene klobouky. Tyto klobouky jsou tradicni
    odev Jeho Velicentsta.""".replace("\n", " ").replace("\t", "")
slovo_1 = "klobouky"
slovo_2 = "fedory"


def nahrad(text, slovo_1, slovo_2):
    a = list(text)
    novy = []
    b = []
    for x in a:
        c = "".join(novy)
        if c == slovo_1 and x == " ":
            c = slovo_2 + " "
            novy = list(c)
            novy = "".join(novy)
            b.append(novy)
            novy = []
        elif c == slovo_1 and x == ".":
            c = slovo_2 + "."
            novy = list(c)
            novy = "".join(novy)
            b.append(novy)
            novy = []
        elif x == " " or x == ".":
            novy.append(x)
            novy = "".join(novy)
            b.append(novy)
            novy = []
        else:
            novy.append(x)
    print("".join(b))


nahrad(text, slovo_1, slovo_2)

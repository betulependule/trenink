#! /usr/bin/env python3

vety = """Vietnamci jsou cool lidi. Portugalci radi pletou
    kasmirove bluzy. Japonci masturbuji pri mesicku a
    Cesi se radi divaji.""".replace("\n", " ").replace("\t", "")


def rozdel_vety(vety):
    a = list(vety)
    b = []
    nova_veta = []
    for x in a:
        if nova_veta == [] and x == " ":
            pass
        elif x == ".":
            nova_veta.append(x)
            nova_veta = "".join(nova_veta)
            b.append(nova_veta)
            nova_veta = []
        else:
            nova_veta.append(x)
    print(b)


rozdel_vety(vety)

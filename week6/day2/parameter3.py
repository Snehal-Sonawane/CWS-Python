def marks(phy: int, chem: int, com: int, sci: int):
    print(phy + chem + com + sci)


marks(56, 67, 89, 90)


def printDictionary(x: dict):
    for k, v in x.items():
        print(f"{k}->{v}")


printDictionary({"Anirudh": 555, "Akul": 99, "Manish": 99})

szam1 = input("Írj be egy számot: ")

if isinstance(szam1, int):
    print("Ez egy szám!")
    print(type(szam1))
else:
    raise ValueError("Nem számot adtál meg!")
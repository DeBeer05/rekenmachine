## simpelste variant van een rekenmachine. vraag 2 getallen waarna deze allebij sowieso worden opgeteld.
# a = input("geef getal nummer 1 op: ")
# b = input("geef getal nummer 2 op: ")

# c = int(a) + int(b)
# print("Het resultaat is:", c)

## iets moeilijkere variant van een rekenmachine. vraag 2 getallen en een operator waarna deze de bewerking uitvoert.
a = input("geef getal nummer 1 op: ")
b = input("geef getal nummer 2 op: ")
vo = input("geef op of je plus of min wilt: ")

match vo:
    case "plus":
        c = int(a) + int(b)
        print("Het resultaat is:", c)
    case "min":
        c = int(a) - int(b)
        print("Het resultaat is:", c)
    case _:
        print("Ongeldige operator, gebruik 'plus' of 'min'.")


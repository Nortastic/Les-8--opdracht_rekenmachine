def toon_menu():
    print("\nWelkom bij de rekenmachine!")
    print("1. Optellen (+)")
    print("2. Aftrekken (-)")
    print("3. Vermenigvuldigen (*)")
    print("4. Delen (/)")
    print("5. Stoppen")


def vraag_getallen():
    try:
        getal_1 = float(input("Voer het eerste getal in: "))
        getal_2 = float(input("Voer het tweede getal in: "))
        return getal_1, getal_2
    except ValueError:
        print("Ongeldige invoer. Gebruik alleen getallen.")
        return None


def bereken(keuze, getal_1, getal_2):
    if keuze == "1":
        return getal_1 + getal_2
    elif keuze == "2":
        return getal_1 - getal_2
    elif keuze == "3":
        return getal_1 * getal_2
    elif keuze == "4":
        try:
            return getal_1 / getal_2
        except ZeroDivisionError:
            print("Delen door nul is niet toegestaan.")
            return None
    else:
        print("Ongeldige keuze.")
        return None


def main():
    Keuze_gebruiker = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/"
    }

    while True:
        toon_menu()
        keuze = input("Selecteer een bewerking naar keuze (1-5): ")

        if keuze == "5":
            print("Programma afgesloten.")
            break

        getallen = vraag_getallen()
        if getallen is None:
            continue

        resultaat = bereken(keuze, getallen[0], getallen[1])
        if resultaat is not None:
            teken = Keuze_gebruiker[keuze]
            print(f"Resultaat: {getallen[0]} {teken} {getallen[1]} = {resultaat}")

        if not vraag_opnieuw():
            break

def vraag_opnieuw():
    antwoord = input("\nWil je nog een berekening maken? (ja/nee): ").lower()

    if antwoord == "ja":
        return True
    elif antwoord == "nee":
        print("Bedankt voor het gebruiken van dit programma en tot ziens!")
        return False
    else:
        print("Ongeldige keuze, programma wordt afgesloten.")
        return False



main()

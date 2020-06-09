#! /usr/bin/env python


class Prajituri():
    """
    Clasa generica pentru definirea unei prajituri

    list_p -> lista de obiecte ale clasei
    """

    list_p = list()

    def __init__(self, nume: str, pret: int, gramaj: int):
        """
        Class constructor

        Args: nume: str, numele prajiturii
              pret: int, pretul prajiturii
              gramaj: int, gramajul prajiturii

        Returns: None
        """

        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        Prajituri.list_p.append(self)


    def print_by_gramaj():
        """
        Sortare si afisare a prajiturilor dupa gramaj
        """

        print("Sortat dupa gramaj:")
        list_sorted = sorted(Prajituri.list_p, key=lambda p: p.gramaj, reverse=True)
        for elem in list_sorted:
            print(f"gramaj: {elem.gramaj}, nume: {elem.nume}, pret: {elem.pret}")


    def print_by_pret():
        """
        Sortare si afisare a prajiturilor dupa pret
        """

        print("Sortat dupa pret:")
        list_sorted = sorted(Prajituri.list_p, key=lambda p: p.pret, reverse=True)
        for elem in list_sorted:
            print(f"gramaj: {elem.gramaj}, nume: {elem.nume}, pret: {elem.pret}")


class Tort(Prajituri):
    """
    Clasa ce mosteneste Prajituri, pentru definirea unui tort
    """

    def __init__(self, nume: str, pret: int, gramaj: int):
        """
        Class constructor

        Args: nume: str, numele tortului
              pret: int, pretul tortului
              gramaj: int, gramajul tortului

        Returns: None
        """

        Prajituri.__init__(self, nume, pret, gramaj)
        self.etajat = False
        self.glazura = "ciocolata"


    def set_attrs(self, etajat: bool, glazura: str):
        """
        Modificarea atributelor specifice tortului

        Args: etajat: bool, daca tortul este etajat sau nu
              glazura: str, tipul glazurii tortului

        Returns: None
        """

        self.etajat = etajat
        self.glazura = glazura


    def get_attrs(self):
        """
        Returnarea atributelor specifice tortului

        Args: None

        Returns: etajat: bool, daca tortul este etajat sau nu
                 glazura: str, tipul glazurii tortului
        """
        return self.etajat, self.glazura


class Fursec(Prajituri):
    """
    Clasa ce mosteneste Prajituri, pentru definirea unui fursec
    """

    def __init__(self, nume: str, pret: int, gramaj: int):
        """
        Class constructor

        Args: nume: str, numele fursecului
              pret: int, pretul fursecului
              gramaj: int, gramajul fursecului

        Returns: None
        """

        Prajituri.__init__(self, nume, pret, gramaj)


def test_classes():
    bezea = Tort('bezea', 15, 100)
    trilogie = Tort('trilogie', 10, 150)
    mousse = Tort('mousse', 12, 200)
    chocolate_chip = Fursec('chocolate chip', 2, 125)
    peanut_butter = Fursec('peanut butter', 4, 100)
    macarons = Fursec('macarons', 5, 150)
    Prajituri.print_by_gramaj()
    Prajituri.print_by_pret()
    bezea.set_attrs(True, "cacao")
    print(f"etajat: {bezea.get_attrs()[0]}, glazura: {bezea.get_attrs()[1]}")
    mousse.set_attrs(True, "caramel")
    print(f"etajat: {mousse.get_attrs()[0]}, glazura: {mousse.get_attrs()[1]}")


def main():
    test_classes()


if __name__ == "__main__":
    main()    

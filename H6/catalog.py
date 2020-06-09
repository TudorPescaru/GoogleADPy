#! /usr/bin/env python


class Catalog():
    """
    Clasa ce defineste un catalog pentru un student cu materii si absente
    """

    def __init__(self, nume, prenume):
        """
        Class constructor

        Args: nume: str, numele de familie al elevului
              prenume: str, prenumele elevului

        Returns: None
        """

        self.nume = nume
        self.prenume = prenume
        self.materii = dict()
        self.absente = 0


    def add_absenta(self):
        """
        Adauga o absenta la numarul de absente ale elevului

        Args: None

        Returns: None
        """

        self.absente += 1


    def remove_absente(self, scutire: int):
        """
        Elimina un numar dat de absente din totalul de absente ale elevului

        Args: scutire: int, numarul de absente ce trebuie eliminate

        Returns: None
        """

        if isinstance(scutire, int) is False:
            return
        self.absente -= scutire
        if self.absente < 0:
            self.absente = 0


    def __str__(self):
        """
        Print returneaza numarul de absente ale elevului
        """

        return f"Elevul {self.nume} {self.prenume} are {self.absente} absente"


class Extensie1(Catalog):
    """
    Extensie a clasei de catalog ce se ocupa cu materiile elevului
    """

    def __init__(self, nume, prenume):
        """
        Class constructor

        Args: nume: str, numele de familie al elevului
              prenume: str, prenumele elevului

        Returns: None
        """

        Catalog.__init__(self, nume, prenume)


    def add_materie(self, materie: str, note: list):
        """
        Adauga o materie si notele la materia respectiva

        Args: materie: string, numele materiei
              note: list, lista de note la materia data

        Returns: None
        """

        self.materii[materie] = note.copy()


    def get_materii(self):
        """
        Afiseaza materiile studentului

        Args: None

        Returns: None
        """

        print(f"Materiile lui {self.prenume} {self.nume} sunt: {', '.join(str(m) for m in self.materii.keys())}")


    def get_medii(self):
        """
        Afiseaza media la fiecare materie

        Args: None

        Returns: None
        """

        for m in self.materii.keys():
            note = [n for n in self.materii[m] if isinstance(n, int)]
            print(f"{self.prenume} {self.nume} are media {sum(note) / len(note)} la {m}")


def test_classes():
    student1 = Extensie1("Roata", "Ion")
    for i in range(3):
        student1.add_absenta()
    student1.remove_absente(2)
    student2 = Extensie1("Cerc", "George")
    for i in range(4):
        student2.add_absenta()
    student2.remove_absente(2)
    print(student1)
    print(student2)
    student1.add_materie("Python", [6, 8, 9])
    student2.add_materie("Python", [7, 9, 10])
    student2.add_materie("Matematica", [5, 7, 6])
    student1.add_materie("Romana", [8, 9, 10])
    student1.get_materii()
    student2.get_materii()
    student1.get_medii()
    student2.get_medii()


def main():
    test_classes()


if __name__ == "__main__":
    main()

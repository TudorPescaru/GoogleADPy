#!/usr/bin/env python


def leapyear(year):
    if (year %4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def main():

    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]

    counties = ["Alba",
                "Arad",
                "Arges",
                "Bacau",
                "Bihor",
                "Bistrita-Nasaud",
                "Botosani",
                "Brasov",
                "Braila",
                "Buzau",
                "Caras-Severin",
                "Cluj",
                "Constanta",
                "Covasna",
                "Dambovita",
                "Dolj",
                "Galati",
                "Gorj",
                "Hargita",
                "Hunedoara",
                "Ialomita",
                "Iasi",
                "Ilfov",
                "Maramures",
                "Mehedinti",
                "Mures",
                "Neamt",
                "Olt",
                "Prahova",
                "Satu Mare",
                "Salaj",
                "Sibiu",
                "Suceava",
                "Teleorman",
                "Timis",
                "Tulcea",
                "Vaslui",
                "Valcea",
                "Vrancea",
                "Bucuresti",
                "Bucuresti S.1",
                "Bucuresti S.2",
                "Bucuresti S.3",
                "Bucuresti S.4",
                "Bucuresti S.5",
                "Bucuresti S.6",
                "",
                "",
                "",
                "",
                "Calarasi",
                "Giurgiu"]

    checkcode = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

    cnp = input("Enter a CNP: ")

    if len(cnp) != 13:
        print("Invalid input - wrong length")
        return

    if cnp.isdigit() is False:
        print("Invalid input - nonnumerical characters")
        return
    
    g = int(cnp[0])
    if g not in range(1, 10):
        print("Invalid input - wrong gender id")
        return
    elif g in range(1, 7):
        gender = "male" if g % 2 != 0 else "female"
        print("Romanian citizen - %s" %(gender))
    elif g in range(7, 9):
        gender = "male" if g % 2 != 0 else "female"
        print("Foreign citizen - Romanian resident - %s" %(gender))
    else:
        print("Foreign citizen")

    year = int(cnp[1:3])
    if g in range(1, 3) or g in range(7, 10):
        year = year + 1900
    elif g in range(3, 5):
        year = year + 1800
    else:
        year = year + 2000

    month = int(cnp[3:5])
    if month == 0 or month > 12:
        print("Invalid input - inexistent month number")
        return
    
    day = int(cnp[5:7])
    if day == 0:
        print("Invalid input - inexistent day number")
        return
    elif month in [1, 3, 5, 7, 9, 11] and day > 31:
        print("Invalid input - inexistent day number")
        return
    elif month in [4, 6, 8, 10, 12] and day > 30:
        print("Invalid input - inexistent day number")
        return
    elif month == 2 and leapyear(year) is True and day > 29:
        print("Invalid input - inexistent day number")
        return
    elif month == 2 and leapyear(year) is False and day > 28:
        print("Invalid input - inexistent day number")
        return
   
    if day % 10 == 1:
        dayformatted = str(day) + "st"
    elif day % 10 == 2:
        dayformatted = str(day) + "nd"
    elif day % 10 == 3:
        dayformatted = str(day) + "rd"
    else:
        dayformatted = str(day) + "th"

    template = "Date of birth: {0} of {1}, {2}"
    dob = template.format(dayformatted, months[month - 1], year)
    print(dob)

    county = int(cnp[7:9])
    if county == 0 or county > 52 or counties[county - 1] == "":
        print("Invalid input - wrong county code")
        return
    
    print("Birth-county: %s" %(counties[county - 1]))

    n = int(cnp[9:12])
    if n == 0:
        print("Invalid input - wrong unique code")
        return

    c = int(cnp[12])
    check = 0
    for i, digit in enumerate(cnp):
        if i == 12:
            break
        check += int(digit) * checkcode[i]
    check %= 11
    check = 1 if check == 10 else check
    if check != c:
        print("Invalid input - wrong check-digit")
        return


if __name__ == "__main__":
    main()


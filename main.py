import sys

def one_symbol(number):
    if number == "0":
        return "ноль"
    if number == "1":
        return "один"
    if number == "2":
        return "два"
    if number == "3":
        return "три"
    if number == "4":
        return "четыре"
    if number == "5":
        return "пять"
    if number == "6":
        return "шесть"
    if number == "7":
        return "семь"
    if number == "8":
        return "восемь"
    if number == "9":
        return "девять"

def two_symbol(number):
    if number[0] == "1":
        if number[1] == "1":
            return "одиннадцать"
        if number[1] == "2":
            return "двенадцать"
        if number[1] == "3":
            return "тринадцать"
        if number[1] == "4":
            return "четырнадцать"
        if number[1] == "5":
            return "пятнадцать"
        if number[1] == "6":
            return "шестнадцать"
        if number[1] == "7":
            return "семнадцать"
        if number[1] == "8":
            return "восемнадцать"
        if number[1] == "9":
            return "девятнадцать"
        if number[1] == "0":
            return "десять"

    if number[0] == "2":
        if number[1] == "0":
            return "двадцать"
        else:
            return "двадцать" + ' ' + one_symbol(number[1])
    if number[0] == "3":
        if number[1] == "0":
            return "тридцать"
        else:
            return "тридцать" + ' ' + one_symbol(number[1])
    if number[0] == "4":
        if number[1] == "0":
            return "сорок"
        else:
            return "сорок" + ' ' + one_symbol(number[1])
    if number[0] == "5":
        if number[1] == "0":
            return "пятьдесят"
        else:
            return "пятьдесят" + ' ' + one_symbol(number[1])
    if number[0] == "6":
        if number[1] == "0":
            return "шестьдесят"
        else:
            return "шестьдесят" + ' ' + one_symbol(number[1])
    if number[0] == "7":
        if number[1] == "0":
            return "семьдесят"
        else:
            return "семьдесят" + ' ' + one_symbol(number[1])
    if number[0] == "8":
        if number[1] == "0":
            return "восемьдесят"
        else:
            return "восемьдесят" + ' ' + one_symbol(number[1])
    if number[0] == "9":
        if number[1] == "0":
            return "девяносто"
        else:
            return "девяносто" + ' ' + one_symbol(number[1])

def three_symbol(number):
    if number[0] == "1":
        if ((number[1] == "0") and (number[2] == "0")):
            return "сто"
        else:
            if number[1] == "0":
                return "сто " + one_symbol(number[2])
            else: 
                return "сто " + two_symbol(number[1] + number[2])
    if number[0] == "2":
        if ((number[1] == "0") and (number[2] == "0")):
            return "двести"
        else:
            if number[1] == "0":
                return "двести " + one_symbol(number[2])
            else: 
                return "двести " + two_symbol(number[1] + number[2])
    if number[0] == "3":
        if ((number[1] == "0") and (number[2] == "0")):
            return "триста"
        else:
            if number[1] == "0":
                return "триста " + one_symbol(number[2])
            else: 
                return "триста " + two_symbol(number[1] + number[2])
    if number[0] == "4":
        if ((number[1] == "0") and (number[2] == "0")):
            return "четыреста"
        else:
            if number[1] == "0":
                return "четыреста " + one_symbol(number[2])
            else: 
                return "четыреста " + two_symbol(number[1] + number[2])
    if number[0] == "5":
        if ((number[1] == "0") and (number[2] == "0")):
            return "пятьсот"
        else:
            if number[1] == "0":
                return "пятьсот " + one_symbol(number[2])
            else: 
                return "пятьсот " + two_symbol(number[1] + number[2])
    if number[0] == "6":
        if ((number[1] == "0") and (number[2] == "0")):
            return "шестьсот"
        else:
            if number[1] == "0":
                return "шестьсот " + one_symbol(number[2])
            else: 
                return "шестьсот " + two_symbol(number[1] + number[2])
    if number[0] == "7":
        if ((number[1] == "0") and (number[2] == "0")):
            return "семьсот"
        else:
            if number[1] == "0":
                return "семьсот " + one_symbol(number[2])
            else: 
                return "семьсот " + two_symbol(number[1] + number[2])
    if number[0] == "8":
        if ((number[1] == "0") and (number[2] == "0")):
            return "восемьсот"
        else:
            if number[1] == "0":
                return "восемьсот " + one_symbol(number[2])
            else: 
                return "восемьсот " + two_symbol(number[1] + number[2])
    if number[0] == "9":
        if ((number[1] == "0") and (number[2] == "0")):
            return "девятьсот"
        else:
            if number[1] == "0":
                return "девятьсот " + one_symbol(number[2])
            else: 
                return "девятьсот " + two_symbol(number[1] + number[2])

def convert_to_int(text):
    try:
        result_int = int(text)
    except (TypeError, ValueError) as identifier:
        print("Не является числом - СОСИ!!!: " + str(identifier))
        quit()

main_number = sys.argv[1]

# for main_number in range(1,1000):
    # main_number = "10"
main_number = str(main_number)
main_result = ""
convert_to_int(main_number)
if (main_number[0]) == "0":
    print ("иди на хуй, сказали!")
    quit()
if len(main_number) == 1:
    main_result = one_symbol(main_number)
if len(main_number) == 2:
    main_result = two_symbol(main_number)
if len(main_number) == 3:
    main_result = three_symbol(main_number)
if len(main_number) > 3:
    print("тупая, не умею")
    quit()
print(main_result)
while True:
    from random import randint
    lose = randint(1,3)
    odp = (input("papier, kamien, czy nozyce? :"))
    if lose == 1:
        x = "papier"
        print(x)
    if lose == 2:
        x = "kamien"
        print(x)
    if lose == 3:
        x = "nozyce"
        print(x)
    if odp == "papier":
        y = 1
    if odp == "kamien":
        y = 2
    if odp == "nozyce":
        y = 3

    if odp == "papier" or odp == "kamien" or odp == "nozyce":
        break
    else:
        print("powtorz prosze")



if lose == y:
    print("remis")

if lose == 1:
    if y == 2:
        print("przegrales")
    elif y == 3:
        print('wygrales')
if lose == 2:
    if y == 1:
        print("wygrales")
    elif y == 3:
        print("przegrales")
if lose == 3:
    if y == 2:
        print("wygrales")
    elif y == 1:
        print("przegrales")

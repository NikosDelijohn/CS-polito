def main():
    stop = False
    while not stop:
        partita()
        yn = input("Continue (y/n)? ")
        if yn.strip().lower().startswith("n"):
            stop = True


def partita():
    words = []

    last = input('Insert the starting word: ').strip().lower()

    valid_game = True
    while valid_game:
        new = input('Insert a word: ').strip().lower()
        if new == '*':
            print('You abandon!')
            valid_game = False
        elif len(new) < 2 or last[-2:] != new[:2]:
            print('Invalid word!')
            valid_game = False
        elif new in words:
            print('Repeated word!')
            valid_game = False
        else:
            last = new
            words.append(new)

if __name__ == "__main__":

    main()

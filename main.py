import random

MAX_ATTEMPTS = 6
POINTS_PER_LETTER = 100
POINTS_LOSS_WRONG = 50
BONUS_WIN = 500


def load_words():
    with open("words.txt", "r", encoding="utf-8") as f:
        words = [line.strip().upper() for line in f if line.strip()]
    return words


def show_word(secret, guessed):
    result = ""
    for letter in secret:
        if letter in guessed:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()


def check_letter(letter, secret, attempts, points):
    if letter in secret:
        count = secret.count(letter)
        points += POINTS_PER_LETTER * count
        print(f"Есть такая буква! +{POINTS_PER_LETTER * count} очков.")
    else:
        attempts -= 1
        points -= POINTS_LOSS_WRONG
        if points < 0:
            points = 0
        print(f"Нет такой буквы. -{POINTS_LOSS_WRONG} очков.")
    return attempts, points


def input_letter(guessed):
    while True:
        letter = input("Введите букву: ").upper().strip()
        if len(letter) != 1:
            print("Введите ровно одну букву!")
            continue
        if letter < 'А' or letter > 'Я':
            print("Только русские буквы!")
            continue
        if letter in guessed:
            print("Эту букву уже называли!")
            continue
        return letter


def show_win(secret, points):
    points += BONUS_WIN
    print(f"\nВы победили! Слово: {secret}")
    print(f"Бонус за победу: +{BONUS_WIN}")
    print(f"Очков за раунд: {points}")


def show_loss(secret, points):
    print(f"\nВы проиграли. Слово: {secret}")
    print(f"Очков за раунд: {points}")


def play_round():
    words = load_words()
    secret = random.choice(words)
    guessed = set()
    attempts = MAX_ATTEMPTS
    points = 0

    print(f"\nЗагадано слово из {len(secret)} букв.")

    while attempts > 0:
        print(f"\nСлово: {show_word(secret, guessed)}")
        print(f"Попыток: {attempts} | Очков: {points}")

        letter = input_letter(guessed)
        guessed.add(letter)
        attempts, points = check_letter(letter, secret, attempts, points)

        if "_" not in show_word(secret, guessed):
            show_win(secret, points)
            return

    show_loss(secret, points)


def show_menu():
    print("\n" + "-" * 30)
    print("1. Новая игра")
    print("2. Выход")
    return input("\nВаш выбор (1-2): ").strip()


def main():
    print("\n" + "=" * 30)
    print("ИГРА ВИСЕЛИЦА")
    print("=" * 30)

    while True:
        choice = show_menu()
        if choice == "1":
            play_round()
        elif choice == "2":
            print("\nСпасибо за игру!")
            break
        else:
            print("Неверный ввод! Выберите 1 или 2.")


if __name__ == "__main__":
    main()
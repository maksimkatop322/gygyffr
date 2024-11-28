import random

def start_game():
    print("Sveiks! Laipni lūdzam uzminēt spēli!")
    print("Es esmu izvēlējies nejaušu skaitli no 1 līdz 100.")
    print("Mēģini uzminēt šo skaitli!")
    secret_number = random.randint(1, 100)
    guessed_number = -1
    attempts = 0
    hint_given = False
    low_range = 1
    high_range = 100
    special_numbers = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    while guessed_number != secret_number:
        try:
            print(f"Skaitļu intervāls ir: {low_range} līdz {high_range}")
            guessed_number = int(input("Ievadi savu uzminēto skaitli (no 1 līdz 100): "))
        except ValueError:
            print("Lūdzu, ievadi skaitli.")
            continue

        if guessed_number < low_range or guessed_number > high_range:
            print(f"Skaitlim jābūt starp {low_range} un {high_range}.")
            continue

        attempts += 1
        if guessed_number < secret_number:
            print("Tavs skaitlis ir par mazu. Mēģini vēlreiz!")
            low_range = guessed_number + 1
        elif guessed_number > secret_number:
            print("Tavs skaitlis ir par lielu. Mēģini vēlreiz!")
            high_range = guessed_number - 1
        else:
            print(f"Tev izdevās uzminēt skaitli {secret_number}! Apsveicu!")
            print(f"Tu izmantoji {attempts} mēģinājumus.")
            break
        
        if not hint_given and attempts >= 5:
            print("Vai vēlies, lai es tev dotu norādi?")
            give_hint = input("Ievadi 'jā', lai saņemtu norādi, vai 'nē', lai turpinātu: ").strip().lower()
            if give_hint == 'jā':
                print("Norāde: Skaitlis ir dalāms ar 3." if secret_number % 3 == 0 else "Norāde: Skaitlis nav dalāms ar 3.")
                hint_given = True

        if attempts % 3 == 0:
            print("Atceries, ka uzminot skaitli pareizi, tu iegūsi iespēju uzvarēt!")

        if secret_number in special_numbers and attempts == 10:
            print("Tu esi uz pareizā ceļa! Skaitlis ir īpašs un atrodas zelta sarakstā!")

    play_again()

def play_again():
    while True:
        again = input("Vai vēlies spēlēt vēlreiz? (jā/nē): ").strip().lower()
        if again == 'jā':
            start_game()
            break
        elif again == 'nē':
            print("Paldies par spēlēšanu! Uz redzēšanos!")
            break
        else:
            print("Lūdzu, ievadi 'jā' vai 'nē'.")

def show_instructions():
    print("Spēles norādījumi:")
    print("1. Es izvēlēšos nejauši skaitli no 1 līdz 100.")
    print("2. Tavs uzdevums ir uzminēt šo skaitli.")
    print("3. Katru reizi, kad tu ievadīsi skaitli, es tev pateikšu, vai tas ir pārāk liels vai pārāk mazs.")
    print("4. Spēle beidzas, kad tu uzmini pareizo skaitli.")
    print("5. Kad spēle beidzas, tev tiks piedāvāts uzsākt jaunu spēli.")
    print("6. Ja uzminēšanas laikā ir vairāk nekā 5 mēģinājumi, varēsi saņemt norādi par skaitļa īpašībām.")
    print("7. Ja uzminēsi skaitli pareizi 10. mēģinājumā, saņemsi īpašu balvu par veiksmi!")
    print("8. Ja skaitlis ir dalāms ar 3, tas ir īpašs skaitlis.")
    print("9. Katru reizi, kad tu ievadīsi skaitli, es centīšos sniegt norādes un motivēt uzvarēt!\n")

def main():
    show_instructions()
    start_game()

if __name__ == "__main__":
    main()

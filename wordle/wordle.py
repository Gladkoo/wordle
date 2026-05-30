import random
import sys

WORDS = [
    "apple", "brave", "chess", "dress", "eagle",
    "flame", "grace", "heart", "ivory", "joker",
    "knife", "lemon", "magic", "noble", "ocean",
    "piano", "queen", "river", "stone", "tiger",
    "ultra", "vapor", "waltz", "xenon", "yacht",
    "zebra", "angel", "beard", "candy", "daisy",
    "elbow", "fable", "giant", "honey", "inlet",
    "jewel", "karma", "laser", "maple", "nerve",
    "orbit", "pearl", "quest", "radar", "salsa",
    "toast", "umbra", "vibes", "waste", "xerox",
    "young", "zonal", "acute", "blaze", "crane",
    "drift", "ember", "forge", "gloom", "haste",
    "ingot", "jazzy", "kneel", "lunar", "mayor",
    "ninety", "oxide", "plank", "quirk", "raven",
    "shelf", "trend", "upset", "vigil", "wheat",
    "boxer", "crisp", "depot", "elope", "finch",
    "grind", "hulk", "irony", "jumpy", "kinky",
    "llama", "mango", "notch", "olive", "patch",
    "rapid", "scorn", "taunt", "unify", "venom",
    "woken", "expel", "youth", "zippy", "aloft",
    "brine", "cleft", "drill", "evade", "fiery",
    "grasp", "hound", "icing", "jaunt", "knack",
    "light", "mourn", "nymph", "optic", "prism",
    "relay", "swamp", "taboo", "undue", "vouch",
    "wrist", "exult", "yearn", "zilch", "abide",
    "brood", "clown", "dowry", "exert", "flint",
    "groan", "hippo", "image", "khaki",
    "llano", "mirth", "noisy", "ounce", "proxy",
    "rebut", "sting", "tulip", "until",
    "witch", "yucky", "zesty",
]

WORDS = [w for w in WORDS if len(w) == 5]

GREEN  = "\033[42m\033[97m"
YELLOW = "\033[43m\033[97m"
GRAY   = "\033[100m\033[97m"
RESET  = "\033[0m"
BOLD   = "\033[1m"

def color_guess(guess, target):
    result = []
    target_chars = list(target)
    guess_chars = list(guess)
    colors = ["gray"] * 5

    # First pass: greens
    for i in range(5):
        if guess_chars[i] == target_chars[i]:
            colors[i] = "green"
            target_chars[i] = None

    # Second pass: yellows
    for i in range(5):
        if colors[i] == "green":
            continue
        if guess_chars[i] in target_chars:
            colors[i] = "yellow"
            target_chars[target_chars.index(guess_chars[i])] = None

    for i, letter in enumerate(guess_chars):
        c = colors[i]
        if c == "green":
            result.append(f"{GREEN} {letter.upper()} {RESET}")
        elif c == "yellow":
            result.append(f"{YELLOW} {letter.upper()} {RESET}")
        else:
            result.append(f"{GRAY} {letter.upper()} {RESET}")

    return "".join(result)

def print_board(guesses, target):
    print()
    for guess in guesses:
        print("  " + color_guess(guess, target))
    for _ in range(6 - len(guesses)):
        print("  " + "".join([f"{GRAY}   {RESET}"] * 5))
    print()

def print_keyboard(guesses, target):
    all_letters = "qwertyuiopasdfghjklzxcvbnm"
    green_letters  = set()
    yellow_letters = set()
    gray_letters   = set()

    for guess in guesses:
        for i, ch in enumerate(guess):
            if ch == target[i]:
                green_letters.add(ch)
            elif ch in target:
                yellow_letters.add(ch)
            else:
                gray_letters.add(ch)

    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for row in rows:
        line = "  "
        for ch in row:
            if ch in green_letters:
                line += f"{GREEN} {ch.upper()} {RESET}"
            elif ch in yellow_letters:
                line += f"{YELLOW} {ch.upper()} {RESET}"
            elif ch in gray_letters:
                line += f"{GRAY} {ch.upper()} {RESET}"
            else:
                line += f" {ch.upper()} "
        print(line)
    print()

def main():
    target = random.choice(WORDS)
    guesses = []
    max_attempts = 6

    print(f"\n{BOLD}╔══════════════════╗")
    print("║     W O R D L E    ║")
    print(f"╚══════════════════╝{RESET}")
    print("  Zgadnij 5-literowe słowo w 6 próbach!")
    print(f"  {GREEN} Z {RESET} dobra litera, dobre miejsce")
    print(f"  {YELLOW} Ż {RESET} litera jest, złe miejsce")
    print(f"  {GRAY} X {RESET} litery nie ma w słowie\n")

    while len(guesses) < max_attempts:
        print_board(guesses, target)
        print_keyboard(guesses, target)

        attempt = len(guesses) + 1
        try:
            guess = input(f"  Próba {attempt}/6: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print(f"\n  Słowo to było: {BOLD}{target.upper()}{RESET}\n")
            sys.exit(0)

        if len(guess) != 5:
            print("  Wpisz dokładnie 5 liter!\n")
            continue

        if not guess.isalpha():
            print("  Tylko litery!\n")
            continue

        guesses.append(guess)

        if guess == target:
            print_board(guesses, target)
            msgs = ["Genialne!", "Świetnie!", "Nieźle!", "Dobra robota!", "Uff, prawie!", "Na styk!"]
            print(f"  {BOLD}{msgs[len(guesses)-1]}{RESET} Słowo to {BOLD}{target.upper()}{RESET}!\n")
            return

    print_board(guesses, target)
    print(f"  Nie udało się. Słowo to było: {BOLD}{target.upper()}{RESET}\n")

if __name__ == "__main__":
    main()

MORSE_SEQUENCE = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
TEXT_SEQUENCE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# create a {text:morse} dictionary
text_to_morse = {TEXT_SEQUENCE[i]: MORSE_SEQUENCE.split(
    ' ')[i] for i in range(len(TEXT_SEQUENCE))}

# create a {morse:text} dictionary
morse_to_text = {morse: text for (text, morse) in text_to_morse.items()}


def translate_text_to_morse():
    text = input("Enter text to be converted...\n")

    result = ''
    for char in text:
        try:
            result += text_to_morse[char.upper()]
            result += " "
        except:
            if char == " ":
                result += " / "
            else:
                print(f"Could not convert this character: '{char}' (skipped)")

    print(f"Result: \n{result}")
    return result


def translate_morse_to_text():
    text = input("Enter Morse to be translated...\n")

    result = ''
    for char in text.split(' '):
        try:
            result += morse_to_text[char]
        except:
            if char == "/":
                result += " "
            elif char == "":
                pass
            else:
                print(f"Could not convert this character: '{char}' (skipped)")

    print(f"Result: \n{result}")
    return result


while(True):
    selected_option = input(
        "Welcome to Morse Code Translator!\n\
        (TEXT TO MORSE) Enter option 'A' if you want to convert plain text to Morse code. OR...\n\
        (MORSE TO TEXT) Enter option 'B' if you want to translate Morse code to plain text instead.\n")

    if selected_option.upper() == "A":
        translate_text_to_morse()
        break
    elif selected_option.upper() == "B":
        translate_morse_to_text()
        break
    else:
        print("Improper option. Please try again.")

# Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді
# коду Морзе та виводить декодоване значення (латинськими літерами).
#    Особливості:
#     - використовуються лише крапки, тире і пробіли (.- )
#     - один пробіл означає нову літеру
#     - три пробіли означають нове слово
#     - результат може бути case-insensetive (на ваш розсуд - велики чи
#     маленькими літерами).
#     - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки
#     тощо використовуватися не будуть. Лише латинські літери.
#     - додайте можливість декодування сервісного сигналу SOS (...---...)
#     Приклад:
#     --. . . -.- .... ..- -...   .. ...   .... . .-. .
#     результат: GEEKHUB IS HERE

class InvalidSymbol(Exception):
    pass


def validation(string_argument):
    return any(char not in [".", "-", " "] for char in string_argument)


def morse_code(string_argument):
    morse_dict = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
            '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
            '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
            '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z', '...---...': 'SOS'
    }

    words = string_argument.split("   ")
    result = ""

    for item in words:
        letters = item.split()

        for letter in letters:
            if validation(string_argument):
                raise InvalidSymbol("input string has not allow symbols")
            result += morse_dict[letter]
        result += " "

    return result


try:
    morse_str = "--. . . -.- .... ..- -...   .. ...   .... . .-. ."
    print(morse_code(morse_str))
except InvalidSymbol as e:
    print(str(e))

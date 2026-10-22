import math
def to_number(text):
    sign = 1
    while text[0] in '+-':
        if text[0] == '-':
            sign = -sign
        text = text[1:]
    return sign * float(text)


def arith(s):
    total = 0.0
    sign = 1
    term = 1.0
    op = '*'
    num = ''
    for ch in s + '+':
        if ch in '+-*/' and num != '' and num[-1] not in '+-':
            value = to_number(num)
            num = ''
            if op == '*':
                term = term * value
            else:
                term = term / value
            if ch == '*' or ch == '/':   # слагаемое продолжается
                op = ch
            else:                        # слагаемое закончилось, добавляем в сумму
                total = total + sign * term
                term = 1.0
                op = '*'
                if ch == '+':
                    sign = 1
                else:
                    sign = -1
        else:
            num += ch
    return total


def ravenstvo(s):
    pos = s.rfind('==')
    if pos == -1:
        return arith(s)
    left = arith(s[:pos])
    right = arith(s[pos + 2:])
    if abs(left - right) < 1e-9:
        return 1
    return 0


def calc(s):
    s = s.replace(' ', '')

    letters = ''.join(ch for ch in s if ch.isalpha())
    if letters and letters != 'sqrt':
        return "Зачем буквы ввел?"

    # проверка скобок: depth — сколько скобок сейчас открыто
    depth = 0
    for ch in s:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth < 0:
                return "Скобку потерял, брат"
    if depth > 0:
        return "Скобку потерял, брат"

    while ')' in s:
        right = s.find(')')            # первая закрывающая скобка
        left = s.rfind('(', 0, right)  # ближайшая к ней открывающая слева
        value = ravenstvo(s[left + 1:right])
        if s[:left].endswith('sqrt'):  # перед скобкой стоит sqrt — берём корень
            value = math.sqrt(value)
            left -= 4                  # и вырезаем вместе со словом sqrt
        s = s[:left] + str(value) + s[right + 1:]

    return ravenstvo(s)


print(calc(input('Введи выражение:')))
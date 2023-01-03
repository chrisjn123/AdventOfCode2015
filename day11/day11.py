password = 'hepxxyzz'

def increment(pw: str) -> str:
    digits = [ord(ch) - ord("a") for ch in reversed(pw)]
    num = sum((26 ** i) * digit for i, digit in enumerate(digits))
    if num == sum((26 ** i) * 25 for i in range(len(pw))):
        num = 0
    else:
        num += 1
    new_digits = []
    for _ in range(len(pw)):
        next_digit = num % 26
        new_digits.append(next_digit)
        num //= 26
    new_letters = [chr(i + ord("a")) for i in new_digits]
    return "".join(reversed(new_letters))

def rule_1(pw: str)->bool:
    ''' Must contain 3 or more increasing letters. '''
    return any(
        ord(a) == ord(b) - 1 == ord(c) -2
        for a, b, c in zip(pw, pw[1:], pw[2:])
    )

def rule_2(pw: str)->bool:
    ''' Must NOT contain 'i', 'o', or 'l' '''
    if 'i' in pw or 'l' in pw or 'o' in pw:
        return False
    return True

def rule_3(pw: str)->bool:
    found = set()
    for a, b in zip(pw, pw[1:]):
        if a == b:
            found.add(a)
    
    return len(found) > 1

while True:
    password = increment(password)
    if all((rule_1(password), rule_2(password), rule_3(password))):
        print(password)
        break
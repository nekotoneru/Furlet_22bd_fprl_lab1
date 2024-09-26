number = input("введіть 4цифрове число: ")
summ = 0
mult = 1
for ch in number:
    summ = summ + int(ch)
    mult = mult * int(ch)
print("сума цифр:", summ)
print("добуток цифр:", mult) 
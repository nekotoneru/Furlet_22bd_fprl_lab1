year = int(input("введіть рік: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "є високосним роком")
else:
    print(year, "не є високосним роком")
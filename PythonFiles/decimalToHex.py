#8 hex digits max, 4,294,967,295 max

x = int(input("Pick a number.\n"))
for i in range(8):
dig0 = x % 16; x = x // 16
dig1 = x % 16; x = x // 16
dig2 = x % 16; x = x // 16
dig3 = x % 16; x = x // 16
dig4 = x % 16; x = x // 16
dig5 = x % 16; x = x // 16
dig6 = x % 16; x = x // 16
dig7 = x % 16; x = x // 16


print(dig7,dig6,dig5,dig4,dig3,dig2,dig1,dig0)

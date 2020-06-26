import sys

number = input('Entrer un nombre décimal: ')
listletter = ['A', 'B', 'C', 'D', 'E', 'F']

if number.isdigit() == False:
    sys.exit("Veuillez saisir un nombre valide")

print("Décimal: ", number)

#decimal vers binaire
binnumber = []
number = int(number)
result = number / 2
temp = 0
while result >= 1:
    if result.is_integer() == False:
        binnumber.append(1)
        result = int(result)
    elif result.is_integer():
        binnumber.append(0)
    result = result / 2
binnumber.append(1)
reversebinnumber = binnumber[::-1]

strings = [str(integer) for integer in  reversebinnumber]
a_string = "".join(strings)
number = str(a_string)

print("Binaire: ", number)

#binaire vers hexadecimal
hexa = []
lenght = len(number) /4
if (lenght-int(lenght) == 0.25) :
    number = '000' + number
elif (lenght-int(lenght) == 0.5) :
    number = '00' + number
elif (lenght-int(lenght) == 0.75) :
    number = '0' + number
groups = [ number[i:i+4] for i in range(0, len(number), 4) ]
temp = 0
while len(groups) != temp:
    group = list(groups[temp])
    group = group[::-1]
    secondTemp = 0
    total = 0
    while len(group) != secondTemp:
        bit = int(group[secondTemp])
        bitValue = bit * (2 ** secondTemp)
        total = total + bitValue
        secondTemp = secondTemp + 1
    if total > 9:
        hexnumber = listletter[total-10]
    else :
        hexnumber = total
    hexa.append(hexnumber)
    temp = temp + 1
strings = [str(integer) for integer in  hexa]
a_string = "".join(strings)
number = str(a_string)

print("Hexadécimal: ", number)
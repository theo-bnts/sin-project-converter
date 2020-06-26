import sys

number = input('Entrer un nombre binaire: ')
listletter = ['A', 'B', 'C', 'D', 'E', 'F']

if number.isdigit() == False:
    sys.exit("Veuillez saisir un nombre valide")

temp = 0
while temp != len(number):
    if int(number[temp]) > 1:
        sys.exit("Veuillez saisir un nombre valide")
    temp = temp+1

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

#hexadecimal vers décimal
decnumber = []
temp = 0
while temp != len(number):
    if number[temp] in listletter:
        tempv = listletter.index(number[temp])
        decnumber.append(tempv + 10)
    elif number[temp].isdigit(): 
        decnumber.append(number[temp])
    else :
        sys.exit("Veuillez saisir un nombre valide")
    temp = temp + 1
temp = 0
total = 0
reversedecnumber = decnumber[::-1]
while temp != len(number):
    total = total + int(reversedecnumber[temp]) * 16 ** temp
    temp = temp + 1
    
print("Décimal: ", total)
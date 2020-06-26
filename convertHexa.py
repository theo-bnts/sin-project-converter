import sys

number = input('Entrer un nombre hexadécimal: ').upper()
listletter = ['A', 'B', 'C', 'D', 'E', 'F']

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

#decimal vers binaire
binnumber = []
number = int(total)
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
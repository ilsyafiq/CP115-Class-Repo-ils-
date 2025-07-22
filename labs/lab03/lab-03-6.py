yardLength = float(input())
yardWidth = float(input())
houseLength = float(input())
houseWidth = float(input())
mowedArea = yardLength * yardWidth - houseLength * houseWidth
wage = mowedArea * 2
print(wage)


from random import randint

#player degiskeni tanimla yaptik
# kullanicidan gelen degeri player degiskenine aktardik

player = input ("rock(r),paper(p),scissors(s)?")  # niye print yerne input?
print(player, 'vs.....')
choose = randint(1, 3)


if choose == 1:
    computer = 'r'
elif choose == 2:
    computer = 'p'
elif choose == 3:
    computer = 's'

print(player, 'vs', computer)

if player == 's' and computer == 's':
    print('Berabere')

if player == 'p' and computer == 'p':
    print('Berabere')

if player == 'r' and computer == 'r':
    print('Berabere')

elif player == 'r' and computer == 's':
    print('sen kazandin')

elif player == 'r' and computer == 'p':
    print('bilgisayar kazandi')

elif player == 's' and computer == 'r':
    print('bilgisayar kazandi')

elif player == 's' and computer == 'p':
    print('sen kazandin')

elif player == 'p' and computer == 'r':
    print('sen kazandin')

elif player == 'p' and computer == 's':
    print('bilgisayar kazandi')
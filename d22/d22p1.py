import time

def repair(x, y = 9):
	return (y - len(x)) * '0' + x

def pas2(x):
	enemy_hp = 50
	for idx, letters in enumerate(x):
		if letters == '0':
			enemy_hp -= 4
		elif letters == '1':
			enemy_hp -= 2
		elif letters == '3':
			if len(x) - idx * 2 + 1 > 5:
				enemy_hp -= 3 * 5
			else:
				enemy_hp -= 3 * len(x) - idx  * 2 + 1

	if enemy_hp > 0:
		return False
	for letter1 in range(len(x)):
		if x[letter1] == '2' or x[letter1] == '3' or x[letter1] == '4':
			for letter2 in range(letter1 - 1):
				if letter1 - letter2 < 6:
					if x[letter1] == x[letter2]:
						return False
			for letter2 in range(len(x) - (letter1 + 1)):
				letter2 += 1 + letter1
				if letter2 - letter1 < 6:
					if x[letter1] == x[letter2]:
						return False
	return True

def fight(x):

	my_hp = 50
	my_mana = 500
	my_armor = 0
	used_mana = 0
	#my_hp = 10
	#my_mana = 250
	
	enemy_hp = 58
	enemy_dmg = 9
	#enemy_hp = 13
	#enemy_dmg = 8
	
	effect_1 = 0
	effect_2 = 0
	effect_3 = 0
	for i in range(len(x)):

		if effect_1 > 0:
			effect_1 -= 1
		if effect_2 > 0:
			enemy_hp -= 3
			effect_2 -= 1
		if effect_3 > 0:
			my_mana += 101
			effect_3 -= 1

		if enemy_hp < 1:
			return [True, used_mana]

		if x[i] == '0':

			used_mana += 53

			my_mana -= 53
			enemy_hp -= 4

		elif x[i] == '1':

			used_mana += 73

			my_mana -= 73
			enemy_hp -= 2
			my_hp += 2

		elif x[i] == '2':

			used_mana += 113

			my_mana -= 113
			effect_1 = 6

		elif x[i] == '3':

			used_mana += 173

			my_mana -= 173
			effect_2 = 6

		else:

			used_mana += 229

			my_mana -= 229
			effect_3 = 5

		if my_mana > 0:
			if  enemy_hp > 0:

				if effect_1 > 0:
					my_armor = 7
					effect_1 -= 1
				else:
					my_armor = 0
				if effect_2 > 0:
					enemy_hp -= 3
					effect_2 -= 1
				if effect_3 > 0:
					my_mana += 101
					effect_3 -= 1

				if enemy_hp < 1:
					return [True, used_mana]

				if enemy_dmg - my_armor < 1:
					my_hp -= 1
				else:
					my_hp -= (enemy_dmg - my_armor)

				if my_hp < 1:
					return [False]
			else:
				return [True, used_mana]

			
		else:
			return [False]
			
	return [False]

def binar(x):
	out = ''
	while x > 0:
		out = str(x % 5) + out
		if x % 5 == 1:
			x = (x - 1) / 5
		else:
			x = x / 5
	return out

def program(start, end, lght):
	for start in range(start, end):

		i = repair(binar(start), lght)

		if pas2(str(i)):
			current_mana = fight(str(i))
			if current_mana[0]:
				print '++++++++++++++++++++++++'
				print '+   ' + i
				print '+   ' + str(current_mana[1])


lght = 13
fast_help = 0


while len(str(binar(fast_help))) < lght + 1:
	fast_help += 1000


program(0, fast_help, lght)
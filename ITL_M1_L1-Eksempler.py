### Kode Stumper til Lektion #1
### Christian, Sasha & Signe

### Variable Demo
besked = ""								# Tekst (Strings)
ord1 = "Hej"
ord2 = " med "
ord3 = "dig!"
besked = ord1 + ord2 + ord3

tal1 = 5								# Heltal (Integers)
tal2 = 10
sum = tal1 + tal2
life_universe_everything = sum + 27

det_passer = True						# Sand / Falsk (Boolean)
det_loegn = False

stadig_tekst = "42"						# Strings
print("Tallet er " + stadig_tekst)

tal3 = 7.42								# Decimaltal (Floating Point)
tal4 = 34.58
tal5 = 99.23459856712343256
sum = tal3 + tal4
print(sum * tal5 / tal4)

print()

### FOR Demo
for taeller in reversed(range(43)):		# Sjov med Range() - I øvrigt ikke den eneste måde at bruge FOR...
	print(taeller)

print()

for taeller in range(8):
	print(taeller)

print()

for taeller in range(1, 8):
	print(taeller)

print()

for taeller in range(1, 8, 2):
	print(taeller)

print()

### IF-ELSE demo
tal = 42
if (tal < 10):							# Sjov med IF sætninger
	print("Tallet er mindre end 10")
else:
	print("Tallet er ikke mindre end 10") 

if (det_passer):						# Kan i gennemskue hvad der sker her?
    print("DET PASSER!!!!")

if (det_loegn == True):					# Se om i kan ændre output uden at pille i IF-sætningen -> i må kun ændre data ovenfor...
	print("Det er Loegn!")
elif (det_passer == False):
	print("Det passer altså ikke...")
elif (sum == 42.0):
	print("The answer to life, the universe and everything...Cheers Douglas!")
else:
	print("Kun naar alt andet fejler...")


def sons_mot(mot):
	sons = []
	ind = 0
	while True:
		if ind == len(mot):
			break
		if mot[ind] in ["p", "f", "t", "b", "v", "d", "m", "n", "s", "z", "k", "r"]:
			sons.append(mot)
			ind += 1
			continue
		elif mot[ind] == "a":
			pass
		elif mot[ind] == "e":
			pass
		elif mot[ind] == "o":
			pass
		elif mot[ind] == "u":
			pass
		elif mot[ind] == "i":
			pass


	return sons
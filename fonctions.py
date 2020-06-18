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
		elif mot[ind] == "e":


	return sons
# https://edabit.com/challenge/2hvruws6kgiKj98Rv


def scottish_screaming(txt):
	lst = list(txt.upper())
	for i in range(len(lst)):
		if "AEIOU".count(lst[i]) != 0:
			lst[i] = "E"
	return "".join(lst)


print(scottish_screaming("hello robert"))
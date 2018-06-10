def saltProing(argPar):
	charVal = 0
	count = 0
	salt = '1001'
	binStrT = ''
	saltCast = ''
	saltCastFinal = ''
	argPar = str(argPar)
	for charac in argPar:
		charVal = ord(charac)
		binStr = '{0:08b}'.format(charVal)
		binStr1 = int(binStr,2)+int(salt,2)
		binStr = '{0:08b}'.format(binStr1)
		binStrT = binStrT + binStr

	for index in range(0,len(binStrT)):
		saltCast = saltCast + binStrT[index]
		if(len(saltCast) == 8):
			asciiSC = int(saltCast,2)
			SCchar = chr(asciiSC)
			saltCastFinal = saltCastFinal + SCchar
			saltCast = ''
	#binStr1 = int(binStr)
	return saltCastFinal


print(saltProing('This is a nice day!'))
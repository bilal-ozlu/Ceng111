def ToEarthian(zx):
	return earth(zx,"","")
def earth(zx,final,stack):
	if zx == "":
		if stack == "":
			return help(final)
		else:
			final = final + stack[::-1]
			return help(final)
	elif zx[0] == " ":
		return earth(zx[1:],final,stack)
	elif zx[0] == "+":
		if stack != "" and stack[-1] == "+":
			final = final + stack[-1]
			stack = stack[:-1]
			return earth(zx,final,stack)
		else:
				stack = stack + zx[0]
				return earth(zx[1:],final,stack)
	elif zx[0] == "/":
		if stack == "":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		elif stack[-1] == "*" or stack[-1] == "-" or stack[-1] == "^" or stack[-1] == "(":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		else:
			final = final + stack[-1]
			stack = stack[:-1]
			return earth(zx,final,stack)
	elif zx[0] == "-":
		if stack == "":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		elif stack[-1] == "*" or stack[-1] == "^" or stack[-1] == "(":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		else:
			final = final + stack[-1]
			stack = stack[:-1]
			return earth(zx,final,stack)
	elif zx[0] == "*":
		if stack == "":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		elif stack[-1] == "^" or stack[-1] == "(":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		else:
			final = final + stack[-1]
			stack = stack[:-1]
			return earth(zx,final,stack)
	elif zx[0] == "^":
		if stack == "":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		elif stack[-1] == "^" or stack[-1] == "(":
			stack = stack + zx[0]
			return earth(zx[1:],final,stack)
		else:
			final = final + stack[-1]
			stack = stack[:-1]
			return earth(zx,final,stack)
	elif zx[0] == "(":
		stack = stack + zx[0]
		return earth(zx[1:],final,stack)
	elif zx[0] == ")":
		final = final + stack[::-1][:stack[::-1].index("(")]
		stack = stack[::-1][stack[::-1].index("(")+1::][::-1]
		return earth(zx[1:],final,stack)
	else:
			final = final + zx[0]
			return earth(zx[1:],final,stack)



def ToZoitankian(ex):
	return zoitank(ex,"","")
def zoitank(ex,final,stack):
	if ex == "":
		if stack == "":
			return help(final)
		else:
			final = final + stack[::-1]
			return help(final)
	elif ex[0] == " ":
		return zoitank(ex[1:],final,stack)
	elif ex[0] == "^":
		stack = stack + ex[0]
		return zoitank(ex[1:],final,stack)
	elif ex[0] == "/" or ex[0] == "*":
		if stack == "":
			stack = stack + ex[0]
			return zoitank(ex[1:],final,stack)
		elif stack[-1] == "+" or stack[-1] == "-" or stack[-1] == "(":
			stack = stack + ex[0]
			return zoitank(ex[1:],final,stack)
		else:
			final = final + stack[-1]
			stack = stack[:-1]
			return zoitank(ex,final,stack)
	elif ex[0] == "+" or ex[0] == "-":
		if stack == "":
			stack = stack + ex[0]
			return zoitank(ex[1:],final,stack)
		elif stack[-1] == "(":
			stack = stack + ex[0]
			return zoitank(ex[1:],final,stack)
		else:
			final = final + stack[-1]
			stack = stack[:-1]
			return zoitank(ex,final,stack)
	elif ex[0] == "(":
		stack = stack + ex[0]
		return zoitank(ex[1:],final,stack)
	elif ex[0] == ")":
		final = final + stack[::-1][:stack[::-1].index("(")]
		stack = stack[::-1][stack[::-1].index("(")+1::][::-1]
		return zoitank(ex[1:],final,stack)
	else:
			final = final + ex[0]
			return zoitank(ex[1:],final,stack)



def help(final):
	return helphelp(final,[],"")
def helphelp(final,depo,netice):
	if final == "":
		return fevkalade(depo[0][1:-1])
	elif final[0]=="a" or final[0]=="b" or final[0]=="c" or final[0]=="d" or final[0]=="e" or final[0]=="f" or final[0]=="g" or final[0]=="h" or final[0]=="i" or final[0]=="j" or final[0]=="k" or final[0]=="l" or final[0]=="m" or final[0]=="n" or final[0]=="o" or final[0]=="p" or final[0]=="q" or final[0]=="r" or final[0]=="s" or final[0]=="t" or final[0]=="u" or final[0]=="v" or final[0]=="w" or final[0]=="x" or final[0]=="y" or final[0]=="z":
		depo.append(final[0])
		return helphelp(final[1:],depo,netice)
	else:
		deponundadeposu = ("(" + depo[-2] + final[0] + depo[-1] + ")")
		depo = depo[:-2]
		depo.append(deponundadeposu)
		return helphelp(final[1:],depo,netice)
def fevkalade(depo):
	depo=depo.replace("/","<<<")
	depo=depo.replace("*","|||")
	depo=depo.replace("<<<","*")
	coksukur=depo.replace("|||","/")
	return coksukur


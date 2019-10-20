command, param = str(input()).split()

cmd = ''

if command == 'convert':

	file = open(param)
	prog = file.read()

	for i in prog:
		if i != '\n':
			cmd += i
			#print(i)
			#print(cmd)
		else:
			cmd += '\n'
			resStr = param.split('.')
			res = open('{}.asm'.format(resStr), 'w')
			res.write(cmd)
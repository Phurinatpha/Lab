message = "123"
pattern = "** *** ** ** *"

out = [' ']*len(pattern)
n=0
message = ''.join((message.split()))

for i,mes in enumerate(pattern):
	if mes == "*":
		out[i] = message[n%len(message)]
		n+=1
	elif mes == "\n":
		pass

print(''.join(out))
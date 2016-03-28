text_file = open('texto.txt', 'r')
text = text_file.read()
text_file.close()

word = str(raw_input("Insira uma palavra pra ser encontrada: "))

for i in range(len(text)):
	count = 0
	for j in range(len(word)):
		if i + j < len(text):
			if text[i+j] == word[j]:
				count += 1
			else:
				break	

	if count > 0 and count == len(word):
		print "Palavra encontrada na posicao", i, "do texto."
		print text[i:i+count]		
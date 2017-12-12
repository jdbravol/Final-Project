from __future__ import print_function
import numpy as np
import pronouncing

# method for generating text
def generate_text(model, length, vocab_size, ix_to_char):
	result = ''
	lastwords = []
	for i in range(4):
		rhyme = False

		while not rhyme:
			# starting with random character
			ix = [np.random.randint(vocab_size)]
			y_char = [ix_to_char[ix[-1]]]

			X = np.zeros((1, length, vocab_size))

			for j in range(100):
				# appending the last predicted character to sequence
				X[0, j, :][ix[-1]] = 1
				print(ix_to_char[ix[-1]], end="")
				ix = np.argmax(model.predict(X[:, :j+1, :])[0], 1)
				y_char.append(ix_to_char[ix[-1]])

				if ix_to_char[ix[-1]] == '\n':
					y_char.append('\n')
					break
			
			line = ('').join(y_char)
			lastword = line.rsplit(None, 1)[-1]

			if i == 0:
				lastwords.append(lastword)
				rhyme = True
			else:
				rhymes = pronouncing.rhymes(lastwords[i - 1])
				if lastword in rhymes:
					rhyme = True

		result += line + '\n'
	return result

# method for preparing the training data
def load_data(data_dir, seq_length):
	data = open(data_dir, 'r', encoding='utf-8').read()
	chars = list(set(data))
	VOCAB_SIZE = len(chars)

	print('Data length: {} characters'.format(len(data)))
	print('Vocabulary size: {} characters'.format(VOCAB_SIZE))

	ix_to_char = {ix:char for ix, char in enumerate(chars)}
	char_to_ix = {char:ix for ix, char in enumerate(chars)}

	X = np.zeros((int(len(data) / seq_length), seq_length, VOCAB_SIZE))
	y = np.zeros((int(len(data) / seq_length), seq_length, VOCAB_SIZE))
	for i in range(0, int(len(data) / seq_length)):
		X_sequence = data[i*seq_length:(i+1)*seq_length]
		X_sequence_ix = [char_to_ix[value] for value in X_sequence]
		input_sequence = np.zeros((seq_length, VOCAB_SIZE))
		for j in range(seq_length):
			input_sequence[j][X_sequence_ix[j]] = 1.
			X[i] = input_sequence

		y_sequence = data[i*seq_length+1:(i+1)*seq_length+1]
		y_sequence_ix = [char_to_ix[value] for value in y_sequence]
		target_sequence = np.zeros((seq_length, VOCAB_SIZE))
		for j in range(seq_length):
			target_sequence[j][y_sequence_ix[j]] = 1.
			y[i] = target_sequence
	return X, y, VOCAB_SIZE, ix_to_char
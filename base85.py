
def _chunk(data):
	# TODO: remove white space
	idx = 0
	while len(data) > idx:
		if data[idx] in 'yz':
			next = data[idx]
			idx += 1
			if next == 'z':
				yield '!!!!!', 0 # 4xNUL
			else:
				assert False # FIXME: 4xSPACE
		else:
			next = data[idx:idx+5]
			idx += len(next)
			padding = 5 - len(next)
			if padding:
				next = next.ljust(5, 'u')
			if next > 's8W-!':
				return
			yield next, padding
def _decode(chunk, padding):
	assert len(chunk) == 5
	num = (((((ord(chunk[0]) - 33)
		 * 85 + ord(chunk[1]) - 33)
		 * 85 + ord(chunk[2]) - 33)
		 * 85 + ord(chunk[3]) - 33)
		 * 85 + ord(chunk[4]) - 33)
	return ('%c%c%c%c' % (
		chr(num >> 24),
		chr((num >> 16) & 0xff),
		chr((num >> 8) & 0xff),
		chr(num & 0xff)
	))[0:4-padding]
def b85encode(text):
	from Crypto.Util.number import bytes_to_long
	text += '\x00' * ((4 - len(text)) % 4)
	print len(text)
	output = []
	for j in range(0,len(text),4):
		num = bytes_to_long(text[j:j+4])
		result = ''
		for i in range(5):
			result = chr((num % 85) + 33) + result
			num = num / 85
		output.append(result)
	return ''.join(output)
def b85decode(x):
	text = ''
	try:
		for i in _chunk(x):
			text += _decode(*i)
		return text
	except:
		raise
def convert(text,seperator,mode):
	if seperator == '':
		try:
			from Crypto.Util.number import long_to_bytes
			return str(long_to_bytes(int(text,int(mode))))[2:-1]
		except ValueError:
			raise Exception("Invalid number!")
	else:
		text = text.split(seperator)
		result = ''
		for t in text:
			try:
				result += chr(int(t,int(mode)))
			except ValueError:
				raise Exception("Number exceed 255!")
		return result

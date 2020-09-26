SUCCESS = u"""<h3>Result: </h3>
				<div id="resulttext" class="ht-tm-element alert alert-success alert-dismissible fade show mt-3" role="alert" id="result">
			  <button type="button" data-clipboard-target="#resulttext" class="close" data-container="body" data-toggle="popover" data-placement="top" data-content="Copied"><i class="far fa-copy"></i></button>
				 %s
			  </div>"""
FAIL = u"""<div class="ht-tm-element alert alert-danger alert-dismissible fade show mt-3" role="alert" id="result">
				<button type="button" class="close" data-dismiss="alert" aria-label="Close">
				  <span aria-hidden="true">×</span>
				</button>
				<strong>Error: </strong> %s
			  </div>"""
def multiResult(*result):
	output = ''
	for i,r in enumerate(result):
		output += SUCCESS.replace("Result:",r[0]).replace("resulttext","result"+str(i)) % str(r[1].replace("\n","<br>"))
	
	return output

def caesar(text,n=0):
	import string
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	if n != 0:
		lowerTrans = str.maketrans(lower,lower[n:] + lower[:n])
		upperTrans = str.maketrans(upper,upper[n:] + upper[:n])
		text = SUCCESS %(text.translate(lowerTrans).translate(upperTrans))
	else:
		result = ''
		for n in range(1,26):
			lowerTrans = str.maketrans(lower,lower[n:] + lower[:n])
			upperTrans = str.maketrans(upper,upper[n:] + upper[:n])
			result += f"<b>Shift {n}:</b> {text.translate(lowerTrans).translate(upperTrans)}<br>"
		text = SUCCESS % result
	return text
def vigenere(text,password,encode=False):
	try:
		text = bytearray(text.lower(),"utf-8")
		password = bytearray(password.lower(),"utf-8")
	except:
		return FAIL % "Invalid text or password!"
	if encode:
		j = 0
		for i in range(len(text)):
			if text[i] >= 0x61 and text[i] <= 0x7a:
				text[i] = (((text[i]-0x61)+(password[j%len(password)]-0x61))%26)+0x61
				j += 1
	else:
		j = 0
		for i in range(len(text)):
			if text[i] >= 0x61 and text[i] <= 0x7a:
				text[i] = (((text[i]-0x61)-(password[j%len(password)]-0x61))%26)+0x61
				j += 1
	return SUCCESS % text.decode() 
def b64(text,encode=False):
	import base64
	pattern = "^(?:[a-zA-Z0-9+\\/]{4})*(?:|(?:[a-zA-Z0-9+\\/]{3}=)|(?:[a-zA-Z0-9+\\/]{2}==)|(?:[a-zA-Z0-9+\\/]{1}===))$"
	text = bytes(text,"utf-8")
	if encode:
		return SUCCESS % base64.b64encode(text).decode("utf-8")
	try:
		return SUCCESS % str(base64.b64decode(text))[2:-1]
	except:
		return FAIL % "Invalid base64 string"
def b32(text,encode=False):
	import base64
	pattern = "^(?:[A-Z2-7]{8})*(?:[A-Z2-7]{2}={6}|[A-Z2-7]{4}={4}|[A-Z2-7]{5}={3}|[A-Z2-7]{7}=)?$"
	text = bytes(text,"utf-8")
	if encode:
		return SUCCESS % base64.b32encode(text).decode("utf-8")
	try:
		return SUCCESS % str(base64.b32decode(text))[2:-1]
	except:
		return FAIL % "Invalid base64 string"		
def b85(text,encode=False):
	import base64
	text = bytes(text,"utf-8")
	if encode:
		return SUCCESS % base64.a85encode(text).decode("utf-8")
	try:
		return SUCCESS % str(base64.a85decode(text))[2:-1]
	except:
		return FAIL % "Invalid base85 input"
def ascii85(text,encode=False):
	import base64
	text = bytes(text,"utf-8")
	if encode:
		return SUCCESS % base64.b85encode(text).decode("utf-8")
	try:
		return SUCCESS % str(base64.b85decode(text))[2:-1]
	except:
		return FAIL % "Invalid base85 input"
def b58(text,encode=False):
	import base58
	if encode:
		return SUCCESS % base58.b58encode(text).decode("utf-8")
	try:
		return SUCCESS % str(base58.b58decode(text))[2:-1]
	except:
		return FAIL % "Invalid base58 input"
def rot47(text):
	import rot47
	return SUCCESS % rot47.rot47(text)
def morse(text,seperator='/',encode=False):
	import morse
	try:
		if encode:
			return SUCCESS % morse.morseencode(text,seperator)
		return SUCCESS % morse.morsedecode(text,seperator)
	except Exception as e:
		return FAIL % str(e)
def malbolge(text):
	from malbolge import malbolge
	try:
		return SUCCESS % malbolge(text)
	except Exception as e:
		return FAIL % str(e)
def xor(text,key,textType,keyType):
	result = ''
	try:
		if textType=="Hex":
			text = bytes.fromhex(text).decode('latin-1')
		if keyType=="Hex":
			key = bytes.fromhex(key).decode('latin-1')
		if textType=="Base64":
			import base64
			text = base64.b64decode(text).decode('latin-1')
		if keyType=="Base64":
			import base64
			key = base64.b64decode(key).decode('latin-1')
		for i,t in enumerate(text):
			result += chr(ord(t) ^ ord(key[i%len(key)]))
		return SUCCESS % str(bytes(result,'latin-1'))[2:-1]
	except Exception as e:
		return FAIL % str(e)

def xorBrute(text,textType):
	try:
		if textType=="Hex":
			text = bytes.fromhex(text).decode('utf-8')
		if textType=="Base64":
			import base64
			text = base64.b64decode(text).decode('utf-8')
	except Exception as e:
		return FAIL % text


	result = ''
	for i in range(256):
		result += '<b>Key %2x:</b> ' % i
		plain = ''
		for t in text:
			plain += chr(ord(t) ^ i)
		result += str(bytes(plain,'latin-1'))[2:-1] + '\n'
	return SUCCESS % result.replace("\n","<br>")

def factor_n(n):
	from factordb.factordb import FactorDB
	f = FactorDB(n)
	f.connect()
	if f.get_status() == "FF":
		factors = f.get_factor_list()
		return factors
	# from primefac import primefac
	# factors = list([int(i) for i in primefac(n)])
	# if len(factors) == 2:
	# 	return factors[0],factors[1]
	# else:

def decryptRSAValues(values,delta=.292,m=4):
	import re
	from Crypto.Util.number import long_to_bytes,isPrime,inverse
	values = values.replace(" ",'')
	decimal = re.findall(".=[0-9]+",values)
	element = {}
	for dec in decimal:
		dec = dec.split("=")
		element[dec[0]] = int(dec[1])
	hexadecimal = re.findall(".=0x[0-9a-fA-F]+",values)
	for h in hexadecimal:
		h = h.split("=")
		element[h[0]] = int(h[1],16)
	keys = element.keys()
	if 'd' in keys:
		if 'n' in keys and 'c' in keys:
			# return decryptRSA(element['n'],element['c'],needFactor=False,d=element['d'])
			d = element['d']
			c = element['c']
			n = element['n']
			m = pow(c,d,n)
			result = [["Message","<b>"+str(long_to_bytes(m))[2:-1]+"</b>"],["m =",str(m)]]
			if 'e' in keys:
				e = element['e']
				from recover_factors import recover
				factors = recover(n,e,d)
				result.append(["Factors =",str(factors)[1:-1]])
			result.append(["d =",str(d)])
			return multiResult(*result)
		else:
			return FAIL % "d without n and c cannot be decrypt!"
	if 'e' not in keys or 'c' not in keys:
		return FAIL % "e and c values were not entered!"
	else:
		e = element['e']
		c = element['c']
		if 'n' not in keys:
			if 'p' not in keys or 'q' not in keys:
				return FAIL % "n or p,q values were not entered!"
			else:
				p = element['p']
				q = element['q']
				n = p*q
				phi = (p-1)*(q-1)
				d = inverse(e,phi)
				m = pow(c,d,n)
				return multiResult(["Message","<b>"+str(long_to_bytes(m))[2:-1]+"</b>"],["m =",str(m)],["Factors =",str([p,q])[1:-1]],["d =",str(d)])
				# return decryptRSA(p*q,c,e,False,p,q)
		else:
			n = element['n']
			try:
				d = 0
				import gmpy2
				cube_root = gmpy2.iroot(c,3)
				if e == 3 and cube_root[1] == True:
					return multiResult(["Message","<b>"+str(long_to_bytes(cube_root[0]))[2:-1]+"</b>"])
				if e > 65537:
					from rsa_wiener.RSAwienerHacker import hack_RSA
					d = hack_RSA(e,n)
					if d == 0:
						from boneh_durfee import attack
						try:
							delta = float(delta)
							m = int(m)
						except ValueError:
							return FAIL % "delta require float, m require integer!"
						d = attack(n,e,delta,m)
				if d != 0:
					from recover_factors import recover
					factors = recover(n,e,d)
				else:
					if isPrime(n):
						phi = n-1
						factors = [None]
					else:
						factors = factor_n(n)
						if len(factors) == 2:
							p,q = int(factors[0]),int(factors[1])
							if p != q:
								phi = (p-1) * (q-1)
							else:
								phi = p * (p-1)
						else:
							phi = 1
							for f in factors:
								phi *= (f-1) 
				
					d = inverse(e,phi)
				m = pow(c,d,n)
				return multiResult(["Message","<b>"+str(long_to_bytes(m))[2:-1]+"</b>"],["m =",str(m)],["Factors =",str(factors)[1:-1]],["d =",str(d)])
			except Exception as e:
				#return FAIL % str(e)	
				return FAIL % "Fail to factorize n!!"
			# try:
			# 	assert(n == p*q)
			# 	return decryptRSA(n,c,e,False,p,q)
			# except:
			# 	return FAIL % "p x q not equal n!!!"
def gcd(a,b):
	from Crypto.Util.number import GCD
	try:
		return SUCCESS % str(GCD(int(a),int(b)))
	except:
		return FAIL % "Please enter 2 numbers!"
def number_to_ascii(text,mode,seperator=''):
	import numtoascii
	try:
		return SUCCESS % numtoascii.convert(text, seperator, mode)
	except Exception as e:
		return FAIL % str(e)
def ocr(file):
	from google.cloud import vision
	import html
	try:
		client = vision.ImageAnnotatorClient()
		content = file.read()
		image = vision.types.Image(content=content)
		response = client.text_detection(image=image)
		texts = response.text_annotations
		result = html.escape(texts[0].description)
		return SUCCESS % result.replace("\n","<br>")
	except Exception as e:
		return FAIL % str(e)
def zsteg(file):
	from zsteg import extract
	try:
		open("test.png",'wb').write(file.read())
		return SUCCESS % extract()
	except Exception as e:
		return FAIL % str(e)
def strings(file):
	from strings import extract
	try:
		open("test.string",'wb').write(file.read())
		return SUCCESS % extract()
	except Exception as e:
		return FAIL % str(e)
def jsteg(file):
	from jsteg import extract
	try:
		open("test.jpg",'wb').write(file.read())
		return SUCCESS % extract()
	except Exception as e:
		return FAIL % str(e)
	
def autoCrypto(text,ignore):
	func = [caesar,b32,b58,b64,rot47,morse,b85,ascii85,malbolge]
	result = ''
	if ignore:
		for f in func:
			r = f(text)
			if 'Error' not in r:
				result += r.replace("Result",f.__name__).replace("resulttext",f.__name__)
	else:
		for f in func:
			result += f(text).replace("Result",f.__name__).replace("resulttext",f.__name__)
	return result
def letternum(text,seperator=' ',encode=False):
	result = ''
	try:
		if encode:
			text = text.upper()
			for t in text:
				result += str(ord(t)-0x40) + seperator
			result = result[:-1]
		else:
			text = text.split(seperator)
			for t in text:
				result += chr(int(t)+0x40)
		return SUCCESS % result
	except Exception as e:
		return FAIL % str(e)
def stegsolve(file):
	from stegsolve import processImage
	from os import system
	import time
	try:
		images = processImage(file)
		result = ''
		for i in images.keys():
			for j in images[i]:
				result += f'<img style="max-width: calc(30% - 10px);max-height: 400px;" src="images/{j}?{time.time()}">'

		return SUCCESS % result
	except:
		return FAIL % "Fail to convert image"
def fernet(text,key="password",encode=False):
	from cryptography.fernet import Fernet
	text = bytes(text,"utf-8")
	if encode:
		import os
		import base64
		from cryptography.hazmat.primitives import hashes
		from cryptography.hazmat.backends import default_backend
		from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
		salt = os.urandom(16)
		kdf = PBKDF2HMAC(
		    algorithm=hashes.SHA256(),
		    length=32,
		    salt=salt,
		    iterations=100000,
		    backend=default_backend()
		)
		key = bytes(key,"utf-8")
		key = base64.urlsafe_b64encode(kdf.derive(key))
		f = Fernet(key)
		token = f.encrypt(text)
		return multiResult(["Key",str(key)[2:-1]],["Token",str(token)[2:-1]])
	else:
		try:
			f = Fernet(key)
			text = f.decrypt(text)
			return SUCCESS % str(text)[2:-1]
		except:
			return FAIL % "Invalid Key or Token!"
def webSource(url):
	import requests
	import urllib3
	import html
	urllib3.disable_warnings()
	try:
		result = requests.get(url,verify=False).text
		return SUCCESS % f'<textarea class="form-control col-xl-6" id="htmltext" rows="20">{result}</textarea>'
	except Exception as e:
		return FAIL % str(e)
def pythonScript(code,password):
	from hashlib import sha512
	if sha512(bytes(password,"utf-8")).hexdigest() == "dde0478e9f248d9f3f9123d91f18cb31b2048211a4d46118efcc285ed39d493fafb30155a90a77082c4542d895e6115d5486b9497d676b6dc28b6cbf0af6b7f8":
		from subprocess import Popen, PIPE
		import os
		env = os.environ
		# https://github.com/Gallopsled/pwntools/issues/818
		env["TERM"] = "linux"
		env["TERMINFO"] = "/etc/terminfo"
		open("python_script/test.py",'w').write(code)
		process = Popen(['python', 'python_script/test.py'], stdout=PIPE, stderr=PIPE,env=env)
		stdout, stderr = process.communicate()
		return multiResult(["Output",str(stdout.replace(b"\n",b'<br>'))[2:-1]],["Error",str(stderr.replace(b"\n",b'<br>'))[2:-1]])
	else:
		return FAIL % "Only SKR member are allow to use this feature =("
def hastad(values):
	import re
	values = values.replace(" ",'')
	values = re.findall(".=[0-9]+",values)
	element = {}
	for v in values:
		v = v.split("=")
		element[v[0]] = int(v[1])
	keys = element.keys()
	n_list = []
	c_list = []
	for k in keys:
		if k.startswith("n"):
			n_list.append(element[k])
		elif k.startswith("c"):
			c_list.append(element[k])
	if len(n_list) != len(c_list):
		return FAIL % "Number of n must equal number of c"
	try:
		import hastad
		m = hastad.hastad_unpadded(c_list,n_list,len(c_list))
		return SUCCESS % m
	except Exception as e:
		return FAIL % str(e)
def ilspy(f):
	from ilspy import extract
	try:
		open("test.exe",'wb').write(f.read())
		return SUCCESS % f'<textarea class="form-control col-xl-6" id="htmltext">{extract()}</textarea>'
	except Expection as e:
		return FAIL % str(e)
def uncompyle(f):
	from uncompyle import extract
	try:
		open("test.pyc",'wb').write(f.read())
		return SUCCESS % f'<textarea class="form-control col-xl-6" id="uncompyletext">{extract()}</textarea>'
	except Expection as e:
		return FAIL % str(e)

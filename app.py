import json
import threading
import os
from werkzeug import secure_filename
import speech_recognition as sr
import numpy as np
from scipy.io import wavfile
import requests
from flask_restful import Resource, Api, request
from flask import Flask,render_template,url_for
from flask_cors import CORS, cross_origin
import wave
import soundfile as sf


app=Flask(__name__,template_folder='template')
api = Api(app)
CORS(app, support_credentials=True)
base_path = os.path.dirname(__file__)
pathname = os.path.dirname(os.getcwd())
DIR_EXEC = os.path.abspath(os.getcwd())


@app.route("/", methods = ["GET", "POST"])
def test():
	return render_template("speechfile.html")


@app.route("/uploader", methods = ["GET", "POST"])
def isgspeech():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		path_of_file = os.path.join(DIR_EXEC,str(f.filename))
		r = sr.Recognizer()
		data, samplerate = sf.read(path_of_file) 
		y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
		wavfile.write(path_of_file, 8000, y)
		response = ''
		with sr.AudioFile(path_of_file) as source:
			audio = r.record(source)
			response = r.recognize_google(audio)
		return response
		

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)

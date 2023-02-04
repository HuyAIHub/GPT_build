#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-*-coding:gb2312-*-
from flask import Flask, request, jsonify, render_template, render_template_string, redirect
import time
# import imp
import sys
import json
from text_process import text_process
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def process_1():
    if request.method == 'GET':
        return render_template('home.html')        
    if request.method == 'POST':        
        text = request.form['messageText']
        text=text.lower()
        result=text_process(text)
        return jsonify({'answer':result})
        # return render_template('home.html',answer=result)

@app.route('/error')

def error():
    return render_template('error.html')        
    # if request.method == 'POST':        
        # text = request.form['messageText']
        # return render_template('submit')
        

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5000)
    

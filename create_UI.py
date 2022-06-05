# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:28:47 2020

@author: DELL
"""
#--------------------------------------------------------------------------
import io 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from base64 import b64encode
from flask import Flask,render_template,request
from pandas import read_csv
from matplotlib import pyplot as plt
#--------------------------------------------------------------------------
def plotting(p_data,data_selected):
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111)
    ax.set(xlabel='Reference',ylabel=data_selected,xlim=(0,100),ylim=(0,100))
    ax.scatter(range(100),p_data)
    return fig
#--------------------------------------------------------------------------    
def plot_data(data_selected,m):
    if(data_selected=='Data-A'):
        p_data=m[:,1]
    elif(data_selected=='Data-B'):
        p_data=m[:,2]
    else:
        p_data=m[:,3]
    fig=plotting(p_data,data_selected)
    output = io.BytesIO()    
    FigureCanvas(fig).print_png(output)
    pic=output.getvalue()
    encoded = b64encode(pic).decode("utf-8")
    return encoded
#----------------------------------------------------------------------------
a=read_csv("Family_1.csv")
a=a.values
b=read_csv("Family_2.csv")
b=b.values
app=Flask(__name__)
#---------------------------------------------------------------------------
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/data/")
def select_file():
    return render_template('select.html')

@app.route("/data/fam1/",methods=["POST"])
def dataselect1():
    data_selected = request.form['data']
    p_data=plot_data(data_selected,a)
    return render_template('figures.html',title="Family-1 : "+data_selected,
                           image=p_data)

@app.route("/data/fam2/",methods=["POST","GET"])
def dataselect2():
    data_selected = request.form['data']
    p_data=plot_data(data_selected,b)
    return render_template('figures.html',title="Family-2 : "+data_selected,
                           image=p_data)
#------------------------------------------------------------------------------
     
if __name__=='__main__':
    app.run()
#-----------------------------------------------------------------------------

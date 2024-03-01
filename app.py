from flask import Flask,request,url_for,render_template,jsonify
import numpy as np
import pickle
import json
from utils import get_predicted_price_class
from config import PORT_NUMBER

app = Flask(__name__)


@app.route("/home",methods = ["GET","POST"])
def home():

    return render_template("index.html")



@app.route("/predicted_price_class",methods = ["GET","POST"])
def predicted_price_class():
    result  = None
    if request.method == "POST":
        data = request.form
        battery_power = eval(data["battery_power"])
        blue = eval(data["blue"])
        clock_speed = eval(data["clock_speed"])
        dual_sim = eval(data["dual_sim"])
        fc = eval(data["fc"])
        four_g = eval(data["four_g"])
        int_memory = eval(data["int_memory"])
        m_dep = eval(data["m_dep"])
        mobile_wt = eval(data["mobile_wt"])
        n_cores = eval(data["n_cores"])
        pc = eval(data["pc"])
        px_height = eval(data["px_height"])
        px_width = eval(data["px_width"])
        ram = eval(data["ram"])
        sc_h = eval(data["sc_h"])
        sc_w = eval(data["sc_w"])
        talk_time = eval(data["talk_time"])
        three_g = eval(data["three_g"])
        touch_screen = eval(data["touch_screen"])
        wifi = eval(data["wifi"])
    
        result = get_predicted_price_class(battery_power, blue, clock_speed, dual_sim, fc,four_g, int_memory, m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi)
        price = {0: '10-16k', 1: '18-24k', 2: '25-30k', 3: '30-35k'}

    return render_template("index.html",prediction = result)





    # f"{price[result]}")
    # return jsonify({"response":"successful",
    #                 "result":f"Predicted price of mobile is : {result}"})



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=PORT_NUMBER,debug=False)
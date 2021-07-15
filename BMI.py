
from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route('/',methods=['post'])
def bmi():
	data=request.get_json()
	weight=data['weight'] #in kg
	height=data['height'] #in m
	res=(int(weight)/(float(height)*float(height)))
	if res<20:
		return(jsonify({"bmi (you are lean) ":res}))
	elif res>25:
		return(jsonify({"bmi (you are fat) ":res}))
	else :			
		return(jsonify({"bmi (you are normal) ":res}))

@app.route('/details',methods=['get'])
def abx():
	return("hello")

app.run(port=2000)












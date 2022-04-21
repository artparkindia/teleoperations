from flask import Flask, abort, render_template, request
from flask_cors import CORS
import sys, getopt
import netifaces as nif
import getmac
import time
import toml
import json

app = Flask(__name__)
CORS(app)

argv = sys.argv[1:]
ip_addr = "0.0.0.0"
valid_mac = ['10:ec:81:e8:02:a3']
mac = "00:00:00:00:00:00"

if(len(argv)>0):
	try:
		opts, args = getopt.getopt(argv, "w:f:")
		_, ip_addr = opts[0]
		_, follow_me = opts[1]
		follow_me = int(follow_me)
	except Exception as e:
		print("error :", e)
		sys.exit(0)

@app.before_request
def remote_auth():
	global mac
	ip =  request.remote_addr
	time.sleep(1)
	mac = getmac.get_mac_address(ip=ip)
	print('mac is valid:', mac in valid_mac)

@app.route('/')
@app.route('/drive')
def index():
	if(True or mac in valid_mac):
		if(follow_me == 0):return render_template("drive.html", ws=ip_addr)
		else:return render_template("follow_me.html", ws=ip_addr)
	else:return render_template("block.html")

@app.route('/booktrip')
def booktrip():
	if(True or mac in valid_mac and follow_me == 0):
		location_data = toml.load('location.toml')['location']
		return render_template("booktrip.html", ws=ip_addr, location_data=location_data)
	else:return render_template("block.html")
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
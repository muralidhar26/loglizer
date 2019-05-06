import requests
import json

# URL
url = 'http://localhost:5000/api'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# Change the value of experience that you want to test
data_normal = {
    "data": [
		[
			0.0,
			0.0418629145,
			0.0,
			0.0,
			0.0,
			0.0,
			-2.51954013e-12,
			0.0,
			0.0426294917,
			0.0,
			-0.75586204,
			0.0,
			0.0,
			0.0426294917
		]
	]
}
data_anamoly = {
    "data": [
		[
            0.00000000e+00,
            4.18629145e-02,
            0.00000000e+00,
            0.00000000e+00,
            0.00000000e+00,
            0.00000000e+00,
            -2.51954013e-12,
            0.00000000e+00,
            4.26294917e-02,
            0.00000000e+00,
            -7.55862040e-12,
            0.00000000e+00,
            0.00000000e+00,
            4.26294917e-02
		]
	]
}

data_json = json.dumps(data_anamoly)
print(data_json)

r = requests.post(url,data_json,headers)
print(r.text)
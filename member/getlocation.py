import requests

def getdata(origin, destination, mode="walking"):
	destinations = "|".join(destination)
	result = []
	data = requests.get(
		"https://maps.googleapis.com/maps/api/distancematrix/json?origins=" +
		origin + "&destinations=" + destinations + "&mode=" + mode + "&key=AIzaSyD68CJlpEQG9PvVvk95liARUfUuSfnSTy0").json()

	for x in range(len(destination)):
		origin_address = str(data["origin_addresses"][0])
		dest_address = str(data["destination_addresses"][x])
		duration = (data["rows"][0]["elements"][x]['duration']["text"])
		distance = (data["rows"][0]["elements"][x]['distance']["text"])

		if distance.endswith(" m"):
			distance = str(float(distance.split(" m")[0]) * 0.001) + " km"

		result.append((origin_address, dest_address, duration, distance))

	return result

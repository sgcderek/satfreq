import os
import json

JSON_PATH = "json/"

sat_filenames = os.listdir(JSON_PATH)
output_json = []

for sat_filename in sat_filenames:
    with open(JSON_PATH + sat_filename, "r") as sat_file:
        sat_json = json.load(sat_file)
        output_json.append(sat_json)

with open("satfreq.json", "w") as output_file:
    output_file.write(json.dumps(output_json))

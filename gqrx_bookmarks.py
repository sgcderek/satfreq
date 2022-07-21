import os
import json

csv_out = "satfreq; #58A6FF" + os.linesep + os.linesep

with open("satfreq.json", "r") as sat_file:
    sat_json = json.load(sat_file)
    for sat in sat_json:
        for downlink in sat["downlinks"]:
            name = sat["name"] + " " + downlink["name"]
            csv_out += str(downlink["frequency"]) + "; " + name + "; Demod Off; 0; satfreq" + os.linesep
            
with open("gqrx_bookmarks.csv", "w") as output_file:
    output_file.write(csv_out)

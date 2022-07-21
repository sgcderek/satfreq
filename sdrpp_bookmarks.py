import json

bookmarks_json = {
    "bookmarkDisplayMode": 1,
    "lists": {
        "satfreq": {
            "bookmarks": {},
            "showOnWaterfall": True
        }
    },
    "selectedList": "satfreq"
}

with open("satfreq.json", "r") as sat_file:
    sat_json = json.load(sat_file)
    for sat in sat_json:
        for downlink in sat["downlinks"]:
            name = sat["name"] + " " + downlink["name"]
            bookmarks_json["lists"]["satfreq"]["bookmarks"][name] = { "bandwidth": 0, "frequency": downlink["frequency"], "mode": 7 }

with open("sdrpp_bookmarks.json", "w") as output_file:
    output_file.write(json.dumps(bookmarks_json, indent=4))

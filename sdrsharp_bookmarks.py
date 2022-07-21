import os
import json
import xml.dom.minidom as minidom

root = minidom.Document()
xml = root.createElement("ArrayOfMemoryEntry")
xml.setAttribute("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
xml.setAttribute("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")

with open("satfreq.json", "r") as sat_file:
    sat_json = json.load(sat_file)
    for sat in sat_json:
        for downlink in sat["downlinks"]:
            bookmark = root.createElement("MemoryEntry")

            val = root.createElement("IsFavourite")
            val.appendChild(root.createTextNode("false"))
            bookmark.appendChild(val)
            val = root.createElement("Name")
            val.appendChild(root.createTextNode(sat["name"] + " " + downlink["name"]))
            bookmark.appendChild(val)
            val = root.createElement("GroupName")
            val.appendChild(root.createTextNode("satfreq"))
            bookmark.appendChild(val)
            val = root.createElement("Frequency")
            val.appendChild(root.createTextNode(str(downlink["frequency"])))
            bookmark.appendChild(val)
            val = root.createElement("DetectorType")
            val.appendChild(root.createTextNode("RAW"))
            bookmark.appendChild(val)
            val = root.createElement("Shift")
            val.appendChild(root.createTextNode("0"))
            bookmark.appendChild(val)
            val = root.createElement("FilterBandwidth")
            val.appendChild(root.createTextNode("0"))
            bookmark.appendChild(val)

            xml.appendChild(bookmark)

with open("sdrsharp_bookmarks.xml", "w") as output_file:
    output_file.write("<?xml version=\"1.0\"?>" + os.linesep)
    output_file.write(xml.toprettyxml())

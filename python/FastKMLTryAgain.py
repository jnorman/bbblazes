# Python script to get coordinates from KML file and create a google maps script for polyline
from fastkml import kml
import re
import polyline

with open('../doc.kml', 'r') as myKML:
	docInput = myKML.read()#.replace('\n', '')
#print docInput;




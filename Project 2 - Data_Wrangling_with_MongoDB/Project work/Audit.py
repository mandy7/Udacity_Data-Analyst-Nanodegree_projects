import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import json
import pandas as pd
import os

os.chdir('/Users/madua/Desktop')

filename = 'newdelhi.osm'
osm_file = open(filename, 'r')

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

street_types = defaultdict(set)
postcodes = []
cities = []


expected = [ ] #'Avenue', 'Street', 'Road', 'Boulevard', 'Circle', 'Center', 'Court', 'Drive', 'Parkway', 'Square', 'Way']
ignore = ['Northeast',  'NE', 'Southeast', 'SE', 'East', 'Northwest', 'NW', 'West', 'North']

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            if street_type in ignore:
                street_type = street_name.split()[-2]
            street_types[street_type].add(street_name)
    
    #for k in keys:
    #    v = d[k]
    #    print "%s: %d" % (k, v)
    
def audit_postcode(postcodes, code):
    postcodes.append(code)
        
def audit_city(cities, city):
    cities.append(city)
    
            
def is_street_name(elem):
    return (elem.attrib['k'] == 'addr:street')
    
def is_postal_code(elem):
    return (elem.attrib['k'] == 'addr:postcode')
    
def is_city(elem):
    return (elem.attrib['k'] == 'addr:city')
    
def audit():
    for event, elem in ET.iterparse(osm_file, events=('start',)):
        if elem.tag == "node" or elem.tag == "way" or elem.tag == "relation":
            for tag in elem.iter('tag'):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
                if is_postal_code(tag):
                    audit_postcode(postcodes, tag.attrib['v'])
                if is_city(tag):
                    audit_city(cities, tag.attrib['v'])
    return dict(street_types), set(postcodes), set(cities)

         
streets, codes, cities = audit()

for k,v in streets.iteritems():
    streets[k] = list(v)
    
codes = list(codes)

cities = list(cities)

#output = json.dumps(streets)

with open('newdelhi_streets_data.json', 'w') as f: 
    f.write(json.dumps(streets, indent=2)+"\n")

with open('newdelhi_zipcodes_data.json', 'w') as f: 
    f.write(json.dumps(codes, indent=2)+"\n")

with open('newdelhi_city_data.json', 'w') as f: 
    f.write(json.dumps(cities, indent=2)+"\n")

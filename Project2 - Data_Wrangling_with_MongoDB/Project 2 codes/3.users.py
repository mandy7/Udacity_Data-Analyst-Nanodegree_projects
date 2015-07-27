# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pprint

import os
#Set the proper current working directory
os.getcwd()
os.chdir('C:/Users/madua/Project2')

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        try:
            users.add(element.attrib['uid'])
        except KeyError:
            pass
        element.clear() #to clear memory
    return users

users = process_map('GVRD - Vancouver - OSM XML Raw.osm')
pprint.pprint(users)
#RESULT set([])
#no users have contributed
#however attributed, created_by, and source may have some useful information by examining the OSM file

import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
"""
Your task is to wrangle the data and transform the shape of the data
into the model we mentioned earlier. The output should be a list of dictionaries
that look like this:
{
"id": "2406124091",
"type: "node",
"visible":"true",
"created": {
          "version":"2",
          "changeset":"17206049",
          "timestamp":"2013-08-03T16:43:42Z",
          "user":"linuxUser16",
          "uid":"1219059"
        },
"pos": [41.9757030, -87.6921867],
"address": {
          "housenumber": "5157",
          "postcode": "60625",
          "street": "North Lincoln Ave"
        },
"amenity": "restaurant",
"cuisine": "mexican",
"name": "La Cabana De Don Luis",
"phone": "1 (773)-271-5176"
}
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
colon_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
address = re.compile(r'^addr:')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

mapping = { "St": "Street",
            "Rd”: ”Road",
            "Nr”: “Near",
            "Ave.": "Avenue",
            "NH”: “National Highway",
            "No”: “number",
            "Rd": "Road",
            "Dr": "Drive",
            }

oddities = {'Udhyog’: ‘Udyog’, 
            'G T road’:  ‘GT road’, 
            'Pritampura’: ‘Pitampura’}

city = {'Pratap Colony, Siraspur, Delhi’ :’Siraspur',
        'Badli Industrial Area, Badli, Delhi’: ‘Badli',
        'Naya Band, Khera': 'Khera',
        'Sector- 10, Rohini, Delhi’: "Rohini',
        'Sector- 10, Rohini, Delhi’: "Rohini'
        'Hira Colony, Siraspur, Delhi’: "Siraspur'}

def is_street_name(elem):
    return (elem == 'addr:street')

def is_postal_code(elem):
    return (elem == 'addr:postcode')

def is_city(elem):
    return (elem == 'addr:city')

def update_name(name, map=mapping, odd=oddities):   
    if name in odd.keys():
        new_name = odd[name]
        return new_name
       
    name_lst = name.split()
    for i,nm in enumerate(name_lst):
        if nm in map.keys():
            name_lst[i] = map[nm]
    new_name = " ".join(name_lst)
    return new_name



def shape_element(element):
    node = {}
    i = 0
    if element.tag == "node" or element.tag == "way" :
        refs = []
        for tag in element.iter():
#            print tag.tag
            created = {}
            pos = []
#            refs = []
            addr = {}
            for k,v in tag.attrib.iteritems():
#                print k,v
                node['type'] = element.tag
                if problemchars.search(k):
                    break
                elif colon_colon.search(k):
                    break
                elif k in CREATED:
                    created[k] = v
                elif (k=='lat') or (k=='lon'):
                    pos.append(float(v))
                    node['pos'] = pos[::-1] #.reverse() 
                elif k == 'ref':
                    refs.append(v)
                    node['node_refs'] = refs
                elif (k=='k'): 
                    key = v
                    node[key] = ''
                elif (k=='v'):
                    value = v
                    node[key] = value
                else:
                    node[k] = v
            if created: 
                node['created'] = created
            if addr:
                node['address'] = addr
        to_remove = []
        for item in node:
            if colon_colon.search(item):
                to_remove.append(item)
        if to_remove:
            for term in to_remove:
                del node[term]
        addr_remove = []
        for item in node:
            if address.search(item):
                # fix postal codes
                if is_postal_code(item):
                    if node[item].isalpha():
                        addr[item[6:]] = ''
                    else:    
                        addr[item[6:]] = node[item][0:6]
            
                # fix city names for those
                    if node[item] in city.keys():
                        addr[item[5:]] = city[ node[item] ]
                        address_lst = node[item].split()
                        addr['housenumber'] = address_lst[0]
                        streetname = " ".join(address_lst[1:])
                        addr['street'] = update_name(streetname)
                    else:
                        addr[item[5:]] = node[item].replace(', Neew Delhi', 'New Delhi')
                        addr[item[5:]] = node[item].replace(', Gaziabad', 'Ghaziabad')
                        addr[item[5:]] = node[item].replace(' UP', '')
                        addr[item[5:]] = node[item].replace('Uttar Pradesh', '')
                        addr[item[5:]] = node[item].replace('India', '')
                # fix street names based on 'mapping' and 'oddities' dicts
                elif is_street_name(item):
                    addr[item[5:]] = update_name(node[item])
                else:
                    addr[item[5:]] = node[item]
                addr_remove.append(item)
        if addr_remove:
            for term in addr_remove:
                del node[term]
        if addr:
            node['address'] = addr
        return node
    else:
        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data

def test():
    # NOTE: if you are running this code on your computer, with a larger dataset, 
    # call the process_map procedure with pretty=False. The pretty=True option adds 
    # additional spaces to the output, making it significantly larger.
    filename = 'newdelhi.osm'
    data = process_map(filename, False)
    #pprint.pprint(data)

#test()

if __name__ == "__main__":
    test()

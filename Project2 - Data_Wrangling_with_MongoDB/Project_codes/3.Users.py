import xml.etree.ElementTree as ET


def get_user(element):
    return 
    
def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        try:
            users.add(element.attrib['uid'])
        except KeyError:
            continue

    return users
    
users = process_map('newdelhi.osm')
print (len(users))

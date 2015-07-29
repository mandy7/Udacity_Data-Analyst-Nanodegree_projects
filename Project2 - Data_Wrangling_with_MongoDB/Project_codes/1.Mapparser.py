import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

def count_tags(filename):
    counts = defaultdict(int)
    for line in ET.iterparse(filename):
        current = line[1].tag
        counts[current] += 1
    return counts
    
tags = count_tags('newdelhi.osm')
pprint.pprint(tags)

# Result - {'bounds': 1,
# 'member': 26614,
# 'nd': 3330789,
# 'node': 2732250,
# 'osm': 1,
# 'relation': 6613,
# 'tag': 642591,
# 'way': 538752}

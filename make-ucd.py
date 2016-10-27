from xml.etree import ElementTree as ET
from collections import defaultdict

tree = ET.parse('ucd.all.flat.xml')

names = defaultdict(set)
blocks = {}

for char_tag in tree.findall("./{http://www.unicode.org/ns/2003/ucd/1.0}repertoire/{http://www.unicode.org/ns/2003/ucd/1.0}char"):
    try:
        cp = int(char_tag.attrib["cp"], 16)
    except KeyError:
        continue
    name_set = names[cp]
    name_set.add(char_tag.attrib["na1"])
    for alias in char_tag.findall("{http://www.unicode.org/ns/2003/ucd/1.0}name-alias"):
        name_set.add(alias.attrib["alias"])

for block_tag in tree.findall(".//{http://www.unicode.org/ns/2003/ucd/1.0}block"):
    name = block_tag.attrib["name"]
    blocks[name] = {
        "name": name,
        "start": int(block_tag.attrib["first-cp"], 16),
        "end": int(block_tag.attrib["last-cp"], 16),
    }

with open("unidata.py", "w", encoding="UTF-8") as outf:
    outf.write("names = {\n")
    for cp, names in sorted(names.items()):
        names = sorted(n for n in names if n)
        if names:
            outf.write("    %d: {%s},\n" % (cp, ", ".join(repr(n) for n in names)))
    outf.write("}\n")
    outf.write("blocks = {\n")
    for name, data in sorted(blocks.items()):
        outf.write("    %r: %r,\n" % (name, data))
    outf.write("}\n")
    
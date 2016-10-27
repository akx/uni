ucd.py: ucd.all.flat.xml
	python make-ucd.py
ucd.all.flat.xml: ucd.all.flat.zip
	unzip -f ucd.all.flat.zip
ucd.all.flat.zip:
	wget http://www.unicode.org/Public/UCD/latest/ucdxml/ucd.all.flat.zip

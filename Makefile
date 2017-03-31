ucd.py: ucd.all.flat.xml
	python3 make-ucd.py
ucd.all.flat.xml: ucd.all.flat.zip
	unzip -o ucd.all.flat.zip
	touch ucd.all.flat.xml
ucd.all.flat.zip:
	wget http://www.unicode.org/Public/10.0.0/ucdxml/ucd.all.flat.zip
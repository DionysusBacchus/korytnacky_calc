#Project Makefile
.PHONY: all clean doc
	
all: run 
clean: 
	rm -rf __pycache__ 
pack:
	zip -r ../../../../xkhrys00_xlebed12_xsikul15_xpavel39.zip ../../../../xkhrys00_xlebed12_xsikul15_xpavel39/ 
test: test_mathlib.py
	python3 test_mathlib.py
run: main.py
	python3 main.py
doc: Doxyfile
	doxygen Doxyfile
profile: profiling.py
	python3 profiling.py


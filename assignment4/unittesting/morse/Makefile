DOCS = docs
PLANTUML = java -jar ~/plantuml.jar

all: typecheck localtest unittest create_documentation create_uml

localtest:
	#python tests
	cat data/1.in | python3 main.py | diff - data/1.ans
	cat data/2.in | python3 main.py | diff - data/2.ans
	cat data/3.in | python3 main.py | diff - data/3.ans

	@echo "Local tests done."

unittest:
	pytest pal_unittest.py

	@echo "Unit tests done."

typecheck:
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict palindrome.py

	@echo "Type check done."

create_uml:
	$(PLANTUML) uml/Text.plantuml
	$(PLANTUML) uml/Morse.plantuml

	@echo "UML diagrams created and saved."

create_doc_dir:
	@mkdir -p $(DOCS)

create_documentation: create_doc_dir
	pdoc --force -o docs main.py palindrome.py
	pdoc --force --html -o docs main.py palindrome.py

	@echo "HTML documentation created and saved."
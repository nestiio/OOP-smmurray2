DOCS = docs
PLANTUML = java -jar ~/plantuml.jar

all: create_documentation create_uml typecheck localtest unittest

localtest:
	#python tests
	cat data/1.in | python3 main.py | diff - data/1.ans
	cat data/2.in | python3 main.py | diff - data/2.ans
	cat data/3.in | python3 main.py | diff - data/3.ans

	@echo "Local tests done."

unittest:
	coverage run -m pytest frac_hypothesistest.py
	@echo "Property tests done."	

	coverage run -m pytest frac_unittest.py
	@echo "Unit tests done."

	coverage html

typecheck:
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict frac.py

	@echo "Type check done."

create_uml:
	$(PLANTUML) uml/Frac.plantuml
	$(PLANTUML) uml/MixedFrac.plantuml
	$(PLANTUML) uml/ClassInteraction.plantuml

	@echo "UML diagrams created and saved."

create_doc_dir:
	@mkdir -p $(DOCS)

create_documentation: create_doc_dir
	pdoc --force -o docs main.py frac.py
	pdoc --force --html -o docs main.py frac.py

	@echo "HTML documentation created and saved."
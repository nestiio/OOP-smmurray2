DOCS = docs
PLANTUML = java -jar ~/plantuml.jar

all: typecheck localtest create_uml create_documentation

localtest:
	#python tests
	cat data/1.in | python3 main.py | diff - data/1.ans
	cat data/2.in | python3 main.py | diff - data/2.ans
	cat data/3.in | python3 main.py | diff - data/3.ans

	@echo "Local tests done."

typecheck:
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict polygon.py

	@echo "Type check done."

create_uml:
	$(PLANTUML) uml/polygon.plantuml
	$(PLANTUML) uml/point.plantuml
	@echo "UML diagrams created and saved."

create_doc_dir:
	@mkdir -p $(DOCS)

create_documentation: create_doc_dir
	pdoc --force -o docs main.py polygon.py
	pdoc --force --html -o docs main.py polygon.py
	@echo "HTML documentation created and saved."
DOCS = docs
PLANTUML = java -jar ~/plantuml.jar

all: create_documentation create_uml typecheck unittest

unittest:
	coverage run -m pytest hypothesis_testing.py
	@echo "Property tests done."	

	coverage run -m pytest unit_testing.py
	@echo "Unit tests done."

	coverage html

typecheck:
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict classes.py

	@echo "Type check done."

create_uml:
	$(PLANTUML) uml/TitleCost.plantuml
	$(PLANTUML) uml/ComparisonClass.plantuml
	#$(PLANTUML) uml/ClassInteraction.plantuml

	@echo "UML diagrams created and saved."

create_doc_dir:
	@mkdir -p $(DOCS)

create_documentation: create_doc_dir
	pdoc -o docs main.py classes.py
	
	@echo "HTML documentation created and saved."
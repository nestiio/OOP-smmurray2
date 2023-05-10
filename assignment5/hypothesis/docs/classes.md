Module classes
==============

Classes
-------

`ComparisonClass(titlecost: classes.TitleCost, cap: float)`
:   Constructor for the class ComparisonClass

    ### Methods

    `getCap(self) ‑> float`
    :   Getter function for the cap data member

    `getMin(self) ‑> float`
    :   Function which calculates and returns the minimum between the cost of the title and the cap for the cost

    `getTitleCost(self) ‑> classes.TitleCost`
    :   Getter function for the titlecost data member

    `setCap(self, newCap: float) ‑> None`
    :   Setter function for the cap data member

    `setTitleCost(self, newTitleCost: classes.TitleCost) ‑> None`
    :   Setter function for the titlecost data member

`TitleCost(title: str)`
:   Constructor for the class TitleCost

    ### Methods

    `getCost(self) ‑> float`
    :   Getter function for the cost data member

    `getTitle(self) ‑> str`
    :   Getter function for the title data member

    `setCost(self, newCost: float) ‑> None`
    :   Setter function for the cost data member

    `setTitle(self, newTitle: str) ‑> None`
    :   Setter function for the title data member
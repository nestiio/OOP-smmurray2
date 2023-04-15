Module cups
===========

Classes
-------

`CupDiameter(color: str, diameter: int)`
:   Solution ABC class for Kattis problems
    
    Constructor for CupDiameter

    ### Ancestors (in MRO)

    * cups.KattisCup
    * abc.ABC

`CupList()`
:   All the operations on a read-write sequence.
    
    Concrete subclasses must provide __new__ or __init__,
    __getitem__, __setitem__, __delitem__, __len__, and insert().
    
    Constructor for CupList

    ### Ancestors (in MRO)

    * collections.abc.MutableSequence
    * collections.abc.Sequence
    * collections.abc.Reversible
    * collections.abc.Collection
    * collections.abc.Sized
    * collections.abc.Iterable
    * collections.abc.Container

    ### Methods

    `append(self, cup: Union[CupDiameter, CupRadius]) ‑> None`
    :   Appends an item to the end of the list

    `insert(self, index: int, cup: Union[CupDiameter, CupRadius]) ‑> None`
    :   Inserts an item into the list

    `sort(self) ‑> None`
    :   Sort the list

`CupRadius(color: str, radius: int)`
:   Solution ABC class for Kattis problems
    
    Constructor for CupRadius

    ### Ancestors (in MRO)

    * cups.KattisCup
    * abc.ABC

`KattisCup(color: Any, number: Any)`
:   Solution ABC class for Kattis problems
    
    Constructor
    :param data_source: input data source object
    :return: None

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * cups.CupDiameter
    * cups.CupRadius

    ### Methods

    `getColor(self) ‑> str`
    :   Getter function for color

    `getRadius(self) ‑> int`
    :   Getter function for radius

    `setColor(self, newColor: str) ‑> None`
    :   Setter function for color

    `setRadius(self, newRadius: int) ‑> None`
    :   Setter function for radius
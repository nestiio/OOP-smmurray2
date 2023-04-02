Module frac
===========

Classes
-------

`Frac(numerator: int, denominator: int)`
:   Constructor for the class Frac

    ### Descendants

    * frac.MixedFrac

    ### Methods

    `getDenominator(self) ‑> int`
    :   Get function for the denominator

    `getNumerator(self) ‑> int`
    :   Get function for the numerator

    `printFrac(self) ‑> None`
    :   Print function for fraction data type

    `setDenominator(self, newDenominator: int) ‑> None`
    :   Set function for the denominator

    `setNumerator(self, newNumerator: int) ‑> None`
    :   Set function for the numerator

`MixedFrac(fraction: frac.Frac)`
:   Constructor for the class MixedFrac

    ### Ancestors (in MRO)

    * frac.Frac

    ### Methods

    `calculateWholeNumber(self) ‑> None`
    :   Calculate mixed fraction

    `getFrac(self) ‑> frac.Frac`
    :   Get function for the fraction

    `getWholeNumber(self) ‑> int`
    :   Get function for the numerator

    `printMixedFrac(self) ‑> None`
    :   Print function for the fraction

    `setFrac(self, fraction: frac.Frac) ‑> None`
    :   Set function for the fraction

    `setWholeNumber(self, wholeNumber: int) ‑> None`
    :   Set function for the whole number
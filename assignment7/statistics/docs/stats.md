Module stats
============

Classes
-------

`Nums(numNumbers: int, numbers: List[int])`
:   Nums Class
    
    Constructor

    ### Descendants

    * stats.Stats

    ### Methods

    `getNumNumbers(self) ‑> int`
    :   Gets min

    `getNumbers(self) ‑> List[int]`
    :   Gets max

    `setNumNumbers(self, min: int) ‑> None`
    :   Sets min

    `setNumbers(self, numbers: List[int]) ‑> None`
    :   Sets max

`Stats(nums: stats.Nums, case: int)`
:   Nums Class
    
    Constructor

    ### Ancestors (in MRO)

    * stats.Nums

    ### Methods

    `getCase(self) ‑> int`
    :   Gets case number

    `getMax(self) ‑> int`
    :   Calculates and returns max

    `getMin(self) ‑> int`
    :   Calculates and returns min

    `getNums(self) ‑> stats.Nums`
    :   Gets nums

    `printStats(self) ‑> None`
    :   Print Function

    `setCase(self, case: int) ‑> None`
    :   Sets case

    `setNums(self, nums: stats.Nums) ‑> None`
    :   Sets nums
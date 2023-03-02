Module polygon
==============

Classes
-------

`Point(x: int, y: int)`
:   Point Class
    
    Constructor

    ### Descendants

    * polygon.Polygon

    ### Methods

    `getX(self) ‑> int`
    :   Gets x coordinate

    `getY(self) ‑> int`
    :   Gets y coordinate

    `setX(self, x: int) ‑> None`
    :   Sets x coordinate

    `setY(self, y: int) ‑> None`
    :   Sets y coordinate

`Polygon(numPoints: int, points: List[int])`
:   Polygon Class
    - Inherits from point class
    - Size of points array must be even
    
    Constructor

    ### Ancestors (in MRO)

    * polygon.Point

    ### Methods

    `area(self) ‑> float`
    :   Finds the area of one convex polygon at a time
        - has an edge case for when i+1 goes past n

    `getNumPoints(self) ‑> int`
    :   Gets the number of points

    `getPoints(self) ‑> List[polygon.Point]`
    :   Gets points

    `setNumPoints(self, numPoints: int) ‑> None`
    :   Sets the number of points

    `setPoints(self, points: List[polygon.Point]) ‑> None`
    :   Sets points
from cups import CupDiameter
from cups import CupRadius
from cups import CupList

def main() -> None:
    """
    Main
    """
    cupList = CupList()

    n = int(input())
    for i in range(n): # take input
        cup = input().split()
        try:
            number = int(cup[0])
            color = cup[1]
            cupDiameter = CupDiameter(color, number)
            cupList.append(cupDiameter)
        except ValueError as e:
            number = int(cup[1])
            color = cup[0]
            cupRadius = CupRadius(color, number)
            cupList.append(cupRadius)

    # implement cupList.sort, somehow
    cupList.sort()
    for i in range(len(cupList)):
        print (cupList[i].getColor())


if __name__ == "__main__":
    main()

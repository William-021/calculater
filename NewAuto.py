ElementsAndTypes = {}  # Dictionary to store all the elements of the equation and their types
container={}

def saveToContainer(dictionary):
    for Element, Type in dictionary.items():
        container[Element] = Type

def returnAndEmptyContainer(dictionary):
    for Element, Type in container.items():
        dictionary[Element] = Type
    container.clear()

def transToDictionary(Equation):
    for i in Equation:
        try:
            float(i)
            ElementsAndTypes[i] = "number"
        except ValueError:
            ElementsAndTypes[i] = "unknown"
        if i=="+" or i=="-" or i=="*" or i=="/" or i=="=" or i=="^":
            ElementsAndTypes[i] = "operator"
        elif i=="#":
            ElementsAndTypes[i]="None"
        saveToContainer(ElementsAndTypes)
        
def searchForUnknowns():
    ListOfUnknowns = {}
    for Element, Type in ElementsAndTypes.items():
        if Type == "unknown":
            #ListOfUnknowns[Element].append(list(ElementsAndTypes.keys()).index(Element))
            while True:
                try:
                    ListOfUnknowns[Element] = list(ElementsAndTypes.keys()).index(Element)
                    if ElementsAndTypes[Element]=="unknown":
                        ElementsAndTypes[Element]="#"
                        break
                    
                except ValueError:
                    break

    print("Unknown elements found: {}".format(ListOfUnknowns))

    

transToDictionary("y=2x^2+4x+3+a")
searchForUnknowns()
print(ElementsAndTypes)

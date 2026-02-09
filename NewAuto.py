ElementsAndTypes = {}
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
        saveToContainer(ElementsAndTypes)
        
def searchForUnknowns():
    ListOfUnknowns = {}
    for Element, Type in ElementsAndTypes.items():
        if Type == "unknown":
            ListOfUnknowns[Element] = list(ElementsAndTypes.keys()).index(Element)
    print("Unknown elements found: {}".format(ListOfUnknowns))

    

transToDictionary("y=2x^2+4x+3+a")
searchForUnknowns()
print(ElementsAndTypes)

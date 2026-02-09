unknowns=[]
EquationElements=[]

def unknownOrNumber(value):
    if value=="+" or value=="-" or value=="*" or value=="/" or value=="=":
        return "operator"
    try:
        float(value)
        return "number"
    except ValueError:
        return "unknown"

# def save(unknown):
#     unknowns.append(unknown)

# def linearFunction(linear):
#     unknown_number_count = 1
#     for i in linear:
#         if unknownOrNumber(i) == "unknown":
#             if unknown_number_count == 1:
#                 x=i
#                 unknown_number_count += 1
#             elif unknown_number_count == 2:
#                 y=i
#         elif unknownOrNumber(i) == "number":

def translateEquation(Equation):          
    for i in Equation:
        if unknownOrNumber(i) == "unknown":
            unknowns.append(i)
        EquationElements.append(i)



translateEquation("y=2x+3")
print(unknowns)
print(EquationElements)
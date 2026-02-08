# def unknownOrNumber(value):
#     try:
#         float(value)
#         return "number"
#     except ValueError:
#         return "unknown"

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

def autoNaming():


def linearFunction(linear):
    for i in linear:
        if i == "x":
            
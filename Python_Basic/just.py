# our_pats = [
#     {
#         "animal_type": "cat",
#         "names": [
#             "Meowzer",
#             "Fluffy",
#             "Kit-Cat"
#         ]
#     },
#     {
#       "animal_type": "dog",
#         "names": [
#             "Spot",
#             "Bowser",
#             "Frankie"
#         ]
#     }
# ]
#
# for i in our_pats:
#     if i["animal_type"] == "cat":
#         print(i["animal_type"])

user: dict = {
    "full_name": None,
    "age": 0,
    "email": None
}

full_name: str = input("What is you full name? ")
# print(full_name.split())
if len(full_name.split()) == 2:
    user["full_name"] = full_name
    print(user)
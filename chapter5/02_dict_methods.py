marks = {
    "Aadi": 100,
    "Harry": 80,
    "Preet": 70,
    0: "Aadi"
}

# print(marks.keys())
# print(marks.items())
# print(marks.values())
# marks.update({"Harry": 99})
# print (marks)

print(marks.get("Aadi2")) # Prints None
print(marks["Aadi2"]) # returns an error
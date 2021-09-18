string = "she is beautiful and she is good singer"
print(string.replace(" ","_")) # to replace spaces with _
print(string.replace("is","was")) # to replace is with was
print(string.replace("is","was", 1)) # to replace only 1st is with was

print(string.find("is")) # to find position of is
pos_is1 = string.find("is")
pos_is2 = string.find("is", pos_is1 + 1)

print(pos_is2) # to find second is position without knowing 1st is position.
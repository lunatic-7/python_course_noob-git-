name, char = input("what is your name and chr. :").split(",") # comma seperated
print(len(name))
print(f"character count : {name.strip().lower().count(char.strip().lower())}")
# WASIF - wasif
#A - a
# " WASIF  " -----> "WASIF" -----> "wasif"
# " A " -----> "A" -----> "a"
# name.strip().lower().count(chr.strip().lower())
# chr.strip().lower()
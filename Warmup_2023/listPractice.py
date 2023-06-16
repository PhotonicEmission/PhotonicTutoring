# Take a set of names from the user, seperated by commas, and print each to its own line.

# input:
names="alice, bob, charlie"

# output:
# alice
# bob
# charlie

for name in names.split(","):
    print(name.strip())
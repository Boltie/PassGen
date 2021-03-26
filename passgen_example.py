from passgen import PassGen

# Assign a new PassGen object to 'pg' using parameters.
pg = PassGen(allow_dupes=True, count=2, length=18, sets_enabled="110")

""" Before generating a password, a check is made on 'sets_enabled' whereby
    if there are insufficient/too many values, it will be padded/trimmed.
    The value of '110' will be padded to '1101'. """

# 1
pw = pg.get_single()
print("1 - " + pw) # 1 18-digit password printed to console/terminal. Duplicates allowed.

# 2
pw = pg.get_multiple() # Count of 2 was set at initialisation.
for s in pw: print("2 - " + s) # 2 18-digit passwords printed to console/terminal. Duplicates allowed.

# 3
pw = pg.get_multiple(False, 5) # Count of 5 provided - the PassGen object count (pg.count) is also updated to 5.
for s in pw: print("3 - " + s) # 5 18-digit passwords printed to console/terminal. Duplicates NOT allowed.

# 4
pw = pg.get_multiple() # 'get_multiple()' defaults to the PassGen object count unless a new count is provided.
for s in pw: print("4 - " + s) # 5 18-digit passwords printed to console/terminal. Duplicates NOT allowed.

# 5
pg.count = 2 # PassGen object count updated to 2.
pw = pg.get_multiple()
for s in pw: print("5 - " + s) # 2 18-digit passwords printed to console/terminal. Duplicates NOT allowed.

# 6
pw = pg.get_multiple(length=8, sets_enabled="00") # The provided 'sets_enabled' will disable the lower and upper sets.
for s in pw: print("6 - " + s) # 2 8-digit passwords printed to console/terminal. Duplicates NOT allowed. Only numbers and punctuation used.

#7
pw = pg.get_single(True, 24) # Generate password providing a length of 24.
print("7 - " + pw) # 1 24-digit password printed to console/terminal. Duplicates allowed. Only numbers and punctuation used.

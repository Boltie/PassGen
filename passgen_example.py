from passgen import PassGen

# Assign a new PassGen object to 'pg' using parameters.
pg = PassGen(count=2, length=18, sets_enabled="110")

""" Before generating a password, a check is made on 'sets_enabled' whereby
    if there are insufficient/too many values, it will be padded/trimmed.
    The value of '100' will be padded to '1101'. """

# 1
pw = pg.get_single()
print("1 - " + pw) # 1 password printed.

# 2
pw = pg.get_multiple() # Count of 2 was set upon initialisation.
for s in pw: print("2 - " + s) # 2 passwords printed.

# 3
pw = pg.get_multiple(5) # Count of 5 provided - the PassGen object count (pg.count) is also updated to 5.
for s in pw: print("3 - " + s) # 5 passwords printed.

# 4
pw = pg.get_multiple() # get_multiple() defaults to the PassGen object count unless a new count is provided.
for s in pw: print("4 - " + s) # 5 passwords printed.

# 5
pg.count = 2 # PassGen object count updated to 2.
pw = pg.get_multiple()
for s in pw: print("5 - " + s) # 2 passwords printed.
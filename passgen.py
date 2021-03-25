import random
import string
import sys

class PassGen():
    count = 1
    length = 16
    sets =  [   [char for char in string.ascii_letters[:26]],
                [char for char in string.ascii_letters[26:]],
                [char for char in string.digits],
                [char for char in string.punctuation]   ]
    sets_enabled = [1 for i in range(len(sets))]

    def __init__(self, count=None, length=None, sets_enabled=None):
        if count: self.count = count
        if length: self.length = length
        if sets_enabled: self.sets_enabled = [int(char) for char in sets_enabled]
        self.set_lengths = [len(self.sets[i]) for i in range(0, len(self.sets))]

    def get_single(self):
        while len(self.sets_enabled) != len(self.sets):
            if len(self.sets_enabled) > len(self.sets): self.sets_enabled.pop()
            else: self.sets_enabled.append(1)
        password = ""
        sets_allowed = []
        sets_required = []
        if self.sets_enabled[:len(self.sets)].count(1) > 0:
            for i in range(len(self.sets)):
                if self.sets_enabled[i] == 1:
                    sets_allowed.append(i)
                    sets_required.append(i)
            for i in range(self.length):
                if len(sets_required) != 0:
                    idx = random.randrange(0, len(sets_required))
                    charset = sets_required[idx]
                    sets_required.pop(idx)
                else:
                    charset = random.choice(sets_allowed)
                found = False
                while not(found):
                    char_idx = random.randrange(0, self.set_lengths[charset])
                    next_char = self.sets[charset][char_idx]
                    if not(password.endswith(next_char)): found = True
                password += next_char
        else: password = "Failed - All character sets were disabled. " + "".join(str(i) for i in self.sets_enabled)
        return password

    def get_multiple(self):
        passwords = []
        for i in range(self.count):
            passwords.append(self.get_single())
            if passwords[i].startswith("Failed - "): break
        return passwords

def main(args):
    pg = PassGen()
    for i in range(len(args)):
        if args[i] == "-c": pg.count = int(args[i+1])
        elif args[i] == "-l": pg.length = int(args[i+1])
        elif args[i] == "-s": pg.sets_enabled = [int(char) for char in args[i+1]]
    for i in pg.get_multiple(): print(i)

if __name__ == "__main__":
    main(sys.argv[1:])

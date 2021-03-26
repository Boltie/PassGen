import math
import random
import string
import sys

class PassGen():
    allow_repeats = False
    count = 1
    entropy = False
    length = 16
    sets =  [   [char for char in string.ascii_letters[:26]],
                [char for char in string.ascii_letters[26:]],
                [char for char in string.digits],
                [char for char in string.punctuation]   ]
    sets_enabled = [1 for i in range(len(sets))]

    def __init__(self, allow_repeats=None, count=None, length=None, sets_enabled=None):
        if allow_repeats: self.allow_repeats = allow_repeats
        if count: self.count = count
        if length: self.length = length
        if sets_enabled: self.sets_enabled = [int(char) for char in sets_enabled]
        self.set_lengths = [len(self.sets[i]) for i in range(0, len(self.sets))]
    
    def get_entropy(self, char_count, length):
        return math.log(pow(char_count, length), 2)

    def get_single(self, allow_repeats=None, entropy=None, length=None, sets_enabled=None):
        if allow_repeats is not None: self.allow_repeats = allow_repeats
        if entropy: self.entropy = entropy
        if length: self.length = length
        if sets_enabled: self.sets_enabled = [int(char) for char in sets_enabled]
        while len(self.sets_enabled) != len(self.sets):
            if len(self.sets_enabled) > len(self.sets): self.sets_enabled.pop()
            else: self.sets_enabled.append(1)
        entropy = 0
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
                    char_count = 0
                    for s in sets_required: char_count += self.set_lengths[s]
                    entropy += self.get_entropy(char_count, 1)
                    sets_required.pop(idx)
                else:
                    charset = random.choice(sets_allowed)
                found = False
                while not(found):
                    char_idx = random.randrange(0, self.set_lengths[charset])
                    next_char = self.sets[charset][char_idx]
                    if (self.allow_repeats or not(password.endswith(next_char))): found = True
                password += next_char
            entropy_remain = self.length - self.sets_enabled[:len(self.sets)].count(1)
            entropy += self.get_entropy(self.get_char_count(), (entropy_remain if entropy_remain > 0 else 0))
        else: password = "Failed - All character sets were disabled. " + "".join(str(i) for i in self.sets_enabled)
        return password + (" E=" + str(round(entropy, 2)) if self.entropy else "")

    def get_multiple(self, allow_repeats=None, count=None, entropy=None, length=None, sets_enabled=None):
        passwords = []
        if allow_repeats is not None: self.allow_repeats = allow_repeats
        if entropy: self.entropy = entropy
        if count: self.count = count
        if length: self.length = length
        if sets_enabled: self.sets_enabled = [int(char) for char in sets_enabled]
        for i in range(self.count):
            passwords.append(self.get_single())
            if passwords[i].startswith("Failed - "): break
        return passwords

    def get_char_count(self):
        char_count = 0
        for i, char in enumerate(self.sets_enabled):
            if int(char) == 1:
                char_count += self.set_lengths[i]
        if (not(self.allow_repeats) and self.length > 1): char_count -= 1
        return char_count

def main(args):
    pg = PassGen()
    for i in range(len(args)):
        if args[i] == "-c": pg.count = int(args[i+1])
        elif args[i] == "-e": pg.entropy = True
        elif args[i] == "-l": pg.length = int(args[i+1])
        elif args[i] == "-r": pg.allow_repeats = True
        elif args[i] == "-s": pg.sets_enabled = [int(char) for char in args[i+1]]
    for s in pg.get_multiple(): print(s)

if __name__ == "__main__":
    main(sys.argv[1:])

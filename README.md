# PassGen
A Python password generator class that accepts parameters for the count, length, character sets and whether to accept repeating characters.
It defaults to providing a single 16-digit string utilising the lower, upper, digit and punctuation character sets with no repeating characters.

All enabled character sets are utilised at least once before being reused. If you request a 4-digit password with all 4 sets enabled, you will not receive multiple characters from any single character set. It will always return a string with a lower, upper, digit and punctuation character.

You can initialise the `PassGen()` class and use the:
* `get_single()` method to return a single string.

* `get_multiple()` method to return an array of strings.

These methods default to using the stored object values. If you provide any of the parameters, the corresponding object value will also be updated.

You can execute `passgen.py` and provide arguments for the count, length, character sets and whether to accept repeating characters. The password strings will then be printed to the console/terminal.

# Console/Terminal Arguments
`-c [int]` Provide an integer to denote the number of passwords you would like returned.

`-e` Denotes that the calculated entropy of the generated password should also be printed.

`-l [int]` Provide an integer to denote the length of generated passwords.

`-r` Denotes repeating characters allowed. No need to provide anything else.

`-s [string]` Provide a string containing only 0's or 1's to flag which sets to utilise. Set order = lower/upper/digit/punctuation. By default, all sets are enabled (e.g. `-s 1111`).

# Example Console/Terminal Commands
The below will generate by default a single, 16-digit password utilising all character sets.\
`python passgen.py`
  
The below will generate a single, 10-digit password utilising the punctuation character set.\
`python passgen.py -l 10 -s 0001`
  
The below will generate 100, 16-digit passwords utilising the digit character set. Repeating characters allowed.\
`python passgen.py -r -c 100 -s 0010`
  
The below will generate 10, 8-digit passwords utilising the lower and upper character sets.\
`python passgen.py -c 10 -l 8 -s 1100`

# Entropy
I have quickly implemented something I believe is close to what is required. The method used assumes an attacker knows the password length, what character sets were used upon generation, what the set order was for the first characters generated with unused character sets and that the password was also generated with this generator. No attacker would know what character sets were used or which order the sets were picked from so this is more than a worst-case scenario.

At the moment, any of the starting digits that are generated before all allowed characters sets have been used will have their own entropy calculated. These will be summed and added to the final entropy for the remaining length of the password (where all characters had the same pool to pick from). If repeating characters are allowed, the character count is lowered by 1 unless the character is the first to be generated. This again assumes that an attacker knows there to be no repeating characters chosen when generating the password.

I'm not planning to put much more effort into this as any measurement has to make a lot of assumptions and I think the most important thing about generating a password is that it is relatively long and randomly made up from a good selection of characters. It might be worth just sticking to `math.log(pow(char_count, length), 2)` and setting the char_count to the sum of chars in each enabled character set to keep things simple. The main purpose of the entropy value is to indicate a password strength. I believe both the current and a basic implementation would suffice in achieving that.

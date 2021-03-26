# PassGen
A Python password generator class that accepts parameters for the count, length, character sets and whether to accept repeating characters.
It defaults to providing a single 16-digit string utilising the lower, upper, digit and punctuation character sets with no repeating characters.

All enabled character sets are utilised at least once before being reused. If you request a 4-digit password with all 4 sets enabled, you will not receive multiple characters from any single character set. It will always return a string with a lower, upper, digit and punctuation character.

You can initialise the `PassGen()` class and use the:
* `get_single(allow_repeats=None, length=None, sets_enabled=None)` method to return a single string.

* `get_multiple(allow_repeats=None, count=None, length=None, sets_enabled=None)` method to return an array of strings.

These methods default to using the stored object values. If you provide any of the parameters, the corresponding object value will also be updated.

You can execute `passgen.py` and provide arguments for the count, length, character sets and whether to accept repeating characters. The password strings will then be printed to the console/terminal.

# Console/Terminal Arguments
`-ar` Denotes repeating characters allowed. No need to provide anything else.

`-c [int]` Provide an integer to denote the number of passwords you would like returned.

`-l [int]` Provide an integer to denote the length of generated passwords.

`-s [string]` Provide a string containing only 0's or 1's to flag which sets to utilise. Set order = lower/upper/digit/punctuation. By default, all sets are enabled (e.g. `-s 1111`).

# Example Console/Terminal Commands
The below will generate by default a single, 16-digit password utilising all character sets.\
`python passgen.py`
  
The below will generate a single, 10-digit password utilising the punctuation character set.\
`python passgen.py -l 10 -s 0001`
  
The below will generate 100, 16-digit passwords utilising the digit character set. Repeating characters allowed.\
`python passgen.py -ar -c 100 -s 0010`
  
The below will generate 10, 8-digit passwords utilising the lower and upper character sets.\
`python passgen.py -c 10 -l 8 -s 1100`

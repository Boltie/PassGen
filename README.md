# PassGen
A Python password generator class that accepts parameters for the count, length and character sets to utilise.
It defaults to providing a single 16-digit string utilising the lower, upper, digit and punctuation character sets.

All enabled character sets are utilised at least once before being reused.\
For example, if you request a 4-digit password with all 4 sets enabled, you will not receive multiple characters from a single character set. It will always return a string with a lower, upper, digit and punctuation character.

Characters are never repeated.

You can initialise the PassGen() class and use the get_single() method to return a single string or get_multiple() method to return an array of strings based on the provided count.

You can also execute passgen.py and provide arguments for the count, length and character sets to utilise. The password strings will then be printed to the console.

# Terminal Arguments
[ -c ] provide an integer to denote the number of passwords you would like returned.

[ -l ] provide an integer to denote the length of generated passwords.

[ -s ] provide a string containing only 1's or 0's to flag which sets to utilise. Set order = lower/upper/digit/punctuation. By default, all sets are enabled (e.g. -s 1111).

# Example Terminal Commands
The below will generate by default a single, 16-digit password utilising all character sets.\
python passgen.py
  
The below will generate a single, 10-digit password utilising the punctuation character set.\
python passgen.py -l 10 -s 0001
  
The below will generate 100, 16-digit passwords utilising the digit character set.\
python passgen.py -c 100 -s 0010
  
The below will generate 10, 8-digit passwords utilising the lower and upper character sets.\
python passgen.py -c 10 -l 8 -s 1100

# Python string format() method
#Definition and Usage
#The format() method formats the specified value(s) and insert them inside the string's placeholder. The Placeholder is
#defined using curly brackets: {}.
txt="For only {price: .2f} dollars!"
print(txt.format(price=48))
#////////////////////////////////////////////////////////////////////////////
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

# Formatting Types
# Inside the placeholders you can add a formatting type to format the result:

# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format



# Creating a String with "" or ''
String1 = 'Welcome to the Geeks World'
print(String1)
########################################################################
# Python Program to Access characters of String
String1 = "GeeksForGeeks"
print(String1)
print("\nFirst character of String is: ")
print(String1[0])
print("\nLast character of String is: ")
print(String1[-1])
################################################################
# Python Program to demonstrate String slicing
String1 = "GeeksForGeeks"
print(String1)
print("\nSlicing characters from 3-12: ")
print(String1[3:12])
# 3rd and 2nd last character
print("\nSlicing characters between " +
    "3rd and 2nd last character: ")
print(String1[3:-2])
###############################
# Python Program for Escape Sequencing of String
String1 = '''I'm a "Geek"'''
print(String1) 
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)
# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)
# Printing Paths with the use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)
################################################################
# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)
# Using raw String to ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)
################################################################
# Python Program for  Formatting of Strings
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)
################################################################
# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)
# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)
# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)
################################################################
# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)
# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)
################################
# Python Program for Old Style Formatting of Integers
Integer1 = 12.3456789
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' % Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' % Integer1)

##########  String constants #################

# Built-In Function	        Description

# string.ascii_letters  	Concatenation of the ascii_lowercase and ascii_uppercase constants.
# string.ascii_lowercase	Concatenation of lowercase letters
# string.ascii_uppercase	Concatenation of uppercase letters
# string.digits         	Digit in strings
# string.hexdigits      	Hexadigit in strings
# string.letters	        concatenation of the strings lowercase and uppercase
# string.lowercase      	A string must contain lowercase letters.
# string.octdigits	        Octadigit in a string
# string.punctuation	    ASCII characters having punctuation characters.
# string.printable	        String of characters which are printable
# String.endswith()     	Returns True if a string ends with the given suffix otherwise returns False
# String.startswith()   	Returns True if a string starts with the given prefix otherwise returns False
# String.isdigit()	        Returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
# String.isalpha()	        Returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.
# string.isdecimal()	    Returns true if all characters in a string are decimal.
# str.format()	            one of the string formatting methods in Python3, which allows multiple substitutions and value formatting.
# String.index	            Returns the position of the first occurrence of substring in a string
# string.uppercase      	A string must contain uppercase letters.
# string.whitespace	        A string containing all characters that are considered whitespace.
# string.swapcase()	        Method converts all uppercase characters to lowercase and vice versa of the given string, and returns it
# replace()	                returns a copy of the string where all occurrences of a substring is replaced with another substring.

##########  Deprecated string functions #################

# Built-In Function	    Description
 

# string.Isdecimal	    Returns true if all characters in a string are decimal
# String.Isalnum	    Returns true if all the characters in a given string are alphanumeric.
# string.Istitle	    Returns True if the string is a title cased string
# String.partition	    splits the string at the first occurrence of the separator and returns a tuple.
# String.Isidentifier	Check whether a string is a valid identifier or not.
# String.len	        Returns the length of the string.
# String.rindex	        Returns the highest index of the substring inside the string if substring is found.
# String.Max	        Returns the highest alphabetical character in a string.
# String.min	        Returns the minimum alphabetical character in a string.
# String.splitlines 	Returns a list of lines in the string.
# string.capitalize	    Return a word with its first character capitalized.
# string.expandtabs	    Expand tabs in a string replacing them by one or more spaces
# string.find	        Return the lowest indexing a sub string.
# string.rfind	        find the highest index.
# string.count	        Return the number of (non-overlapping) occurrences of substring sub in string
# string.lower	        Return a copy of s, but with upper case, letters converted to lower case.
# string.split	        Return a list of the words of the string, If the optional second argument sep is absent or None
# string.rsplit()	    Return a list of the words of the string s, scanning s from the end.
# rpartition()	        Method splits the given string into three parts
# string.splitfields	Return a list of the words of the string when only used with two arguments.
# string.join	        Concatenate a list or tuple of words with intervening occurrences of sep.
# string.strip()	    It returns a copy of the string with both leading and trailing white spaces removed
# string.lstrip	        Return a copy of the string with leading white spaces removed.
# string.rstrip	        Return a copy of the string with trailing white spaces removed.
# string.swapcase	    Converts lower case letters to upper case and vice versa.
# string.translate	    Translate the characters using table
# string.upper	        lower case letters converted to upper case.
# string.ljust	        left-justify in a field of given width.
# string.rjust	        Right-justify in a field of given width.
# string.center()	    Center-justify in a field of given width.
# string-zfill	        Pad a numeric string on the left with zero digits until the given width is reached.
# string.replace	    Return a copy of string s with all occurrences of substring old replaced by new.
# string.casefold()	    Returns the string in lowercase which can be used for caseless comparisons.
# string.encode	        Encodes the string into any encoding supported by Python. The default encoding is utf-8.
# string.maketrans	    Returns a translation table usable for str.translate()
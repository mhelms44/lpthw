#uses \t to tab the new line
tabby_cat = "\tI'm tabbed in."
#uses \n to put it on a new line
persian_cat = "I'm split\non a line."
#uses \\ to create a single \
backslash_cat = "I'm \\ a \\ cat."

#uses the triple quotes to create block of strings which escapes all text anyway, however we use the \t and \n to do tabs and new lines
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
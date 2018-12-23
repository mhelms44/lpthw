# imports sys
import sys
# sets required arguments for program to run
script, input_encoding, error = sys.argv

# creates main function  which will read the language file line
def main(language_file, encoding, errors):
    line = language_file.readline()
# if a line is not empty this statement will be true and will continue to run until it runs out of lines
    if line:
        # runs the print_line function
        print_line(line, encoding, errors)
        # at the end of the function, it re-runs the main function again. 
        return main(language_file, encoding, errors)
# print_line function, which is called from the main function
def print_line(line, encoding, errors):
# line.strip() by default removes any whitespaces on the line
    next_lang = line.strip()
    # we use the encode method to take the string and encode it with its byte form and set that as the raw_bytes var
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # the decode method takes rawbytes and decodes it into a readable string
    cooked_string = raw_bytes.decode(encoding, errors=errors)
# this prints out the raw_bytes and cooked_string var
    print(raw_bytes, "<===>", cooked_string)
# sets the language var with the languages.txt file
languages = open("languages.txt", encoding="utf-8")
# when the script is run, we call the main function and pass it the language, input_encoding, and error arguments. 
main(languages, input_encoding, error)


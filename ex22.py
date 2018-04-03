from sys import argv
#import sys
script, input_encoding ,error = argv

#script = "ex22.Py"
#input_encoding = "utf-8"
#error = "strict"

def main(lanaguage_file, encoding, errors):
    line = lanaguage_file.readline()

    if line:
        print_line(line, encoding,errors)
        return main(lanaguage_file,encoding,errors)

def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("/home/kpatel/Python-3.6.0/lpthw/languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


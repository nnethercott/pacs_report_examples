import re

import argparse
parser = argparse.ArgumentParser(description='A convenient way to modify sim params externally')
parser.add_argument('-f', "--file", help="Specify filename", default="")

args = parser.parse_args()

text = None
with open(args.file) as f:
    text = f.read()

r = re.findall(r"\{.*\}", text)
print(r)

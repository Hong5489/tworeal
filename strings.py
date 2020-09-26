from helper import cmdline
import re

def extract():
    results = re.split("\r|\n", cmdline("strings test.string"))
    return '<br>'.join(results)
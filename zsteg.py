from helper import cmdline
import re

def extract():
    results = re.split("\r|\n", cmdline("zsteg test.png --all"))
    chans = []
    for elt in results:
        if elt[23:28]:  # , Keep channels only
            chans.append(elt)
    result = ''
    for c in chans:
        index = c.find("..")
        result += "<b>" + c[:index] + "</b>" + c[index:] + "<br>"
    return result
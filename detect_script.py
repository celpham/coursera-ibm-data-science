

tokens = []
with open("detect_script.csv", "r") as file:
    try:
        token = "//"
        while token:
            token = file.readline()
            if token[0:1] == "//":
                continue
            tokens.append(token.strip())
    except:
        file.close()

rootdir = "D:/KALLYAS 4.17.1 - Creative eCommerce Multi-Purpose WordPress Theme/KALLYAS 4.17.1 - Creative eCommerce Multi-Purpose WordPress Theme/"

import glob, os
os.chdir(rootdir)

for filename in glob.iglob('**/*.php', recursive=True):
    filename = filename.replace("\\\\", "\\")
    try:
        with open(".\\" + filename, "r") as file:
            try:
                file_text = file.read()            

                for token in map(lambda t: t if file_text.find(t) > -1 else None, tokens):
                    if not token:
                        continue
                        
                    print(" ** {} **".format(filename))
                    print(" -> {} ".format(token))

            except:
                file.close()
    except FileNotFoundError:
        print(" !!!!! => {} ".format(filename))

print(" ***************** FINISHED ***************** ")
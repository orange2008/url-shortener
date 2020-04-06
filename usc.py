import json

print("This is Unattend script creator.")
print("This program is just create a script.")

print("Script is a json file, you can copy it to anywhere.")
print("We will overwritten this file.")
fn = input("Script name: ")
fn = fn + ".json"
d = []
t = 1
print("\n\n\n")
print("Create wizard began.")
print("If you type: quit , we will save and quit. If you didn't save and exit, all operation will cancel.")
while True:
    print("\n")
    url = input("URL " + str(t) + ": ")
    if url == "quit":
        print("Saving...")
        with open(fn, 'w') as ff:
            json.dump(d, ff)
        print("Ok.")
        l = len(d)
        if l == 1:
            p = "is"
        else:
            p = "are"
        print("There " + p + " " + str(l) + " URL in it.")
        break
    else:
        pass
    d.append(url)
    t = t + 1
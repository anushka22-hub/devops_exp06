file = open("index.html", "r")
code = file.read()
file.close()

if "<html>" in code and "</html>" in code:
    print("HTML Test Passed")
else:
    print("HTML Test Failed")
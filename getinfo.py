txt = "spring-2023_Spring.txt"
new2023 = "sping-2023.csv"
data = open(txt,"r")
getin = open(new2023,"w")
listcollect = []
while True:
    content = data.readline()
    listcollect.append(content)
    if (content == "DONEREAD"):
        break
    for i in listcollect:
        getin.write(i)
    listcollect = []

    
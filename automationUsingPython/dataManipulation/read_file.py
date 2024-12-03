
#this code reads the records of grades in inputFile.txt and write the passed records into passFile.txt and the failed ones into failFile.txt
inputFile=open("Documents/inputFile.txt", "r")
passFile=open("Documents/passFile.txt", "w")
failFile=open("Documents/failFile.txt", "w")


for line in inputFile:
    line_split=line.split()
    if line_split[2]=="P":
        passFile.write(line)
    else:
        failFile.write(line)

inputFile.close()
passFile.close()
failFile.close()


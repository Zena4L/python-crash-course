# create a file of usersname in batch mode

def batchName():
    print("This program create a file of username from a")
    print("file of names")

    # get the filenames
    infileName = input("What are the file names in : ")
    outfileName = input("What file should the username go in : ")

    #open the files
    infile = open(infileName,"r")
    outfile = open(outfileName,"w")

    # process each line of the input field
    for line in infile:
        #get first and last name from line
        first,last = line.split()
        #create the username
        uname = (first[0] + last[0:7]).lower()
        #write it to the output file
        print(uname,file=outfile)
    infile.close()
    outfile.close()

batchName()
import sys
import time 

argsfile = open("args.txt", "a") #Output to file

scriptfullname = "This is the name of the script: ", str(sys.argv[0])
print(scriptfullname)
argsfile.write("".join(str(scriptfullname)))
print(scriptfullname)
argsfile.write("\n")

argnumber = "Number of arguments:", len(sys.argv), "arguments"
argsfile.write("".join(str(argnumber)))
print(argnumber)
argsfile.write("\n")

arglist = "Argument List:", str(sys.argv)
argsfile.write("".join(str(arglist)))
print(arglist)

argsfile.close()

time.sleep(100)

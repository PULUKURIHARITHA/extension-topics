#Extensions
#r+    ->fil;le should exist / overwrits existing content
#w+    -> content clarity(refresh)
#a+   ->creates a file if exists,reading works only after seek()
#truncate()
filename='sample.txt'
with open(filename,'w') as f:
    f.write("My full name is Haritha Pulukuri.\n")
with open(filename,'r+')as file:
    print("latest data :")
    print(file.read())
    file.seek(0)
    userinput=input("\n enter text to overwrite from begining....")
    file.write(userinput)
    file.seek(0)
    print("\n file after writing by r+")
    print(file.read())
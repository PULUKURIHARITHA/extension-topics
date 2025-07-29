with open('sample.txt','w+') as file:
    text=input("enter the data.....")
    file.write(text)
    file.seek(0)
    print("\n latest file content ")
    print(file.read())
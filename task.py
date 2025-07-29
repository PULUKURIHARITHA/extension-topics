filename=input("enter filename with extension :")
with open(filename, 'r') as file:
    text=file.read()
    letter=input("enter a char to search frequency:")
    count=0
    for char in text:
        if char==letter:
            count +=1
print(letter,"appears",count,"time in the file") 
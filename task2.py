user_input=input("Enter text to write in file:")
with open('output.txt','w') as file:
    file.write(user_input +"\n")
    print("Data saved in output.txt")

apprended_data=input("Enter additional data to apprehend:")
with open('output.txt','a') as file:
    file.write(apprended_data+"\n")
    print("Data successfully appended")

print("Final content of output.txt")
with open('output.txt','r') as file:
    read_file=print(file.read())
    print(read_file)



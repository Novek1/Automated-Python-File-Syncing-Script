with open('test1.txt', 'w') as write_file:
    write_file.write("Today I just collected my Bachelor of Engineering in Computer Science Diploma")
# this creates a file and writes in it 


with open('test1.txt', 'r') as read_file:
    print(read_file.read())
# this reads the text we put in the file

with open('test1.txt', 'a') as write_file:
    write_file.write("\n Here is the read, append and write file I am learning today.")
#This adds some text to the file

with open('test1.txt', 'r') as read_file:
    print(read_file.read())

# this part reads the appended file

with open('test1.txt' ,'w')as write_file:
    write_file.write("All the text has been deleted.")

# This part deletes all the texts and replaces t with "All the text has been deleted."

with open('test1.txt', 'r') as read_file:
    print(read_file.read())
# This reads that file and should show "All the text has been deleted."

#using the with key word avoids the responsibility of having to close the file manually after executing the file operation

write_file =open('test.txt', 'w')
write_file.write("original text ")
write_file.close()

with open('test1.txt', 'r') as read_file:
    print(read_file.read())
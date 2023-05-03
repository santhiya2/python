filename = "preproinsulin-clean.txt"  # replace with your file name

x = filename.split("5")
print(x)


with open(filename, "r") as file:
    contents = file.read()
    

count = 0
for char in contents:
    if char.islower():   
        count += 1
print("The number of lowercase letters in the file is:", count)
  
with open("preproinsulin-clean.txt" ,"r") as source_file:
    file_contents = source_file.read()
with open("Isinsulin.txt", "w" ) as dest_file:
    extarct_contenct = file_contents[:24]
    dest_file.write(extarct_contenct)
    
with open("binsulin.txt" ,"w") as dest_file2:
    extarct_contenct2 = file_contents[24:54]
    dest_file2.write(extarct_contenct2)
    
with open("cinsulin.txt" ,"w") as dest_file3:
    extarct_contenct3 = file_contents[54:90]
    dest_file3.write(extarct_contenct3)
    
with open("ainsulin.txt" ,"w") as dest_file4:
    extarct_contenct4 = file_contents[90:111]
    dest_file4.write(extarct_contenct4)
source_file.close()  
dest_file.close()   
dest_file2.close()
dest_file3.close()
dest_file4.close()
 
    
    

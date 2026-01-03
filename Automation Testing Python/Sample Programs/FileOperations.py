
### File read operations

# Goto file path, locate file with name, 
# open file
# Read content from file 
# print/copy content
# close file
## -------------------------------------------------------------
# fileVariable = open("C:\\tmp\\Class\\T8DemoFile.txt")  # open file
# content = fileVariable.read()           # Read content
# print("File content: ", content)        # print file 
# fileVariable.close()        # close file    # very important

# ## ------------------------------------------------

# try:
#     fileVariable = open("C:\\tmp\\Class\\T8DemoFile1.txt")  # open file
#     content = fileVariable.read()           # Read content
#     print("File content: ", content)        # print file 
# except Exception as e:
#     print("Something went wrong: ", e) 
# finally:
#     try:
#         fileVariable.close()        # close file    # very important
#         print("file has been closed")
#     except: 
#         print("File never opened..")


# ## -------------------------------------------------------------------------
# ## opne file in read mode
# fileVariable = open("C:\\tmp\\Class\\T8DemoFile.txt",'r')  # open file
# content = fileVariable.read()           # Read content
# print("File content: ", content)        # print file 
# fileVariable.close()        # close file    # very important

## --------------------------------------------------------------------
## opne file in write mode

# content = '''Updated content for T8 batch 
#             File opened in write mode
#         '''


# fileVariable = open("C:\\tmp\\Class\\T8DemoFile.txt",'w')  # open file
# fileVariable.write(content)             # Write content in file
# #content22 = fileVariable.read()           # Read content
# print("File content: ", content)        # written content in file 
# fileVariable.close()        # close file    # very important

#-------------------------------------------------------------------------

# Special way to open a file....

with open("C:\\tmp\\Class\\T8DemoFile.txt",'r') as fileVariable:
    contents = fileVariable.readlines()
    print("File content: ", contents)        # written content in file 


### ----------------------------------------------
# Special way to open a file....
content = '''Updated content for T8 batch 
            File opened in write mode

            Text inserted on 21 Feb 22
        '''
with open("C:\\tmp\\Class\\T8DemoFile.txt",'r') as fileVariable:
    #contents = fileVariable.readlines()
    fileVariable.write(content)             # Write content in file
    contents = fileVariable.read()

    print("File content: ", contents)        # written content in file 


### ----------------------------------------------

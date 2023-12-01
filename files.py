#? when working with python I might want to work with some external files like text document or excel spreadsheet
#? here we are going to learn about how to read and write that file 

country_file = open('E:/python/countries.txt', 'w') #! r : read only, w : write only , r+ : read and write , a : append to the end of the file
# print(country_file.readlines())

# country_file.close()

country_file.write('This is the new text')
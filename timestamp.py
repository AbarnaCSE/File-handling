import datetime
current_datetime=datetime.datetime.now()
print(current_datetime)
str_current_datetime = str(current_datetime)
file_name = str_current_datetime
file = open("file_name.txt",'w')
file.write(file_name)
print("File created:",file_name)
file.close()
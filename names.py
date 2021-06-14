filenames = []
fileExtension = ".txt"

for i in range(1880, 2021):
   j = "yob{}{}".format(i,fileExtension)
   j = j.replace("'","") 
   filenames.append(j)
   

with open('/home/imme/Documents/names/Names.csv', 'w') as output:
    for name in filenames:
        with open(name) as file:
            for line in file:
                output.write(line)

print("Action Completed!")
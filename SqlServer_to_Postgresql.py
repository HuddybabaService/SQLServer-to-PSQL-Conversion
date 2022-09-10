import re

file = open('mssql_insert_statements.txt', 'r')

lines = file.readlines();

output_file = open('output.txt', 'a')
output_file.truncate(0)

for line in lines:
    if(line.startswith('INSERT')):
        
        line = line.replace("[dbo].", "").replace("[", "").replace("]","")

        line = line[:6] + " INTO" + line[6:]

        insertCommandFirstHalf = line.split("VALUES")

        values = insertCommandFirstHalf[1].strip()[1:-1]

        splittedValues = values.split(",")

        newValues = []

        for val in splittedValues:
            if "N'" in val.strip():
                val = val.replace('N', '').replace('\'', '')
                val = val.strip()
                val = '\'' + val + '\''
            newValues.append(val)
        print(newValues)
        
        output_file.write(insertCommandFirstHalf[0].strip() + ' VALUES ' + '(' + ','.join(newValues) + ');\n\n')

file.close()
output_file.close()

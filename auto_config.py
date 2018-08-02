import re
import os

# configuration file template
conf_temp= '''
input {
    beats {
        port => "5044"
    }
}

filter {
	csv {
	    columns => ["sepal length", "sepal width", "petal length", "petal width", "clas"]
	    separator => ","
	}
	
	#mutate
}
output {
	stdout { codec => rubydebug }
	elasticsearch{
		index => "plants"
		hosts => "localhost:9200"
	}
}
'''

# function to check if string's vlaue can be float
def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# function to return the required type
def getType(s):
    if isfloat(s):
        return "float"
    return "text"

def writeConversion(dictionary):
    return ['\t\tconvert => {"[' + key + ']" => "' + dictionary[key] + '"}\n' for key in dictionary]

# get names of files in python 3.6
data_file_name = input("Data File Name: ")
conf_file_name = input("Configurations File Name: ")

# get names of files in python 2.7
# data_file_name = raw_input("Data File Name: ")
# conf_file_name = raw_input("Configurations File Name: ")

# get index name
db_name = input("Insert Desirable Index/DB name: ")

# get column title names
with open(data_file_name, "r") as in_data:
    file_lines = in_data.readlines()

# check if file exists
if in_data.mode == 'r':
    table_column_titles_array = re.sub("[\n\r\"]", '', re.sub(r"\\\\TARDIS\\", '', file_lines[0])).split(',')
    data_sample =  re.sub("[\n\r\"]", '', file_lines[2]).split(',')


d = dict(zip(table_column_titles_array, map(getType, data_sample)))

# swap all the values to string in case the text file is formated in binary 
# (in general: where the values cannot be understood by logstash, 
# like the example of the windows tool logman)
string_mutate_lines = 'mutate{\n' + ''.join(writeConversion(d)) + '\n\t}'

# format the conversion lines
conversion_lines = 'mutate{\n' + ''.join(writeConversion(dict.fromkeys(d, "string"))) + '\n\t}'

# write to output file
with open(conf_file_name, 'w+') as fout:
    fout.writelines(re.sub("#mutate", string_mutate_lines + '\n' + conversion_lines, re.sub("index =>.*"
    , 'index => "' + db_name + '"', re.sub("columns =>.*"
    , "columns => " + '["'+'", "'.join(table_column_titles_array)+'"]', conf_temp))))


print("Done!")

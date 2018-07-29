import re

# get names of files in python 3.6
data_file_name = input("Data File Name: ")
conf_file_name = input("Configurations File Name: ")

# get names of files in python 2.7
# data_file_name = raw_input("Data File Name: ")
# conf_file_name = raw_input("Configurations File Name: ")

# get column title names
with open(data_file_name, "r") as in_data:
    file_lines = in_data.readlines()

# check if file exists
if in_data.mode == 'r':

    table_column_titles_array = file_lines[0][:-2].split(',')

# read the config file
with open(conf_file_name, "r") as in_data:
    # check if file exists
    if in_data.mode == 'r':
        config_contents = in_data.read()

# write to output file
with open(conf_file_name, 'w+') as fout:
    fout.writelines(re.sub("columns:"
    , "columns: " + '"'+'", "'.join(table_column_titles_array)+'"'
    , config_contents)
)

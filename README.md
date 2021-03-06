# Logstash-AutoConfigureTable
>This is a simple script that auto-creates a configuration file for logstash from a csv data file.

## Pre-conditions
1. data needs to be in csv format (`.txt.` or `.csv`)
2. output file must be a `.conf` file
3. the column names need to be all be written on the first line and seperated by commas
4. The `.conf` file will look similar to the following snippet

Example:
```
filter {
    grok {
        #match => ...etc...
    }
    csv {
        columns =>
        seperator => ","
    }
}
```

>Tip: `bcancer.csv` file is merely provided to serve as templates or for testing, it carries no particular significance for the code to run.


5. python 2.7 or python 3.6 (or higher) needs to be installed
6. install the correct version of the code for your python version of choice


## Steps
1. choose a code version by fetching the branch with your version number (default/master branch is set to Python 3.6)
2. open bash
3. go to the cloned folder's directory
4. run code:
    
    * for Python 2.7: `python auto_config.py`
    * for Python 3.6 (or higher): `python3 auto_config.py`
5. when prompted to enter file names, do so with their file extensions (and path if needed)
6. finally enter the database name which will be used as index when inputed into Elasticsearch


## Result
>After running the code, an output file will be created by an array of strings including the column names, their data types, as well as the index.

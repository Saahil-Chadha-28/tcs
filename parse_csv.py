import errno, unittest
import sys 
def parse_csv(dir_name):
    import os, csv

    # to store content from different csv files
    content = []

    # open Combined.csv to write header row if not already written
    outputFile = open(dir_name+os.path.join('\\')+'Combined.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile)
    open_output_file = open(dir_name+os.path.join('\\')+"Combined.csv")
    out_file_reader = csv.reader(open_output_file)
    if (len(list(out_file_reader)) == 0):
        outputWriter.writerow(['Source IP','Environment'])


    # scanning the directory, reading from csv files, appending rows to Combined.csv
    if os.path.isdir(dir_name):
        for file in os.listdir(dir_name):
            fileName = file.split('.')
            if (os.path.isfile(dir_name+os.path.join('\\')+file) and file != 'Combined.csv'):
                file_ = open(dir_name+os.path.join('\\')+file)
                file_reader = csv.reader(file_)
                for row in file_reader:
                    if (file_reader.line_num == 1):
                        continue
                    content.append([row[0],fileName[0]])
                    
                    
        for row_list in content:
            outputWriter.writerow(row_list)           
    outputFile.close()
    
    
           


# provide directory path in function call
parse_csv(r'C:\Test\Engineering Test Files')


#Unit Test   
class TestIO(unittest.TestCase):
    def test_file_not_found(self, dir_name=''):
        import os
        if (not os.path.isdir(dir_name)):
            self.assertRaises(ValueError, parse_csv, dir_name)
        else:
            print('Success in Unit Test')
        

test_io =  TestIO()
# provide directory path to test
test_io.test_file_not_found(r'C:\Test\Engineering Test Files')



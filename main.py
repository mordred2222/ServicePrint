#import time
#import pandas as pa
#import re
import os
import PyPDF2
#path='/path/to/process/'
path='./folders_with_pdf/'

files=os.listdir(path)
for file in files: 
        print (file)
        try:
            PyPDF2.PdfFileReader(open(path+file, "rb"))
        except PyPDF2.utils.PdfReadError:
                print("invalid PDF file")
        else :
                pass
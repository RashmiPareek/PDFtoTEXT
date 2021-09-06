#Pip Install Tika [For importing the package]
from tika import parser
import json


def pdfToText(fileName,outputPath):
    raw = parser.from_file(fileName)

    with open(outputPath, 'w') as convert_file:
        convert_file.write(json.dumps(raw))

if __name__ == '__main__':
     pdfToText('YOUR_FILE_NAME','YOUR_TEXT_FILE')




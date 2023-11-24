import docx
import sys

def main():
    while True:
        print("Hello and welcome to the CV Bot")
        print("Please input your information here and make sure that places in your CV")
        print("have {{company}} and {{position}} where the company and position name is")
        print("./CVChange filename position company")

        if (len(sys.argv) != 4):
            Usage()
        else:
            filePath = sys.argv[1]
            position = sys.argv[2]
            company = sys.argv[3]
            doc = docx.Document(filePath)
            for paragraph in doc.paragraphs:
                print(paragraph.text)



def Usage():
    print("Please use the command correctly")
    print("./CVChange filename position company")

if __name__ == "__main__":
    main()
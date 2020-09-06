#Run this code when there is pdf file abd txt file in the same directory
#or add the path of the file
#edit the file paths


# importing required modules
import PyPDF2
 
# creating a pdf file object
pdf_file = open('pdf/sample_2.pdf', 'rb') # edit the file path

#creating a txt file object
text_file = open('txt/sample.txt','w') #edit the file path
 
# creating a pdf reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
 
# printing number of pages in pdf file
print(pdf_reader.numPages)
 
# creating a page object
page_obj = pdf_reader.getPage(0)
 
# extracting text from page
#print(pageObj.extractText())
 
#writing extracted text into txt file
text_file.write(page_obj.extractText())

# closing the pdf file object
pdf_file.close()

#closing text file
text_file.close()

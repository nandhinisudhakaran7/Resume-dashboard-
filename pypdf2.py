# install (run once in terminal)
# pip install PyPDF2

import PyPDF2
import re
from collections import Counter
def extract_all_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text
#check if the specific word exist
word = "Python"
text = extract_all_text(pdf_path)
print(word.lower() in text.lower())

#count occurrences of words
word = "Python"
text = extract_all_text(pdf_path).lower()
print(text.count(word.lower()))

#Extract term from user page number
page_no = int(input("Enter page number: ")) - 1
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(reader.pages[page_no].extract_text())

#words per page
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    for i,page in enumerate(reader.pages):
        print(f"Page {i+1}:", len(page.extract_text().split()))
        
#longest word
words = extract_all_text(pdf_path).split()
print(max(words, key=len))

#shortest word
words = extract_all_text(pdf_path).split()
print(min(words, key=len))

#Exract only numbers
text = extract_all_text(pdf_path)
print(re.findall(r'\d+', text))

#Extract only email id's
text = extract_all_text(pdf_path)
emails = re.findall(r'\S+@\S+', text)
print(emails)

#Extract only phone numbers
text = extract_all_text(pdf_path)
phones = re.findall(r'\b\d{10}\b', text)
print(phones)

#Extract  upperlines
lines = extract_all_text(pdf_path).splitlines()
upper = [line for line in lines if line.isupper()]
print(upper)

#convert text to lowercase
print(extract_all_text(pdf_path).lower())

#remove special characters
text = extract_all_text(pdf_path)
clean = re.sub(r'[^A-Za-z0-9\s]', '', text)
print(clean)

#word frequency
words = extract_all_text(pdf_path).lower().split()
freq = Counter(words)
print(freq)

#most frequent word
words = extract_all_text(pdf_path).lower().split()
print(Counter(words).most_common(1))

#split into sentence & count
text = extract_all_text(pdf_path)
sentences = re.split(r'[.!?]', text)
print(len(sentences))

# search keyword and show page number
keyword = "Python"
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    for i,page in enumerate(reader.pages):
        if keyword.lower() in page.extract_text().lower():
            print("Found on page", i+1)
            

#merge text from multiple pdf
files = ["a.pdf","b.pdf"]
merged_text = ""
for f in files:
    merged_text += extract_all_text(f)

print(merged_text)

#extract text from even pages
with open(pdf_path,"rb") as file:
    reader = PyPDF2.PdfReader(file)
    for i,page in enumerate(reader.pages):
        if (i+1)%2==0:
            print(page.extract_text())


#extract text from odd pages
with open(pdf_path,"rb") as file:
    reader = PyPDF2.PdfReader(file)
    for i,page in enumerate(reader.pages):
        if (i+1)%2!=0:
            print(page.extract_text())
            
            
#handle file not error
try:
    text = extract_all_text("missing.pdf")
    print(text)
except FileNotFoundError:
    print("PDF file not found!")
    
    
    
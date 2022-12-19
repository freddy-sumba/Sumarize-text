# Summarize-text

The process itself is quite simple:

1. Download the PDF
2. Convert from pdf to text
3. Feed the text to the GPT-3 model using the openai api
4. Show the summary

Here you will have to install openai for interfacing with GPT-3 in case you have an API key, 
if you don’t have it you can get started here.
https://openai.com/api/
You will also need wget for downloading the pdf from the arxiv page 
and pdfplumberfor converting the pdf to text:

```
pip install openai
pip install wget
pip install pdfplumber

```



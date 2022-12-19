#pip install openai
#pip install wget
#pip install pdfplumber
#



import openai
import wget
import pathlib
import pdfplumber
import numpy as np

def getPaper(paper_url, filename="InformeCamaraComercio.pdf"):
    """
    Downloads a paper from it's arxiv page and returns
    the local path to that file.
    """
    downloadedPaper = wget.download(paper_url, filename)    
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)

    return downloadedPaperFilePath


def showPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:"
    openai.organization = 'org-KEY'
    openai.api_key = "API-KEY"
    engine_list = openai.Engine.list() 
    
    for page in paperContent:    
        text = page.extract_text() + tldr_tag
        data = text[:3500]

        #response = openai.Completion.create(engine="text-davinci-003",prompt=data,temperature=0.3,
        response = openai.Completion.create(engine="text-davinci-003",prompt=data,temperature=0.25,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        print(response["choices"][0]["text"])


paperContent = pdfplumber.open(r"InformeCamaraComercio.pdf").pages
showPaperSummary(paperContent)
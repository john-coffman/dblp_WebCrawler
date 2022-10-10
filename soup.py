import re
from dataclasses import dataclass


@dataclass
class data:
    author: str
    year: str
    Journals: int
    Conference_papers: int

data_needed = []
def parser(text_file):
    years = []
    authors = []
    published = []
    journals = 0
    Conference_papers = 0
    with open(text_file) as file_in:
        for line in file_in:
            match_a = re.findall('<title>(.+?)</title>', line)
            match_y = re.search('<li class="year">(.+?)</li>', line)
            match_p = re.findall('<div class="nr" id=(.+?)</div>', line)
        
            if(match_y):
                years.append(match_y.group(0))
            if (match_p):
                published = match_p
            if (match_a):
                 authors = match_a
        
        for papers in published:
            paper = papers.split('>')
            if(paper[1][1] == "j"):
                journals += 1
            elif(paper[1][1] == "c"):
                Conference_papers += 1

        for j in authors:
            author = j.split(": ")

        for year in years:
            curr_year = year.split("<")
            curr_year = curr_year[1].split(">")
            if( curr_year[1] != "2022" and curr_year[1] != "2021" and curr_year[1] != "2020" ):
                break
            else:
                d = data(author[1], curr_year[1], journals, Conference_papers)
                data_needed.append(d)


for i in range(1, 21):
    temp = "page" + str(i) + ".txt"
    parser(temp)

for data in data_needed:
    all_papers = (data.Journals + data.Conference_papers)
    num_authors = len(data_needed);
    




    





    


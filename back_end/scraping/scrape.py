from bs4 import BeautifulSoup
import requests
import sys
import summarizing.summarize

class Scraper():

    def scrape(self, link):
        try:
            html_text = requests.get(link)
            soup = BeautifulSoup(html_text.content.decode('utf-8'), features="lxml")
        except:
            with open('dataset_scraping/ulta/errored.txt', 'a', encoding="utf-8") as f:
                f.write(link + "\n")

        title = soup.find('title')
        print(title.text)
        paragraphs = soup.find_all('p')
        lists = soup.find_all('li')
        #list_result = self.filter_lists(lists)

        text = []
        for p in paragraphs:
            text.append(p)

        return text
    
    # def filter_lists(self, lists):

    #     for l in lists:
    #         # trying to manually filter out some of the short list text 
    #         if l.text.count(" ") > 2:
    #             #print(l.text)

    #     # ...


if __name__ == "__main__":
    
    link = sys.argv[1]

    paragraph_list = Scraper().scrape(link)
    print(paragraph_list)

    sum = summarizing.Summarizer()

    sum.summarize(paragraph_list[0])



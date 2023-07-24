from bs4 import BeautifulSoup
import requests
import sys

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

    def get_desc_text(self, desc) -> str:
        """ Converts a description into display-able text.
        
        EX: a raw description may look like:
        <a href="https://news.google.com/rss/articles/CBMiQmh0dHBzOi8vd25iZi5jb20vcHJlc3Mtc3VuLWJ1bGxldGluLXNoaWZ0LWRlbGl2ZXJ5LXBvc3RhbC1zZXJ2aWNlL9IBAA?oc=5" 
        target="_blank">Will Press & Sun-Bulletin Shift Delivery to the Postal Service?</a>&nbsp;&nbsp;<font color="#6f6f6f">wnbf.com</font>

        This function will return just:
        Will Press & Sun-Bulletin Shift Delivery to the Postal Service?

        """

        # if html
        if BeautifulSoup(desc, "html.parser").find():
            return self._scrape_desc_text(desc)
        else:
            return desc

    def _scrape_desc_text(self, html) -> list[str]:
        
        soup = BeautifulSoup(html, features="lxml")

        # In case there are multiple a tags, join the descriptions of all of them.
        links = soup.find_all('a')
        text = []

        for a in links:
            text.append(a.string)

        return '/n'.join(text)


if __name__ == "__main__":
    
    # link = sys.argv[1]

    # paragraph_list = Scraper().scrape(link)
    # print(paragraph_list)

    # sum = summarizing.Summarizer()

    # sum.summarize(paragraph_list[0])

    Scraper().get_desc_text("whatever")



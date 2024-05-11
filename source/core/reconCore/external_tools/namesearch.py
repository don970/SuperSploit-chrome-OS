from prompt_toolkit import PromptSession
import os
installation = f'{os.getenv("HOME")}/.SuperSploit'
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = FileHistory(f'{installation}/.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt

class NameSearch:
    @staticmethod
    def append(strs):
        with open(f"{installation}/.data/personSearch", "a") as file:
            file.write(strs)
            file.close()

    @staticmethod
    def write(strs):
        with open(f"{installation}/.data/personSearch", "w") as file:
            file.write(strs)
            file.close()


    @classmethod
    def simpleNamesSearch(cls, arg):
        name = input("Enter the name to search: ")
        sdb = ["facebook.com", "instagram.com", 'linkedin.com', "Avk.com", "twitter.com"]
        list1 = []
        print("Using site dictionary to perform a search return")
        for site in sdb:
            searchPhrase = f"https://www.google.com/search?q=site%3A%22{site}%22+%7C+intext%3A%22{name}%22"
            list1.append(searchPhrase)
        for x in list1:
            print(f"To search {sdb[list1.index(x)]} just copy the link and past it into a browser.")
            print(x)
    @classmethod
    def help(cls):
        print("""[OSNIT Help Menu]
help - Shows this help menu.
dorks - Returns a list of google dork links for the 
        name and various social media site. 
""")
        pass

    @classmethod
    def main(cls, args):
        print("OSNIT Name Search Tool")
        inputs = ["help", "dork"]
        funs = [cls.help, cls.simpleNamesSearch]
        while True:
            try:
                data = input("[ONST]: ")
                for x in funs:
                    funs[inputs.index(data)]()
                continue
            except Exception as e:
                print(e)
        return




import sys

from prompt_toolkit import prompt as input


def append(strs):
    with open(".data/personSearch", "a") as file:
        file.write(strs)
        file.close()

def write(strs):
    with open(".data/personSearch", "w") as file:
        file.write(strs)
        file.close()


def namesSearch():
    name = input("enter the name to search: ")
    generator = ("""URL: https://www.google.com/search?q=site%3Afacebook.com+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Atwitter.com+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Alinkedin.com+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Ainstagram.com+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Avk.com+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
Disposable providers:
	URL: https://www.google.com/search?q=site%3Ahs3x.com+intext%3A%225672685401%22
	URL: https://www.google.com/search?q=site%3Areceive-sms-now.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Asmslisten.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Asmsnumbersonline.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Afreesmscode.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Acatchsms.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Asmstibo.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Asmsreceiving.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Agetfreesmsnumber.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Asellaite.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Areceive-sms-online.info+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Areceivesmsonline.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Areceive-a-sms.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Asms-receive.net+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Areceivefreesms.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Areceive-sms.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Areceivetxt.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Afreephonenum.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Afreesmsverification.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Areceive-sms-online.com+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Asmslive.co+intext%3A%225672685401%22+%7C+intext%3A%2272685401%22
Reputation:
	URL: https://www.google.com/search?q=site%3Awhosenumber.info+intext%3A%22%2B5672685401%22+intitle%3A%22who+called%22
	URL: https://www.google.com/search?q=intitle%3A%22Phone+Fraud%22+intext%3A%225672685401%22+%7C+intext%3A%22%2B567265401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Afindwhocallsme.com+intext%3A%22%2B5672685401%22+%7C+intext%3A%225672685401%22
	URL: https://www.google.com/search?q=site%3Ayellowpages.ca+intext%3A%22%2B5672685401%22
	URL: https://www.google.com/search?q=site%3Aphonenumbers.ie+intext%3A%22%2B5672685401%22
	URL: https://www.google.com/search?q=site%3Awho-calledme.com+intext%3A%22%2B5672685401%22
	URL: https://www.google.com/search?q=site%3Ausphonesearch.net+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Awhocalled.us+inurl%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Aquinumero.info+intext%3A%2272685401%22+%7C+intext%3A%225672685401%22
	URL: https://www.google.com/search?q=site%3Auk.popularphotolook.com+inurl%3A%2272685401%22
Individuals:
	URL: https://www.google.com/search?q=site%3Anuminfo.net+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Async.me+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Awhocallsyou.de+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Apastebin.com+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Awhycall.me+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Alocatefamily.com+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=site%3Aspytox.com+intext%3A%2272685401%22
General:
	URL: https://www.google.com/search?q=intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22+%7C+intext%3A%2272685401%22
	URL: https://www.google.com/search?q=%28ext%3Adoc+%7C+ext%3Adocx+%7C+ext%3Aodt+%7C+ext%3Apdf+%7C+ext%3Artf+%7C+ext%3Asxw+%7C+ext%3Apsw+%7C+ext%3Appt+%7C+ext%3Apptx+%7C+ext%3Apps+%7C+ext%3Acsv+%7C+ext%3Atxt+%7C+ext%3Axls%29+intext%3A%225672685401%22+%7C+intext%3A%22%2B5672685401%22+%7C+intext%3A%2272685401%22""").split("\n")
    mainlist = []
    fishlist = []
    for x in generator:
        worklist = x.split("25672685401")
        mainlist.append(worklist)
    for xx in mainlist:
        strs = ''
        for i in xx:
            strs += i + name
        sys.stdout.write(strs)
    write(strs)

    return
namesSearch()
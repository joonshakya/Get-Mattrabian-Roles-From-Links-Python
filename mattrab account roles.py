# Insert account link in the form of python lists
account_link = [
    'https://www.askmattrab.com/users/45-joon-shakya',
]
















from bs4 import BeautifulSoup
import requests

name_and_post = []
print()

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

# Initial call to print 0% progress
l = len(account_link)
printProgressBar(0, l, prefix = 'Finding:', suffix = 'Complete', length = 50)
max_len = 0
for i, link in enumerate(account_link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    nameElement = soup.find(class_="name")
    if nameElement:
        name = nameElement.text.strip()
        max_len = len(name) if max_len < len(name) else max_len
        post = soup.find(class_="badge").text.strip().capitalize()
        name_and_post.append({
            'id': link[link.find("users") + 6:link.find("-") if link.find("-") != -1 else len(link)],
            'name': name,
            'post': post
        })
    printProgressBar(i + 1, l, prefix = 'Finding:', suffix = 'Complete', length = 50)

if max_len < 4:
    max_len = 4
print(f"\n\nID    | Name {' '*(max_len - 4)} | Post")
print('-'*6 + '|' + '-'*(max_len + 3) + '|' + '-'*11)
for person in name_and_post:
    print(person['id'] + ' '*(5 - len(person['id'])) + ' | ' + person['name'] + ' '*(max_len - len(person['name']) + 1) + ' | ' + person['post'])
print('\n\n')
input("Press enter to exit ")


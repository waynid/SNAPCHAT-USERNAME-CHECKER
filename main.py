import random
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import words
import time
import re
from colorama import Fore, Style, init

init(autoreset=True)
nltk.download('words')
pattern = re.compile("^[a-z]{1,15}$")
word_list = [w.lower() for w in words.words() if pattern.fullmatch(w.lower())]

headers = {
    "User-Agent": "Mozilla/5.0"
}

def check(username):
    url = f"https://www.snapchat.com/add/{username}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else ""
        if "@" in title:
            return f"{Fore.RED}[TAKEN]{Style.RESET_ALL} {username}"
        else:
            return f"{Fore.GREEN}[AVAILABLE]{Style.RESET_ALL} {username}"
    except Exception as e:
        return f"{Fore.YELLOW}[ERROR]{Style.RESET_ALL} {username} - {str(e)}"

while True:
    username = random.choice(word_list)
    result = check(username)
    print(result)
    time.sleep(1)

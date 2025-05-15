# Standard Python Libraries
import os
from imaplib import IMAP4_SSL
import email
from collections.abc import Iterable
# Third-Party Libraries
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests


load_dotenv()

username: str = os.getenv("EMAIL")
password: str = os.getenv("PASSWORD")


def connect_to_email() -> IMAP4_SSL:
    mail = IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    return mail


def extract_links_from_html(html_content: str) -> Iterable:
    soup: BeautifulSoup = BeautifulSoup(html_content, "html.parser")
    links = [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]
    return links


def click_link(link: str) -> None:
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print(f"Successfully visited: {link}")
        else:
            print(f"Failed to visit: {link}, Error code: {response.status_code}")
    except Exception as e:
        print(f"Error requesting link: {link}, Error: {e}")


def search_for_email():
    mail = connect_to_email()
    _, search_data = mail.search(None, '(BODY "unsubscribe")')
    data = search_data[0].split()

    links = []

    for num in data:
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    html_content = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    links.extend(extract_links_from_html(html_content))
                    #print(f"Found unsubscribe links in email: {msg['Subject']}")
        else:
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

            if content_type == "text/html":
                links.extend(extract_links_from_html(content))
                #print("Unsubscribe links found:")
    mail.logout()
    return links


if __name__ == "__main__":
    links = search_for_email()
    for link in links:
        click_link(link)
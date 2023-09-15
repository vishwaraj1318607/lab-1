#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

# The URL of the webpage to scrape
url = "https://www.uta.edu/academics/faculty"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <div> elements with class "list" and containing "==$0."
    list_divs = soup.find_all("div", class_="list", text="==$0.")

    # Extract and write the text content of each matching <div> element to a text file
    with open("list_divs_content.txt", "w", encoding="utf-8") as file:
        for div in list_divs:
            file.write(div.get_text() + "\n\n")

    print("Data saved to list_divs_content.txt")

else:
    print("Failed to retrieve the webpage")


# # Diagnostic Problem 1

# In[3]:


def compress_message(msg):
    compressed_msg = ""
    count = 1

    for i in range(1, len(msg)):
        if msg[i] == msg[i - 1]:
            count += 1
        else:
            compressed_msg += msg[i - 1] + (str(count) if count > 1 else "")
            count = 1

    compressed_msg += msg[-1] + (str(count) if count > 1 else "")

    return compressed_msg

# Read the input message
msg = input()

# Compress the message
compressed_msg = compress_message(msg)

# Print the compressed message
print(compressed_msg)


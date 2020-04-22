import lxml
import html5lib
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re
import urllib.request
from tqdm import tqdm

def get_links(url):
    ret_list = []
    
    r = requests.get(url)
    root = BeautifulSoup(r.content)
    
    divs = root.find_all(class_=re.compile("col-md-2 spiritDiv"))
    for div in divs:
        a = BeautifulSoup(str(div)).find("a")
        ret_list.append(a.attrs['href'])
    
    return ret_list

def download_images(root, links, path):
    failed_links = []
    
    for i in tqdm(range(0, len(links)), desc="Download Images:", position=0, leave=True):
        link = links[i]   
        if len(link.split(" ")) != 1:
            link = '%20'.join(link.split(" "))
            
        name = link.split("/")[-1]
        
        try:
            urllib.request.urlretrieve(root+link, path+name)
        except:
            failed_links.append(link)
    
    print(len(failed_links), "failed downloads")
    print('\n'.join(failed_links))

def main():
    links = get_links("http://smashbros-ultimate.com/spirits")
    download_images("http://smashbros-ultimate.com/", links, "img/")

main()
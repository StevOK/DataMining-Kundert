# Steven Kundert
# CMPS 5443 Data Mining - Griffin
# Assignment 2 - Scraping Data
# 9/18/17
# This program will go to _______ and scrape _______


#This is the example code, will replace later

import sys
import requests
import bs4
from bs4 import BeautifulSoup
import time
import random


emp_details = []

for i in range(9,10):
    letter = chr(i+65)
    url = "https://mwsu.edu/profiles/people.asp?browse="+letter
    print(url)
    

    # Beautiful soup way
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    people = soup.findAll('tr',{'class',"person__item"})
    for person in people:
        subperson = person.findNext('td',{'class':'col-sm-10'})
        name = person.findNext('h3').text
        dept = person.findNext('h4')
        deptName = dept.findNext('a').text
        title = dept.findNext('small').text
        
        # Hacky way to get office
        office = subperson.find('div',{'class':'row'})
        for c in office.children:
            for cc in c:
                if isinstance(cc,bs4.element.NavigableString) and len(cc) > 10:
                    officelocation = cc.strip()
                    

                
        anchors = subperson.findAll('a')
        email = anchors[0].text
        phone = anchors[-1].text
        
        person_dict = {}
        person_dict['deptName'] = deptName.strip()
        person_dict['title'] = title.strip()
        person_dict['name'] = name.strip()
        person_dict['email'] = email.strip()
        person_dict['phone'] = phone.strip()
        person_dict['officelocation'] = officelocation.strip()
        emp_details.append(person_dict)
        time.sleep(random.randint(0,3))
           

print(emp_details)

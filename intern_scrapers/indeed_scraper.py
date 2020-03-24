# pip install mysql-connector-python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import datetime
import logging
import mysql.connector

def main():
    logging.basicConfig(level=logging.INFO, filename="scraper.log") 
    logger = logging.getLogger()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mel0nl0rd!",
        database="internships",
        auth_plugin="mysql_native_password"
    )

    url = "https://www.indeed.com/jobs?q=Intern&l=San+Francisco,+CA&radius=100&sort=date&start=0"
    # page = requests.get(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36"})
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    job_list = soup.find_all("div", class_ = "jobsearch-SerpJobCard unifiedRow row result clickcard")
    for job in job_list:
        position = job.find("a", class_ = "jobtitle turnstileLink").text[1:]
        company = job.find("span", class_ = "company").text[2:]
        location = job.find("div", class_ = "recJobLoc")["data-rc-loc"] #.text
        city = location[0:location.find(",")]
        state = location[location.find(",") + 2:]
        collection_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # print("Position: " + position)
        # print("Company: " + company)
        # print("Location: " + location)
        # print("City: " + city)
        # print("State: " + state)
        # print("Collection date: " + collection_date)
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO jobs (position, company, city, state, url, collection_date) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (position, company, city, state, url, collection_date)
        mycursor.execute(sql, val)
        mydb.commit()

    print("Inserted")

if __name__ == "__main__":
    main()
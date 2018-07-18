import re
import time
import datetime
import sqlite3
import traceback
import smtplib
import logging
import os
import zipfile

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.remote.remote_connection import LOGGER

def selenium_scraping_firefox(delay=3.5):
    print("{} Script started, fetching elements...".format(datetime.datetime.today().strftime("%H:%M:%S")))
    #I have opted to grab the website with selenium, initially requests was tested however it failed to grab the website since the request is performed before the page is fully loaded and there is no option to delay it
    #Can access the website straight through following the values details from the cookies from requests

    #setting a headless browser
    options = Options()
    options.set_headless(headless=True)

    #spoofing the user agent & removing elements to speed up selenium
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0")
    firefox_profile.set_preference("permissions.default.stylesheet", 2)
    firefox_profile.set_preference("permissions.default.image", 2)

    driver = webdriver.Firefox(firefox_options=options, firefox_profile = firefox_profile, log_path='/dev/null')
    driver.get("https://www.bet365.es/en/")

    #first connection is directed to landing page and cookies are injected in the browser, we then access the tennis url
    driver.get("https://www.bet365.es/?oty=2#/AC/B13/C1/D50/E2/F163/P^50/Q^2/I") #option ?oty=2 in url toggles between fractional (1) and decimal (2) odds
    time.sleep(delay) #delayed to ensure the page loads up
    parser = BeautifulSoup(driver.page_source, "lxml")
    scraped_on = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") #to be displayed on the csv
    driver.quit()
    #this will give us each of the containers for each tournament, will pick up an extra div we slice off
    containers = parser.find_all("div", class_="gl-MarketGrid")[0].contents[0:-1]
    print("{} All elements fetched".format(datetime.datetime.today().strftime("%H:%M:%S")))
    return containers, scraped_on

def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(os.path.join(path, 'chromedriver'),chrome_options=chrome_options)
    return driver

def selenium_scraping_chrome(delay=3.5):
    user_agent_chrome = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    driver = get_chromedriver(use_proxy=False, user_agent=user_agent_chrome)
    driver.get("https://www.bet365.es/en/")
    driver.get("https://www.bet365.es/?oty=2#/AC/B13/C1/D50/E2/F163/P^50/Q^2/I")
    time.sleep(delay) #delayed to ensure the page loads up
    parser = BeautifulSoup(driver.page_source, "lxml")
    scraped_on = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") #to be displayed on the csv
    driver.quit()
    #this will give us each of the containers for each tournament, will pick up an extra div we slice off
    containers = parser.find_all("div", class_="gl-MarketGrid")[0].contents[0:-1]
    print("{} All elements fetched".format(datetime.datetime.today().strftime("%H:%M:%S")))
    return containers, scraped_on
    
def selenium_scraping_initiate():
    service_args = [
    '--proxy=TOBEADDED',
    '--proxy-type=https',
    '--proxy-auth=TOBEADDED',
    ]
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246")
    
    driver = webdriver.PhantomJS(service_args=service_args,desired_capabilities=dcap, service_log_path="/dev/null")
    driver.get("https://www.bet365.es/en/")
    return driver

def selenium_scraping_phantomjs(driver, delay=46.5):  #delay set to 46.5 to ensure each run takes at least 1 min to avoid IP bans
    #first connection is directed to landing page and cookies are injected in the browser, we then access the tennis url
    driver.get("https://www.bet365.es/?oty=2#/AC/B13/C1/D50/E2/F163/P^50/Q^2/I") #option ?oty=2 in url toggles between fractional (1) and decimal (2) odds
    time.sleep(delay)
    #driver.save_screenshot('out2.png')
    parser = BeautifulSoup(driver.page_source, "lxml")
    scraped_on = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") #to be displayed on the csv
    #driver.quit()
    #this will give us each of the containers for each tournament, will pick up an extra div we slice off
    containers = parser.find_all("div", class_="gl-MarketGrid")[0].contents[0:-1]
    print("{} All elements fetched".format(datetime.datetime.today().strftime("%H:%M:%S")))
    return containers, scraped_on

def email_notification(error):
    with open("./start.py") as f:
        setup = f.read()
    subject = "EXCEPTION RAISED"
    
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('test@outlook.com', setup)
    smtpObj.sendmail('test@outlook.com', 'mail@outlook.com', 'Subject: {}\n\n{}'.format(subject,error))
    smtpObj.quit()
    

class Match:
    
    def __init__(self,scraped_on):
        self.scraped_on = scraped_on
        self.female = ["WTA", "ITF Women", "Fed Cup", "Women"]
        self.male = ["ATP", "Challenger", "ITF", "Davis Cup", "Roland Garros", "Australian Open", "US Open", "Wimbledon"]
        self.headers = "tournament_header, sex, tournament_class, singles_doubles, qualifier, round_match, time_match, player1, player2, odds_player1, odds_player2, scraped_on\n"
        self.filename = "bet365_scraping3.csv"
        
    def tournaments(self,container):
        tournament_header = container.find_all("span", class_="cm-CouponMarketGroupButton_Text")[0].text

        sex = "N/A"
        for i in self.male:
            if re.search(i, tournament_header) != None:
                if re.search("^ITF\sWomen", tournament_header) != None:  #will ensure if starts by ITF is classed right
                    continue
                sex = "male"
        for i in self.female:
            if re.search(i, tournament_header) != None:
                sex = "female"

        tournament_class = "N/A"
        for i in (self.male+self.female)[:-1]:
            if re.search(i, tournament_header) != None:
                tournament_class = i

        if " WD"  in tournament_header or " MD" in tournament_header:
            singles_doubles = "doubles"
        else:
            singles_doubles = "singles"

        if " Qual" in tournament_header:
            qualy = "qualifier"
        else:
            qualy = ""

        round_match = re.sub("\sMatches", "", (re.sub(".*\\s-\\s", "", tournament_header)))

        self.tournament_header = tournament_header 
        self.sex = sex
        self.tournament_class = tournament_class
        self.singles_doubles = singles_doubles
        self.qualy = qualy
        self.round_match = round_match     
    
    def matches(self, container):
        return self.parse_times(container), self.parse_players(container), self.parse_odds(container)

    def parse_times(self,container):
        times = container.find_all("div", class_=re.compile("sl-CouponParticipantWithBookCloses_LeftSideContainer"))
        all_dates_games = container.find_all("div", class_=re.compile(".*sl-MarketHeaderLabel_Date.*"))
        day_played = container.find_all("div", class_=re.compile(".*sl-MarketHeaderLabel_Date.*"))[0].text
        day_played_year = datetime.datetime.strptime(day_played  + " " + str(datetime.datetime.now().year), "%a %d %b %Y").strftime("%Y-%m-%d")

        def date_convert(date):  #append the year and format it to ISO standard
            new_date = datetime.datetime.strptime(date  + " " + str(datetime.datetime.now().year), "%a %d %b %Y").strftime("%Y-%m-%d")
            return new_date

        def number_games_new_date(dates):  #only supports 2 diff dates per tournament
            if len(dates) > 1:
                counter = 0
                dates_new = dates[1]
                for i in range(len(times)):
                    if dates_new == None: #blank match container is last one
                        break
                    else:
                        dates_new = dates_new.next_sibling #moves to next match container
                        counter +=1
            return counter-1

        times_fixed = [re.sub(".*", "Live", time.text) if "Live" in time.text else time.text for time in times] #when the tag Live is on, raw data format is inconsistent
        time_matches = []
        for index,time_match in enumerate(times_fixed):
            if (len(all_dates_games) > 1) and ((index+1) > (len(times) - number_games_new_date(all_dates_games))):
                new_date = date_convert(all_dates_games[1].text)
                time_matches.append(new_date + " " + str(time_match))
            else:
                time_matches.append(day_played_year + " " + str(time_match))
        return time_matches

    def parse_players(self, container):
        names = container.find_all("div", class_="sl-CouponParticipantWithBookCloses_NameContainer ")
        player1 = [(re.sub("\\svs\\s.*", "", name.text)) for name in names]
        player2 = [(re.sub(".*\\svs\\s", "", name.text)) for name in names]
        return player1, player2

    def parse_odds(self, container):
        #dynamic classes all named the same, we will pick the one where column equals 'x' and then move to the parent directory
        column_odds1 = container.find_all("div", class_= "gl-MarketColumnHeader ")[0]
        column_odds2 = container.find_all("div", class_= "gl-MarketColumnHeader ")[1]

        odds_player1 = column_odds1.parent.find_all("div", class_=re.compile("OddsOnly"))
        odds_player1_list = [odd1.text for odd1 in odds_player1]
        odds_player2 = column_odds2.parent.find_all("div", class_=re.compile("OddsOnly")) 
        odds_player2_list = [odd2.text for odd2 in odds_player2]
        return(odds_player1_list, odds_player2_list)
    
    def create_csv(self):
        with open(self.filename, "w") as f:
            f.write(self.headers)
        print("{} File '{}' created".format(datetime.datetime.now().strftime("%H:%M:%S"), self.filename))
        
    def write_csv(self,containers):
        self.create_csv()
        with open(self.filename, "a") as f:
            print("{} Writing data to csv file".format(datetime.datetime.today().strftime("%H:%M:%S")))
            for container in containers:
                self.tournaments(container)
                tournament_matches = self.matches(container)
                for i in range(len(tournament_matches[0])):
                    matches_data = (tournament_matches[0][i] + "," + tournament_matches[1][0][i] + "," + tournament_matches[1][1][i] + "," + tournament_matches[2][0][i] + "," + tournament_matches[2][1][i])
                    f.write(self.tournament_header + "," + self.sex + "," + self.tournament_class + "," + self.singles_doubles + "," + self.qualy + "," + self.round_match + "," + matches_data + "," + self.scraped_on + "\n")
        print("{} Finished".format(datetime.datetime.today().strftime("%H:%M:%S")))
 
    def create_sql(self):
        conn = sqlite3.connect("tennis.db")
        curr = conn.cursor()
        table_schema = '''CREATE TABLE matches(
            tournament_header TEXT,
            sex TEXT,
            tournament_class TEXT,
            singles_doubles TEXT,
            qualifier TEXT,
            round_match TEXT,
            time_match TEXT,
            player1 TEXT,
            player2 TEXT,
            odds_player1 NUMERIC,
            odds_player2 NUMERIC,
            scraped_on DATETIME
            );'''
        curr.execute(table_schema)
        conn.close()
        
    def write_sql(self,containers):
        try:
            conn = sqlite3.connect("tennis.db")
            curr = conn.cursor()

            print("{} Writing data to SQL database".format(datetime.datetime.today().strftime("%H:%M:%S")))
            counter_new_matches = 0
            
            for container in containers:
                self.tournaments(container)
                tournament_matches = self.matches(container)
                for i in range(len(tournament_matches[0])):
                    match_all_vars = [self.tournament_header, self.sex, self.tournament_class, self.singles_doubles, self.qualy, self.round_match, tournament_matches[0][i], tournament_matches[1][0][i], tournament_matches[1][1][i], tournament_matches[2][0][i], tournament_matches[2][1][i], self.scraped_on]
                    unique_fields = tuple(field for index, field in enumerate(match_all_vars) if index in [0,7,8,9,10])
                    curr.execute("""SELECT tournament_header, player1, player2, odds_player1, odds_player2
                                    FROM matches
                                    WHERE tournament_header = ? AND player1 = ? AND player2 = ? AND odds_player1 = ? AND odds_player2 = ?
                                    """, (unique_fields))
                    if (curr.fetchone() == None) and ("Live" not in match_all_vars[6]):  #filtering already started games
                        counter_new_matches += 1
                        curr.execute("INSERT INTO matches VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", match_all_vars)
                        conn.commit()
        finally:
            conn.close()
            print("{} Finished. {} New matches/Changes in odds added.".format(datetime.datetime.today().strftime("%H:%M:%S"), counter_new_matches))


if __name__ == "__main__":
    try:
        phjs_driver = selenium_scraping_initiate()
        while True:
            try:
                containers,scraped_on = selenium_scraping_phantomjs(phjs_driver)
            except IndexError:
                print("{} Error fetching the data, retrying...".format(datetime.datetime.today().strftime("%H:%M:%S")))
                containers,scraped_on = selenium_scraping_phantomjs(phjs_driver)        
            tennis_scraper = Match(scraped_on)
            tennis_scraper.write_sql(containers)
            time.sleep(11)
    except:
        error_info = traceback.format_exc()
        email_notification(error_info)
        print(error_info)

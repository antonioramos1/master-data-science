# Web scraping betting website

The goal of this project is to web scrape tennis matches creating a database of each match and capturing any fluctuation on the odds as close to real time as possible.  

Phase 2 involves using business knowledge of the tennis market betting scene and perform data analysis and machine learning techniques to the resulting dataset. 

Due to the challenges encountered while scraping the website Phase 2 has been discarded.


### Dependencies

- SQLite
- Selenium
- PhantomJS
- Private proxy
- Server / RaspberryPI / other

### Caveats
- Selenium has been used to circumvent issues that other libraries such as Requests had loading up the Javascript dynamic content.

- The script has been run on a Digital Ocean droplet with the least resource config (1GB $5) to cater for the real time data requirement. Vouchers are available to cover up to the first $10 of expenses.

- A private proxy connection ($4) was used for this project since IPs are geographically tracked by the website to grant access in this case to the Spanish site.

- Although functionality for Chrome and Firefox has been built, the final script runs on PhantomJS since this is the only browser that supported proxy authentication while using Selenium. Also, User Agent info has been spoofed to avoid being detected and blocked.

### Outcome
After overcoming many challenges, eventually managed to run the script successfully for a few hours, however the proxy IP ended up blacklisted.  

Additional steps can still be taken ie. Introducing random delays to the connections, however this is not guaranteed to mask the bot.

Another option would be alternating between a group of proxys which would increase the cost of the project, however this would increase the cost of this project and there is no guarantee that the website will not detect these connections as non user traffic. 

Due to the cost of exploring further options I have decided to pull back from this project.

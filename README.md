# DataSciencePortfolio
A collection of selected data science projects to demonstrate skill sets, knowledge, and what I find interesting. This also gives me the perfect opportunity to manage this repo via git through git bash.

## Contents
- PythonWebScraping:
  - WebScrapingASong: Web scraped "she's a rebel" by GreenDay by using **BeautifulSoup**. Used a bit of REGEX and `INSPECT ELEMENT` to scrape clean/required lyric.
  - DollarTreeOntarioLocations: Web scraped Dollar Tree locations present in Ontario by using **BeautifulSoup**. Scraped the addresses and geolocations by working with json, regex and `INSPECT ELEMENT`. Plotted the locations of the stores on a map in python.
- BasicCodingProblems:
  - Python:
    - 1_217_ContainsDuplicate.ipynb: first practice python challenge from leetcode. 
- MyFitbitSleepCycle:
  - I bought a Fitbit during my last semester (9th Feb 2021) of university with the intention of tracking and analysing my sleep quality. Extracted my data in json files through an API and analysed my sleeping patterns at different stages of my life (my time from my last semester of uni till I satrted powerlifting post data science bootcamp). Got to do parametric and non parametric tests. This project took me 9 days to complete.
  - [Video Summary](https://youtu.be/qwMC3FuT74M)
- RapLyricsGenerator:
  - I was catching up with a friend from Bahrain over a video call sometime in November 2021. That's when we brought up about how we used to share earphones and listen to rap music together on his mp3 on the school bus back home. That got us talking about our current taste in music and our appreciation for lyrical rap. That's when I thought of building a rap lyrics generator achieved through a Recurrent Neural Network. This project took me 11 days to complete and the most tedious part was this project was extracting data (through Genius API) and debugging the aws related code. I locally deployed the generator on a web application through streamlit. In addition to that, the web application accesses the trained RNN model from an AWS S3 bucket on which I'm hosting on. 
- BikeShareToronto:
  - Started biking to the gym with my roommate during the summer of 2021. While he had his own bike, I would rent a bike for every use from Bike Share Toronto. We'd ride to the gym during sunny and rainy days. That got me thinking of this service's usage. After getting my hands on 5 years’ worth of data, I got to perform time-series analysis on SARIMA and F-Prophet models by first confirming the stationarity of the data by performing ADF and KPSS tests on it. In addition to that, I created an interactive Tableau dashboard that revolved around the top 20 busiest stations. Was able to complete this project in 5 days. 

## In Progress
- PythonWebScraping:
  - WebScrapingAnAlbum: Web scraping an album.
  - WebScrapingAnAppReview: Web scraping user reviews off a certain app for future NLP work. Same foundation used for the BrainStation x McDonald's hackathon.
  - WebScrapingTweets: Scraping tweets of BigMouth Season 4 off twitter from users.
- DollarTreeOntarioStoreFinder: Build off of **DollarTreeOntarioLocations** and design a system that will find the closest store to any given location in Ontario.
- BigMouth_S4_NLP: Getting to know the opinions of people on BigMouth's season 4 on Netflix off twitter tweets. Idea popped into my head after talking to my best friends from Bahrain.

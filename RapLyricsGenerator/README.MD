# RapLyricsGenerator
I was catching up with a friend from Bahrain over a video call sometime in November 2021. That's when we brought up about how we used to share earphones and listen to rap music together on his mp3 on the school bus back home. That got us talking about our current taste in music and our appreciation for lyrical rap. That's when I thought of building a rap lyrics generator achieved through a Recurrent Neural Network. This project took me 11 days to complete and the most tedious part was this project was extracting data and debugging the aws related code.

## Summary
Initially used Selenium and BeautifulSoup to scrape lryics off AZLyrics by navigating through URLs. Extracting process wasn't successful when certain URLs didn't follow the standard format that other songs used. Since the project revolved around rap music, I was able to use the API of [Genius](https://genius.com/) to scrape lyrics off rappers. The dataframe containing the lyrics was cleaned using regex and nltk. I then used an RNN (tensorflow) with 50 epochs (would've opted for more if it wasn't so time consuming) to identify cadence, flows etc. which I then used for my recommender system. I then built a web application through streamlit and hosted my trained RNN model on one of my AWS S3 buckets from which the application reads from. Ideally, I would've hosted it on Heroku but I would've had to pay a monthly fee in order to keep it running. Instead, here's the demo of it being hosted locally: https://youtu.be/JNiABudFnqI

## Improvements / Future work
- Scrape mumble rap lyrics to give the recommender system a new genre/style of predicting lyrics. Who knows, I can potentially bring rise to the newest soundcloud rapper (LOL)

## Notebooks
- WebScrapingSongNames: The purpose of this notebook was to scrape the names of rap songs by going through the URLs of rappers on [AZLyrics](https://www.azlyrics.com/). This was achieved through Selenium
- LyricalLyricsScraping: The purpose of this notebook was to loop through artists and their song names through attain its lyrics by navigating through the URLs of AZLyrics. Eventually put all 3 information into a dataframe to work with. Sadly, this didn't follow through due to the inconsistent URL naming convention 
- ScrapingLyricsWithGeniusAPI: The purpose of this notebook was to loop through artists, their song names and lyrics and put them into a dataframe by using the Genuis API. However, due to the API timing out (despite the highest timeout setting) I had to manually extract the data instead of letting it extract overnight
- CleaningData: The purpose of this notebook is to clean the lyrics column in the dataframe
- ModellingLyrics: The purpose of this notebook is to create and train the RNN, and create a recommender system 
- webapp_RapLyricsGenerator: Pupose of this script is to locally host the recommender system on a web application through streamlit

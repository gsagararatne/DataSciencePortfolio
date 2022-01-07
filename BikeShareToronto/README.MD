# BikeShareToronto
I started biking to the gym with my roommate during the summer of 2021. While he had his own bike, I would rent a bike for every use from Bike Share Toronto. We'd ride to the gym during sunny and rainy days. That got me thinking of this service's usage. I was able to download 5 years of data from [here](https://open.toronto.ca/dataset/bike-share-toronto-ridership-data/) and performed time-series analysis. 

## Summary
After I downloaded the usage data and created a proper dataframe out of it, I gave time-series a go. I first explored its stationarity by conducting Augmented Dickey-Fuller (ADF) and  (KPSS) tests to see if the data was stationary. The ADF test indicated that the data was not stationary, but when done on its log, seemed to be stationary. The KPSS test concluded that the series was stationary around the deterministic trend. After that, I started building a SARIMA model since Seasonality was present in this data set. After exploring the autocorrelation function (acf) and partial autocorrelation function (p_acf), I was able to identify the p,d and q terms required. I did not stop there, and created a loop to identify ideal p,d and q scores by comparing MAE scores. With my findings being unsatisfactory, I looked into F-prophet and found a model with a much better MAE score! That being said, I forecasted 2 years worth of data using pyramid-arima and F-Prophet models, but am more confident with the findings from F-Prophet.

Lastly, I created an interactive Tableau dashboard that looked into the top 20 bussiest stations to understand the usage trends of members and non-members.

## Improvements / Future work
- Cleaning the dataset to give better results on the Tableau dashboard
    - Especially the data present in 2018. Member data seem to be missing. Will need to dwelve in deeper

## Notebooks
- BikeShareTimeSeries
    - The purpose of this notebook was to model timeseries after importing the csv dataset 
- CleaningBikeShareToronto
    - The purpose of this notebook was to merge all individual csv files into one main dataframe and clean it
- CleaningBikeShareToronto_full
    - The purpose of this notebook was to merge all individual csv files into one main dataframe and export it as a main csv file without cleaning it

## Dashboard
https://public.tableau.com/views/TorontoBikeShare_16415028869190/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link 
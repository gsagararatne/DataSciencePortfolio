# FitbitSleepAnalysis
Analysing my quality of sleep and activity levels during different parts of my life.

Video summary: https://youtu.be/qwMC3FuT74M

## Notebooks
- ExtractingFitbitJsonData: The purpose of this notebook is to extract data from a fitbit API into respective json files.
- ExtractingFitbitCsv: The purpose of this notebook is to read in all the extracted json files, put the required data into a DataFrame and then export them as csv files.
- FitbitSleepAnalysis: The main notebook where I imported my fitbit csv files and ran my analysis.

## Required Libraries
- pandas
- numpy
- simplejson
- datetime
- sleep
- requests
- cherrypy
- scipy
- matplotlib
- seaborn

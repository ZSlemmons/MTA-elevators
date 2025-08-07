A project looking into MTA elevator outages and accessebility

Terms: 
Subway station: For the purpose of this analysis, a “station” is defined as a subway stop consisting of tracks with service in both directions. For example, the Times Square complex contains 4 stations – a station for the 1-2-3, a station for the N-Q-R, a station for the 7, and a station for the Shuttle.

Rules: 
Several city subway stations are accessible in only one direction. For the purpose of this analysis, we have chosen to include them in the count of accessible stations. 
In most instances, the average is defined as the mean of the data. However, in the case of elevator outage durations, the median was used to calculate the average. This is because one elevator was under repair for more than 400 days, an extreme outlier which drastically skewed the mean. 

Overview: 

For this story, we first began with establishing the number of accessible stations in the city, and the percent of total stations that are accessible. According to the MTA, that number is around 33%. When we analyzed the data, that proved to be true. 

By mapping out those stations, we were then able to calculate the average distance between stations using a QGIS distance matrix.

The difference in travel time between regular and accessible commutes was calculated using the MTA’s own directions API. Two random samples of 100 New York City addresses were collected from usps.biglocalnews.org, and were then run through the API as origins and destinations. The same sets of addresses were then run through the API again, with a “wheelchair accessible” parameter. Both commutes used the “quickest” parameter to ensure that the first route option returned would be the fastest possible commute. The difference in commute times were then averaged. 

To control for commutes that were naturally accessible on both ends and therefore identical, we removed those commutes from the dataset and performed the analysis again. Both results were included in our reporting. 

To look at where accessible stations were concentrated in comparison to where people with ambulatory disabilities lived, we used a combination of American Community Survey census data and NYC open data on neighborhoods. Some manual cleaning was necessary to get these to line up, and areas that could not be cleanly matched, were identified on the resulting map as “data not available.”


To examine elevator outages, multiple data sets were used. New York State open data provided a log of outages from 2015-2025. However, that dataset only recorded outages per month, offering almost no insight into how long each outage lasted. To fill in that gap in information, we used the MTA’s equipment outage API to scrape data on outages every hour for several days. This data was then used in the analysis to get a better breakdown of the cause of each outage, as well as the duration of the outages. 



Data Sources:
MTA station data: https://catalog.data.gov/dataset/mta-subway-stations
MTA outage data: https://www.mta.info/elevator-escalator-status
Elevator complaints: https://data.ny.gov/Transportation/MTA-NYCT-Subway-Elevator-and-Escalator-Availabilit/rc78-7x78/explore/query/SELECT%0A%20%20%60month%60%2C%0A%20%20%60borough%60%2C%0A%20%20%60equipment_type%60%2C%0A%20%20%60equipment_code%60%2C%0A%20%20%60total_outages%60%2C%0A%20%20%60scheduled_outages%60%2C%0A%20%20%60unscheduled_outages%60%2C%0A%20%20%60entrapments%60%2C%0A%20%20%60time_since_major_improvement%60%2C%0A%20%20%60am_peak_availability%60%2C%0A%20%20%60am_peak_hours_available%60%2C%0A%20%20%60am_peak_total_hours%60%2C%0A%20%20%60pm_peak_availability%60%2C%0A%20%20%60pm_peak_hours_available%60%2C%0A%20%20%60pm_peak_total_hours%60%2C%0A%20%20%60_24_hour_availability%60%2C%0A%20%20%60_24_hour_hours_available%60%2C%0A%20%20%60_24_hour_total_hours%60%2C%0A%20%20%60station_name%60%2C%0A%20%20%60station_mrn%60%2C%0A%20%20%60station_complex_name%60%2C%0A%20%20%60station_complex_mrn%60%0AORDER%20BY%20%60month%60%20ASC%20NULL%20LAST/page/filter
Metro lines shapefile: https://geo.nyu.edu/catalog/nyu-2451-34758
London data: https://data.london.gov.uk/dataset/accessibility-london-underground-stations/
MTA APIs: https://api.mta.info/#/EAndEFeeds
NTA info: https://data.cityofnewyork.us/City-Government/2020-Neighborhood-Tabulation-Areas-NTAs-/9nt8-h7nd/about_data
Disability data: https://public.tableau.com/app/profile/nyc.health/viz/NewYorkCityNeighborhoodHealthAtlas/Home
MTA 2025 budget: https://www.mta.info/document/151266




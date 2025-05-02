# Team Member: Brad Leonard

## fishbone
1. weather
 * temperature
  * feels like
 * humidity
 * solar radiation
 * air pollution
2. ridability
 * visibility
 * wind speed
 * precipitation
  * rainfall
  * snowfall
3. scheduling
 * day of week
 * holiday
 * season
4. infrastructure
 * traffic
 * usage
  * taxi
  * subways
  * buses
  * bikes

## background slide ideas
---
* Introduces the topic with necessary background information.​
  * Bike rentals are a service, usually a subscription service, in which there are many bike stations across a given area
  * At these stations, customers can take a bike, ride to another station, and drop the bike off there
* Provides a review of relevant literature, properly cited, highlighting successes and shortcomings of each study and how each relates to this study​
  * Variations on bike rental demand prediction studies generally predict hourly data, focus on major cities, use ML​
  * One study using daily models, uses GAM (generalized additive models)​
  * Most common non-time or location related factors related to weather (precipitation, visibility, temperature, season, wind speed), other factors related to the day of the week, holidays
* Describes how this study builds upon prior similar studies.​
* Establishes the study’s context.​
  * 
* Describes this research’s significance and potential impact.​
  * 
* Explains the relevance and importance of the study area.​
  * Gives an alternate, low-cost, low-maintenance transportation option to those who frequently travel in a specific area
  * Cars heavily contribute to CO2 emissions and therefore climate change, relying less on cars for transportation is a positive and improving the UX of bike rental systems is key to making them appealing
* Clearly identifies the problem or research gap​
  * The issue is balancing maintenance needs with customer satisfaction
* Clearly defines the study's objectives and boundaries.​
  * Predicting the daily demand of a bike rental company

"A bike rental company with a fleet of 4,000 bikes wants to optimize its operations by predicting daily rental demand. Accurate forecasts would enable the company to implement a rotating maintenance schedule while ensuring sufficient bike availability for customers each day. Since servicing typically takes one day and can only be conducted on operational days, the company needs a reliable prediction model to balance maintenance needs with customer satisfaction."

"describes prior literature supporting the importance of this problem and how it affects people" VERSUS "state the business question, provide a little background about why it is important"

GO TO GOOGLE SCHOLAR AND SEARCH BIKE RENTALS

- [X] [Modeling of the daily dynamics in bike rental system using weather and calendar conditions: A semi-parametric approach](https://www.sciencedirect.com/science/article/pii/S2468227624001571)

- DC
- affected by visibility, windspeed, season, working day, maintenance
- negatively affected by spring and winter
- penalized splines quasi-poisson
- generalized additive models (GAM)
  - mix between parametric and non-parametric, research more

---
- [X] [Investigation on the effects of weather and calendar events on bike-sharing according to the trip patterns of bike rentals of stations](https://www.sciencedirect.com/science/article/pii/S0966692317304659) - weather (heat waves), time, station-based clustering, temperature humidity index (THI)/weekend vs weekday/traffic/day of week, daejeon SK
- [X] [Forecasting Bike Rental Demand Using New York Citi Bike Data](https://arrow.tudublin.ie/scschcomdis/79/) - "How many bikes will meet users’ demand in a future certain time", random forest, hourly, weather/location/user info
- [ ] [A forecast for bicycle rental demand based on random forests and multiple linear regression](https://ieeexplore.ieee.org/abstract/document/7959977?casa_token=i_Vln_jViJ0AAAAA:ZDRyMmQaikgiRCKz-8H6uZi1I8U0ZYZsOWUlBTwLvIN3FemNMUoDgW-pH5V7BgA-uxS7BpU) - SPSS regression less accurate than random forest, hourly, temp/feels like/humidity/wind speed
- [ ] [Forecasting Bike Rental Demand](https://cs229.stanford.edu/proj2014/Jimmy%20Du,%20Rolland%20He,%20Zhivko%20Zhechev,%20Forecasting%20Bike%20Rental%20Demand.pdf) - conditional inference tree model, hourly, temp/feels like/humidity/wind speed/day of week
- [X] [Demand cycles and market segmentation in bicycle sharing](https://www.sciencedirect.com/science/article/pii/S030645731830503X?casa_token=S1uQTIQmAOwAAAAA:9IQavBFEkSihVIDT0he-rHFL_qQ1snrqtD2UWFe_D_Te3yAJnoaYbNPV15f9Tk7bgO_XelmF) - ML, weather/air quality/time/location, hourly, ???
- [X] [Predicting bike sharing demand using recurrent neural networks](https://www.sciencedirect.com/science/article/pii/S1877050919302364) - LSTM, time-based, renting and returning, usage data
- [ ] [A predictive analytics approach for forecasting bike rental demand](https://www.sciencedirect.com/science/article/pii/S2772662224000869) - same dataset
- [ ] [Unreliability of Delay Caused by Bike Unavailability in Bike Share Systems](https://journals.sagepub.com/doi/abs/10.1177/0361198120916136?journalCode=trra) - no access
- [ ] [Optimizing Bike Rental Demand Forecasting - An Ensemble Machine Learning Approach](https://ieeexplore.ieee.org/abstract/document/10810973?casa_token=2B1eoUNTKfQAAAAA:XctmIv1H3TPX_meonTSbf2vC5iQeWrs74pQSumqTlVhaQW1hNe_yQkxiDAO3hbZkn2YvZp0) - no access
---
some useful news articles

- [ ] [Comptroller report shows Citi Bike service is unreliable in many neighborhoods](https://ny1.com/nyc/all-boroughs/transit/2023/11/16/comptroller-report-shows-citi-bike-service-is-unreliable-in-many-neighborhoods)
- [ ] [‘Completely Unreliable’: Full Citi Bike Docks Cut Off Red Hook Even More](https://nyc.streetsblog.org/2024/08/22/completely-unreliable-full-citi-bike-docks-cut-off-red-hook-even-more)
---
studies that are interesting but not as directly related

- [ ] [An exploratory study of the bike rental system](https://www.researchgate.net/publication/334401657_An_exploratory_study_of_the_bike_rental_system)
- [ ] [Data-driven rebalancing methods for bike-share systems](https://people.orie.cornell.edu/shane/pubs/BSOvernight.pdf)
- [ ] [The Robust Bike Sharing Rebalancing Problem: Formulations and a Branch-and-Cut Algorithm](https://optimization-online.org/2023/10/the-robust-bike-sharing-rebalancing-problem-formulations-and-a-branch-and-cut-algorithm/)
- [ ] [Investigation on the effects of weather and calendar events on bike-sharing according to the trip patterns of bike rentals of stations](https://www.sciencedirect.com/science/article/pii/S0966692317304659)
- [ ] [Forecasting Bike Rental Demand Using New York Citi Bike Data](https://arrow.tudublin.ie/scschcomdis/79/)
- [ ] [A forecast for bicycle rental demand based on random forests and multiple linear regression](https://ieeexplore.ieee.org/abstract/document/7959977?casa_token=i_Vln_jViJ0AAAAA:ZDRyMmQaikgiRCKz-8H6uZi1I8U0ZYZsOWUlBTwLvIN3FemNMUoDgW-pH5V7BgA-uxS7BpU)
- [ ] [A predictive analytics approach for forecasting bike rental demand](https://www.sciencedirect.com/science/article/pii/S2772662224000869)
---
regular news articles

- [ ] [How Bike Share Systems Are Failing Us](https://www.vice.com/en/article/bike-share-systems-fail-underserved-communities/)
- [ ] [The Bike-Share Report: Hard Times and Hope for the Future](https://www.smartcitiesdive.com/ex/sustainablecitiescollective/bike-share-report-hard-times-and-hope-future/208761/)
- [ ] [Study Case — Rental Bike Analysis](https://muhammadfadlisyukur.medium.com/study-case-rental-bike-analysis-0945c342a281)
- [ ] [Why some bike shares work and others don't](https://www.bbc.com/future/article/20210112-the-vast-bicycle-graveyards-of-china)
- [ ] [Bike Sharing Is Doomed to Fail in Most American Cities](https://www.vice.com/en/article/bike-sharing-doomed-to-fail-dallas-limebike-ofo-transportation-cycling/)
- [ ] [Using data mining techniques for bike sharing demand prediction in metropolitan city](https://www.sciencedirect.com/science/article/pii/S0140366419318997?casa_token=tpw9HRau_NcAAAAA:8xYqDPiYi2ycysCSbJAbASdqc4SLq-wnIJ5aFge-Ef5xt86lak_SfQlTYKxF51sCEdC7wcRS)

day of week, weather/forecast, holiday, season
other ppl: events in the city (can they be seen in data?)
semi-parametric paper: visibility, wind speed

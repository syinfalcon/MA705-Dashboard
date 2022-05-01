# MA705 Final Project

This repository contains files used in the MA705 dashboard project.

The final dashboard is deployed on Heroku [here](https://ma705bostonuniversities.herokuapp.com).

## Dashboard Description

The dashboard summarizes the information of the number of deaths caused by different reasons during four years obtained from the Data.CDC.gov website.
There is one bar chart and two tables in this dashboard.

Bar chart:
- x axis shows the time by year
- y axis shows the number of deaths per 1000000 residents
- y label shows the cause of death
- the color in the bar chart means different states

Table1:
- it solves the question that which state has the highest average number of deaths per 1000000 residents caused by the reason selected?
- Table1 is only affected by the cause of death

Table2:
- it shows the average number of deaths per 1000000 residents with different causation in each state you select
- Table2 is only affected by states

### Data Sources

- Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2014-2019.csv
- nst-est2019-01.csv (the estimated US population of each state)


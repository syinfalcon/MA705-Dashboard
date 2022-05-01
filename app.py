# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:16:58 2022

@author: Yinsh
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
#from pandas import Series
import numpy as np

'''DATA FRAME'''

#import cuase of death data
file = pd.read_csv('Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2014-2019.csv')
df = file.iloc[:, 0:17]
df1 = df.dropna()

state_in_df1 = set(df1["Jurisdiction of Occurrence"])


#import population data
population = pd.read_csv("nst-est2019-01.csv")
df2 = population.iloc[:51, :]
for state in df2["states"].index:
    df2.states[state] = df2.states[state].replace(".","")
for state in df2["states"].index:
    df2["2014"][state] = int(df2["2014"][state].replace(",",""))
    df2["2015"][state] = int(df2["2015"][state].replace(",",""))
    df2["2016"][state] = int(df2["2016"][state].replace(",",""))
    df2["2017"][state] = int(df2["2017"][state].replace(",",""))
    df2["2018"][state] = int(df2["2018"][state].replace(",",""))
    df2["2019"][state] = int(df2["2019"][state].replace(",",""))
   

##add new column in df1 using the data from df2
#shorten the df2 based on the state that df1 have (state_in_df1)
df2 = df2[df2["states"].isin(state_in_df1)]
#shorten the df1 based on the state that df3 have
df1 = df1[df1["Jurisdiction of Occurrence"].isin(set(df2["states"]))]
#add new column in df1
df1_2014 = df1[df1["MMWR Year"] == 2014]
df2_2014 = df2[["states","2014"]]
df1_2014 = df1_2014.merge(df2_2014, left_on ='Jurisdiction of Occurrence',
                          right_on = 'states', how='left')
df1_2014 = df1_2014.rename(columns={'2014':'population'})
df1_2015 = df1[df1["MMWR Year"] == 2015]
df2_2015 = df2[["states","2015"]]
df1_2015 = df1_2015.merge(df2_2015, left_on ='Jurisdiction of Occurrence',
                          right_on = 'states', how='left')
df1_2015 = df1_2015.rename(columns={'2015':'population'})
df1_2016 = df1[df1["MMWR Year"] == 2016]
df2_2016 = df2[["states","2016"]]
df1_2016 = df1_2016.merge(df2_2016, left_on ='Jurisdiction of Occurrence',
                          right_on = 'states', how='left')
df1_2016 = df1_2016.rename(columns={'2016':'population'})
df1_2017 = df1[df1["MMWR Year"] == 2017]
df2_2017 = df2[["states","2017"]]
df1_2017 = df1_2017.merge(df2_2017, left_on ='Jurisdiction of Occurrence',
                          right_on = 'states', how='left')
df1_2017 = df1_2017.rename(columns={'2017':'population'})
df1_2018 = df1[df1["MMWR Year"] == 2018]
df2_2018 = df2[["states","2018"]]
df1_2018 = df1_2018.merge(df2_2018, left_on ='Jurisdiction of Occurrence',
                          right_on = 'states', how='left')
df1_2018 = df1_2018.rename(columns={'2018':'population'})
df1_2019 = df1[df1["MMWR Year"] == 2019]
df2_2019 = df2[["states","2019"]]
df1_2019 = df1_2019.merge(df2_2019, left_on ='Jurisdiction of Occurrence',
                          right_on = 'states', how='left')
df1_2019 = df1_2019.rename(columns={'2019':'population'})
df1 = pd.concat([df1_2014, df1_2015, df1_2016, df1_2017, df1_2018, df1_2019])
df1.index = pd.Series(list(range(0,5251)))

##change variables for number of deaths per 1000000 residents

# df1['All  Cause'] =( df1['All  Cause'] / df1['population'] )* 100000
# df1['Natural Cause'] =( df1['Natural Cause'] / df1['population'] )* 100000
# df1['Septicemia (A40-A41)'] =( df1['Septicemia (A40-A41)'] / df1['population'] )* 100000
# df1['Malignant neoplasms (C00-C97)'] =( df1['Malignant neoplasms (C00-C97)'] / df1['population'] )* 100000
# df1['Diabetes mellitus (E10-E14)'] =( df1['Diabetes mellitus (E10-E14)'] / df1['population'] )* 100000
# df1['Alzheimer disease (G30)'] =( df1['Alzheimer disease (G30)'] / df1['population'] )* 100000
# df1['Influenza and pneumonia (J10-J18)'] =( df1['Influenza and pneumonia (J10-J18)'] / df1['population'] )* 100000
# df1['Chronic lower respiratory diseases (J40-J47)'] =( df1['Chronic lower respiratory diseases (J40-J47)'] / df1['population'] )* 100000
# df1['Other diseases of respiratory system (J00-J06,J30-J39,J67,J70-J98)'] =( df1['Other diseases of respiratory system (J00-J06,J30-J39,J67,J70-J98)'] / df1['population'] )* 100000
# df1['Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)'] =( df1['Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)'] / df1['population'] )* 100000
# df1['Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)'] =( df1['Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)'] / df1['population'] )* 100000
# df1['Diseases of heart (I00-I09,I11,I13,I20-I51)'] =( df1['Diseases of heart (I00-I09,I11,I13,I20-I51)'] / df1['population'] )* 100000
# df1['Cerebrovascular diseases (I60-I69)'] =( df1['Cerebrovascular diseases (I60-I69)'] / df1['population'] )* 100000

#round the number of deaths per 1000000 residents
causes = ['All  Cause', 'Natural Cause',
'Septicemia (A40-A41)', 'Malignant neoplasms (C00-C97)',
'Diabetes mellitus (E10-E14)', 'Alzheimer disease (G30)',
'Influenza and pneumonia (J10-J18)',
'Chronic lower respiratory diseases (J40-J47)',
'Other diseases of respiratory system (J00-J06,J30-J39,J67,J70-J98)',
'Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)',
'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)',
'Diseases of heart (I00-I09,I11,I13,I20-I51)',
'Cerebrovascular diseases (I60-I69)']
for cause in causes:
    df1[cause] =( df1[cause] / df1['population'] )* 1000000
    df1[cause] = np.array(df1[cause], dtype=int)
    
'''DASHBOARD TABLE'''
#in which states is the, say, cancer death rate highest
df_table1_columns = ['states', 'All  Cause', 'Natural Cause',
       'Septicemia (A40-A41)', 'Malignant neoplasms (C00-C97)',
       'Diabetes mellitus (E10-E14)', 'Alzheimer disease (G30)',
       'Influenza and pneumonia (J10-J18)',
       'Chronic lower respiratory diseases (J40-J47)',
       'Other diseases of respiratory system (J00-J06,J30-J39,J67,J70-J98)',
       'Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)',
       'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)',
       'Diseases of heart (I00-I09,I11,I13,I20-I51)',
       'Cerebrovascular diseases (I60-I69)']
df_table1 = df1.groupby('states', as_index = False).mean()
df_table1 = round(df_table1)
df_table1 = df_table1[df_table1_columns]

df_table2 = df_table1

'''DASHBOARD'''

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


### pandas dataframe to html table
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=stylesheet)
server = app.server

fig = px.bar(df1, x = "MMWR Year", y = "All  Cause")
# fig = fig.update_xaxes(showgrid=False)
# fig = fig.update_yaxes(showgrid=False)
# fig = fig.update_layout(xaxis=dict(showgrid=False),
#               yaxis=dict(showgrid=False))

checklist_options = [{'label': state, 'value': state} for state in set(df1.states)]
dropdown_options = [{'label': cause, 'value': cause} for cause in causes]

app.layout = html.Div([html.H1("Cause of Death Dashboard",
                              style = {'textAlign': 'center', 'family':'Actor'}),
                       html.H1("What is this dashboard about?",
                               style = {'fontSize': 25, 'family':'Actor'}),
                       html.H3("The dashboard summarizes the information of"+
                               " the number of deaths caused by different "+
                               "reasons during four years obtained from"+
                               " the Data.CDC.gov website. "+
                               "It includes one bar chart and two tables.",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.A("Click here to go to Data.CDC.gov",
                              href = "https://data.cdc.gov/NCHS/Weekly-Counts-of-Deaths-by-State-and-Select-Causes/3yf8-kanr",
                              target = "_blank"),
                       # html.H3("The dashboard summarizes the information of"+
                       #         " the number of deaths caused by different "+
                       #         "reasons during four years obtained from"+
                       #         " the Data.CDC.gov website."+
                       #         "There is one bar chart and two tables in this dashboard."+
                       #         " In the bar chart,  x axis shows the time by year, y axis shows the number of deaths per 1000000 residents, y label shows the cause of death."+
                       #         " The color in the bar chart means different states."+
                       #         " This bar chart is affected by states and the cause of death."+
                       #         " For the table1, it solves the question that which state has the highest average number of deaths per 1000000 residents caused by the reason selected?"+
                       #         " Table1 is only affected by the cause of death."+
                       #         " For the table2, it shows the average number of deaths per 1000000 residents with different causation in each state you select."+
                       #         " Table2 is only affected by states.",
                       #         style = {'fontSize': 18}),
                       html.H2("Bar chart:",
                               style = {'fontSize': 20, 'family':'Actor'}),
                       html.H3("- x axis shows the time by year",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H3("- y axis shows the number of deaths per 1,000,000 residents",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H3("- y label shows the causes of death",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H3("- the color of the bar chart shows different states",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H3("- this bar chart is affected by states and the cause of death",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H2("Table 1:",
                               style = {'fontSize': 20, 'family':'Actor'}),
                       html.H3("- it solves the question that which state has the highest average number of deaths per 1,000,000 residents caused by the reason selected",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H3("- Table 1 is only affected by the cause of death",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H2("Table 2:",
                               style = {'fontSize': 20, 'family':'Actor'}),
                       html.H3("- it shows the average number of deaths per 1,000,000 residents with different causation in each state you selected",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H3("- Table 2 is only affected by states",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       
                       html.H1("How to use this dashboard?",
                               style = {'fontSize': 25, 'family':'Actor'}),
                       html.H3("- Use checklist to select states",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H3("- Use dropdown to select the cause of death",
                               style = {'fontSize': 18, 'family':'Actor'}),
                       html.H1("Bar chart: the number of deaths caused per 1,000,000 residents by different "+
                       "reasons",
                               style = {'fontSize': 25, 'family':'Actor'}),
                       html.Div([html.H6("Select cause of death:",
                                                  style = {'fontSize': 18, "marginTop": 10,'family':'Actor'}),
                                          dcc.Dropdown(options = dropdown_options, 
                                             value = "Septicemia (A40-A41)",
                                             id = "dropdown")]),
                       dcc.Graph(figure = fig, id = "plot",
                                  style = {'width':'85%', 'float':'right', 'height': 900}),
                       html.Div([html.H2('Select States:',
                                         style = {'fontSize': 18, 'family':'Actor'}),
                                 dcc.Checklist(options = checklist_options, 
                                     value = ["Alabama"],
                                     id = "checklist")],
                                style = {'width':'15%', 'float':'left', 'height': 890}),
                       # html.Div([html.H6("Select cause of death:",
                       #                             style = {'fontSize': 18, "marginTop": 30}),
                       #                     dcc.Dropdown(options = dropdown_options, 
                       #                        value = "Septicemia (A40-A41)",
                       #                        id = "dropdown")]),
                       html.H1("Table 1: which state has the highest average number of deaths per 1,000,000 residents caused by the reason selected?",
                               style = {'fontSize': 25, "marginTop": 30}),
                       html.Div(generate_table(df_table2), id = "table"),
                       html.H1("Table 2: the average number of deaths per 1,000,000 residents",
                               style = {'fontSize': 25, "marginTop": 30}),
                       html.Div(generate_table(df_table1), id = "table2")
                     ])

@app.callback(
    Output("plot", "figure"),
    Input("checklist", "value"),
    Input("dropdown","value")
)
def update_plot(state, cause):
    df_plot = df1[df1.states.isin(state)]
    y = df_plot[cause]
    fig = px.bar(df_plot, x = "MMWR Year", y = y, color="states")
    fig = fig.update_layout(xaxis=dict(showgrid=False),
                   yaxis=dict(showgrid=False))
    return fig

@app.callback(
    Output("table", "children"),
    Input("dropdown","value")
)
def update_table(cause):
    x = df_table2[["states", cause]]
    x = x[x[cause] == x[cause].max()]
    return generate_table(x)


@app.callback(
    Output("table2", "children"),
    Input("checklist", "value")
)
def update_table(state):
    x = df_table1[df_table1.states.isin(state)]
    #x = df_table.loc["Wisconsin"].sort_values(ascending=False)
    return generate_table(x)


if __name__ == '__main__':
    app.run_server(debug=True)
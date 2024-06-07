import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as g
from babel.numbers import format_currency

# Load Data
day_df = pd.read_csv("Bike-sharing-dataset/day.csv")
hour_df = pd.read_csv("Bike-sharing-dataset/hour.csv")

# Sidebar
st.sidebar.header('Bike Sharing Analysis')
st.sidebar.markdown('By T. Zalfa Ramadhani')
st.sidebar.markdown('---')

# Main
st.header(':sparkles: Bike Sharing Analysis :sparkles:')

# Hourly Rentals
st.subheader('Hourly Rentals')
hourly_cnt = hour_df.groupby('hr')['cnt'].sum().reset_index()

fig_hourly = px.line(hourly_cnt, x='hr', y='cnt', title='Distribution of Bike Rentals by Hour', labels={'cnt': 'Count', 'hr': 'Hour'})
st.plotly_chart(fig_hourly)

# Monthly Rentals
st.subheader('Monthly Rentals')
month_cnt = day_df.groupby('mnth')['cnt'].sum().reset_index()

fig_monthly = px.line(month_cnt, x='mnth', y='cnt', title='Distribution of Bike Rentals by Month', labels={'cnt': 'Count', 'mnth': 'Month'})
fig_monthly.update_xaxes(tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
st.plotly_chart(fig_monthly)

# Yearly Rentals
st.subheader('Yearly Rentals')
yearly_cnt = hour_df.groupby('yr')['cnt'].sum().reset_index()

fig_yearly = px.bar(yearly_cnt, x='yr', y='cnt', title='Distribution of Bike Rentals by Year', labels={'cnt': 'Count', 'yr': 'Year'})
fig_yearly.update_xaxes(tickvals=[0, 1], ticktext=['2011', '2012'])

max_value_index = yearly_cnt['cnt'].idxmax()
fig_yearly.data[0].marker.color = ['rgba(0, 0, 255, 1)' if i == max_value_index else 'rgba(0, 0, 255, 0.5)' for i in range(len(yearly_cnt))]

st.plotly_chart(fig_yearly)

# Seasonal Rentals
st.subheader('Seasonal Rentals')
season_cnt = hour_df.groupby('season')['cnt'].sum().reset_index()

fig_seasonal = px.bar(season_cnt, x='season', y='cnt', title='Distribution of Bike Rentals by Season', labels={'cnt': 'Total Rentals', 'season': 'Season'})
fig_seasonal.update_xaxes(tickvals=[1, 2, 3, 4], ticktext=['Spring', 'Summer', 'Fall', 'Winter'])

max_value_index_season = season_cnt['cnt'].idxmax()
fig_seasonal.data[0].marker.color = ['rgba(0, 0, 255, 1)' if i == max_value_index_season else 'rgba(0, 0, 255, 0.5)' for i in range(len(season_cnt))]
st.plotly_chart(fig_seasonal)

st.plotly_chart(fig_seasonal)

# Total Rentals vs Temperature
st.subheader('Total Rentals vs Temperature')

fig_temp = px.scatter(hour_df, x='temp', y='cnt', title='Relationship between Total Rentals and Temperature', labels={'temp': 'Temperature (Celsius)', 'cnt': 'Counts'})
st.plotly_chart(fig_temp)

# Bike Rental Patterns on Working Days and Non-working Days (Year 2011)
st.subheader('Bike Rental Patterns on Working Days and Non-working Days (Year 2011)')
day_df_2011 = day_df[day_df['yr'] == 0]

working_days_2011 = day_df_2011[day_df_2011['workingday'] == 1]
non_working_days_2011 = day_df_2011[day_df_2011['workingday'] == 0]

rentals_working_days_2011 = working_days_2011.groupby('mnth')['cnt'].mean().reset_index()
rentals_non_working_days_2011 = non_working_days_2011.groupby('mnth')['cnt'].mean().reset_index()

fig = px.line(rentals_working_days_2011, x='mnth', y='cnt', title='Bike Rental Patterns on Working Days and Non-working Days (Year 2011)', labels={'cnt': 'Average Rental Counts'}, line_shape='linear')
fig.add_scatter(x=rentals_non_working_days_2011['mnth'], y=rentals_non_working_days_2011['cnt'], mode='lines', name='Non-working Days', line=dict(color='red'))
fig.update_traces(mode='lines')  # Ensure no markers
fig.update_layout(xaxis_title='Month', yaxis_title='Average Rental Counts', xaxis=dict(tickmode='linear', tick0=1, dtick=1))
fig.add_scatter(x=rentals_working_days_2011['mnth'], y=rentals_working_days_2011['cnt'], mode='lines', name='Working Days', line=dict(color='blue'))
st.plotly_chart(fig)

# Relationship between Rental Counts and Weather Condition
st.subheader('Relationship between Rental Counts and Weather Condition')
weather_counts = hour_df.groupby('weathersit')['cnt'].sum().reset_index()

fig_weather = px.bar(weather_counts, x='weathersit', y='cnt', title='Relationship between Rental Counts and Weather Condition', labels={'cnt': 'Total Rentals', 'weathersit': 'Weather Condition'})
fig_weather.update_xaxes(tickvals=[1, 2, 3, 4], ticktext=['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow'])

max_value_index_season = weather_counts['cnt'].idxmax()
fig_weather.data[0].marker.color = ['rgba(255, 0, 0, 1)' if i == max_value_index_season else 'rgba(0, 0, 255, 0.5)' for i in range(len(weather_counts))]

st.plotly_chart(fig_weather)

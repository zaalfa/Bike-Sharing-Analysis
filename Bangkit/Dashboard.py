import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from babel.numbers import format_currency

sns.set(style='dark')

# Load Data
day_df = pd.read_csv("Bike-sharing-dataset/day.csv")
hour_df = pd.read_csv("Bike-sharing-dataset/hour.csv")

# Side Bar
st.sidebar.header('Bike Sharing Analysis')
st.sidebar.markdown('By T. Zalfa Ramadhani')
st.sidebar.markdown('---')

# Main
st.header(':sparkles: Bike Sharing Analysis :sparkles:')


# Hourly Rentals
st.subheader('Hourly Rentals')
hourly_cnt = hour_df.groupby('hr')['cnt'].sum()

sns.set_palette("pastel")
fig, ax = plt.subplots()
sns.lineplot(x=hourly_cnt.index, y=hourly_cnt.values, marker='o', color='blue', linewidth=1.5, ax=ax)
ax.fill_between(hourly_cnt.index, hourly_cnt.values, alpha=0.5)  

ax.set_xlabel('Hour')
ax.set_ylabel('Count')
ax.set_title('Distribution of Bike Rentals by Hour')
ax.set_xticks(range(24)) 
ax.set_ylim(0, hourly_cnt.max() + 5)
st.pyplot(fig)

# Monthly Rentals
st.subheader('Monthly Rentals')
month_cnt = day_df.groupby('mnth')['cnt'].sum()

sns.set_palette("pastel")
fig, ax = plt.subplots()
sns.lineplot(x=month_cnt.index, y=month_cnt.values, marker='o', color='blue', linewidth=1.5)
ax.fill_between(month_cnt.index, month_cnt.values, alpha=0.5)

ax.set_xlabel('Month')
ax.set_ylabel('Count')
ax.set_title('Distribution of Bike Rentals by Month')
ax.set_xticks(range(1, 13))
ax.set_ylim(400, month_cnt.max() + 5)

st.pyplot(plt)

# Yearly Rentals
st.subheader('Yearly Rentals')
yearly_cnt = hour_df.groupby('yr')['cnt'].sum().reset_index()

sns.set_palette("pastel")
fig, ax = plt.subplots()
sns.barplot(x='yr', y='cnt', data=yearly_cnt, ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Distribution of Bike Rentals by Month')
ax.set_xticklabels(['2011', '2012'])
st.pyplot(fig)

# Seasonal Rentals
st.subheader('Seasonal Rentals')
season_cnt = hour_df.groupby('season')['cnt'].sum().reset_index()

sns.set_palette("pastel")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=season_cnt, ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Total Rentals')
ax.set_title('Distribusi Penyewa Berdasarkan Musim')
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

# Total Rentals vs Temperature
st.subheader('Total Rentals vs Temperature')

fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=hour_df, ax=ax)
ax.set_xlabel('Temperature (Celsius)')
ax.set_ylabel('Counts')
ax.set_title('Hubungan antara Jumlah Penyewa dan Temperatur')
st.pyplot(fig)

#1st Question
st.subheader('Bike Rental Patterns on Working Days and Non-working Days (Year 2011)')
day_df_2011 = day_df[day_df['yr'] == 0]

working_days_2011 = day_df_2011[day_df_2011['workingday'] == 1]
non_working_days_2011 = day_df_2011[day_df_2011['workingday'] == 0]

rentals_working_days_2011 = working_days_2011.groupby('mnth')['cnt'].mean()
rentals_non_working_days_2011 = non_working_days_2011.groupby('mnth')['cnt'].mean()

plt.figure(figsize=(12, 6))
plt.plot(rentals_working_days_2011.index, rentals_working_days_2011.values, label='Working Days', color='blue')
plt.plot(rentals_non_working_days_2011.index, rentals_non_working_days_2011.values, label='Non-working Days', color='red')
plt.xlabel('Month')
plt.ylabel('Average Rental Counts')
plt.title('Bike Rental Patterns on Working Days and Non-working Days (Year 2011)')
plt.legend()
plt.xticks(range(1, 13))
plt.tight_layout()
st.pyplot(plt)

#2st Question
st.subheader('Relationship between Rental Counts and Weather Condition')
weather_counts = hour_df.groupby('weathersit')['cnt'].sum().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_counts, color='blue')
plt.xlabel('Weather Condition')
plt.ylabel('Total Rentals')
plt.title('Relationship between Rental Counts and Weather Condition')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow'])
plt.tight_layout()
st.pyplot(plt)
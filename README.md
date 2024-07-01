## **Lok Sabha Election Analysis**
This repository contains Python scripts for scraping Lok Sabha election data from the Election Commission of India's website and deriving key insights from it.

## **Project Overview**

The scripts included:

**Scraper Script**: election_scraper.py - Scrapes data from ECI Results Portal.

**Analysis Script**: task.py - Analyzes the scraped data to derive insights.

**README**: This file provides an overview of the project and insights derived.

## **Insights Derived**

**Total Number of Parliament Constituencies**: Displaying the total number of constituencies contested in the elections.

**Winning Party**: Identifying the party with the highest number of seats won in the elections.

**Seats Won by Winning Party**: Showing the exact number of seats won by the winning party.

**Number of Parties**: Counting the total number of political parties participating in the elections.

**Second Highest Votes Party**: Identifying the party with the second-highest number of votes.

**Seats Won by Telugu Desam**: Total seats won by Telugu Desam Party.

**Difference Between BJP and INC**: Displaying the difference in seats won between Bharatiya Janata Party (BJP) and Indian National Congress (INC).

**Top 5 Parties by Seats**: Listing the top 5 parties based on the number of seats won.

**Parties with At Least 20 Seats**: Counting the number of parties that won at least 20 seats.

**Third Highest Party**: Identifying the party with the third-highest number of seats.

## **Usage**

Clone the repository:

``` bash
git clone https://github.com/YandapalliChinni/Election_analysis.git
```
Install dependencies:

``` bash
pip install requests beautifulsoup4 pandas
```

Run the scraper script to fetch latest election data:

``` bash
python election_scraper.py
```

Run the analysis script to derive insights:

``` bash
python task.py
```

## **Data Source**

Election results data sourced from Election Commission of India Results Portal.

## **Author**

Chinni Yandapalli

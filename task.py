import pandas as pd

# Load the CSV file with the correct encoding
x= "C:\\Users\\91824\\Downloads\\election_results.csv"
df = pd.read_csv(x, encoding='ISO-8859-1')

# Defining functions for each and every case that we need
def total_constituencies_count(df):
    return f"Total number of parliament constituencies: {df['Won'].sum()}"

def winning_party(df):
    return f"Winning party name: {df.loc[df['Won'].idxmax(), 'Party']}"

def winning_party_seats(df):
    return f"Winning party number of seats: {df['Won'].max()}"

def number_of_parties(df):
    return f"Number of parties: {df.shape[0]}"

def second_highest_party(df):
    return f"2nd highest votes having party: {df.nlargest(2, 'Won').iloc[1]['Party']}"

def telugu_desam_seats(df):
    return f"Number of seats won by Telugu Desam: {df.loc[df['Party'].str.contains('Telugu Desam'), 'Won'].sum()}"

def difference_bjp_inc(df):
    bjp_seats = df.loc[df['Party'].str.contains('Bharatiya Janata Party'), 'Won'].sum()
    inc_seats = df.loc[df['Party'].str.contains('Indian National Congress'), 'Won'].sum()
    return f"Difference between BJP and INC: {bjp_seats - inc_seats}"

def top_5_parties(df):
    top_5 = df.nlargest(5, 'Won')[['Party', 'Won']]
    return f"Top 5 parties:\n{top_5.to_string(index=False)}"

def parties_at_least_20_seats(df):
    return f"Number of parties with at least 20 seats: {df[df['Won'] >= 20].shape[0]}"

def third_highest_party(df):
    return f"3rd highest party: {df.nlargest(3, 'Won').iloc[2]['Party']}"

# Create a dictionary to map case numbers to functions
cases = {
    1: total_constituencies_count,
    2: winning_party,
    3: winning_party_seats,
    4: number_of_parties,
    5: second_highest_party,
    6: telugu_desam_seats,
    7: difference_bjp_inc,
    8: top_5_parties,
    9: parties_at_least_20_seats,
    10: third_highest_party
}

# Descriptions for the cases
res = {
    1: "Total number of parliament constituencies",
    2: "Winning party name",
    3: "Winning party number of seats",
    4: "Number of parties",
    5: "2nd highest votes having party",
    6: "Number of seats won by Telugu Desam",
    7: "Difference between BJP and INC",
    8: "Top 5 parties",
    9: "Number of parties with at least 20 seats",
    10: "3rd highest party"
}

# Function to execute the selected case
def execute_case(count, df):
    if count in cases:
        result = cases[count](df)
        print(result)
    else:
        print("Invalid case number")

# Interactive loop to execute cases based on user input
while True:
    print("Select a case number to execute (1-10) or type 'exit' to quit:")
    
    data= input()
    
    if data.lower() == 'exit':
        break

    try:
        count = int(data)
        execute_case(count, df)
    except ValueError:
        print("Please enter a valid number or 'exit' to quit.")

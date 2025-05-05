# batting_average.py
# This program calculates Geoffrey Boycott's batting average

# Career statistics
matches = 609
innings_batted = 1014
not_outs = 162
total_runs = 48426

# Calculate completed innings
completed_innings = innings_batted - not_outs

# Calculate batting average
batting_average = total_runs / completed_innings

# Display the result
print(f"Geoffrey Boycott's batting average: {batting_average:.2f}")

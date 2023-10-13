# Read a date from the input given in one of the following formats: YYYY-MM-DD or YYY-MM-DD. 
# Print the year, month and day on separate lines.

date_input = input()
date_split = date_input.split("-")
print("\n".join(date_split))

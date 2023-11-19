import csv
import pickle

views_raw = []

# Open the CSV file
with open('modules\\View_Data_createView.csv', newline='') as csvfile:
    # Create a CSV reader
    csvreader = csv.reader(csvfile, delimiter=';')
    
    # Skip the header row if there is one
    # next(csvreader, None)
    
    # Iterate over each row in the CSV
    for i, row in enumerate(csvreader):
        # Stop after the first 20 entries
        if i == 20:
            break
        # Check if the row has at least nine values
        if len(row) >= 9:
            # Remove spaces, tabs, and newlines, then append the ninth value to the list
            cleaned_value = row[8].replace('\t', '').replace('\n', '').replace('\r', '').strip()
            views_raw.append(cleaned_value)
        else:
            # Handle rows that do not have at least nine values
            print(f"Row {i} does not contain 9 values.")

# Save the list to a file using pickle
with open('views_raw.pkl', 'wb') as f:
    pickle.dump(views_raw, f)

print("The first 20 ninth values, with all spaces, tabs, and new lines removed, have been saved to views_raw.pkl")


import pickle

# Load the list from the file
with open('views_raw.pkl', 'rb') as f:
    views_raw = pickle.load(f)

# Now you can use the list `views_raw` as needed
#print(views_raw[3])
print(f"View (type: {type(views_raw)}): {views_raw[3]}")
import json

# Read the JSON data from ex5.json
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Add a new batter for "Old Fashioned" donut
new_batter = {
    "id": "coffee",
    "type": "Coffee"
}

# Find the "Old Fashioned" donut and add the new batter
for donut in ex5:
    if donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append(new_batter)
        break

# Write the updated data back to ex5.json
with open('ex5.json', 'w') as file:
    json.dump(ex5, file)

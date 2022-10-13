"""Demonstrates the capabilities of dictionaries."""

# Declaring the type of a dictionary.
schools: dict[str, int]

# Initialize to an empty dictionary.
schools = dict()

# Set a key-value pairing in the dictionary.
schools["UNC"] = 19_400
schools["Duke"] = 7_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation.
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary by its key. 
schools.pop("Duke")

# Test for existence of a key. 
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update or reassign a key-value pair. 
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Empty dictionary literal.
schools = {}  # Same as dict()

# Alternatively, initialize key-value pairs. 
schools = {
    "UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 26150
}

print(schools)

# Examples of looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")


# Compound data types with dictionaries and lists.
rows: list[dict[str, int]] = [
    {"hi": 76, "lo": 51},
    {"hi": 77, "lo": 53}
]

low: dict[str, int] = rows[1]

print(rows)
print(low)

print("Now modifying low...")
low["hi"] = 50
print("Here is the new low...")
print(low)
print("Has it affected rows?")
print(rows)
# We can get a variable assigned to a list within a dictionary or a dictionary within a list directly. 
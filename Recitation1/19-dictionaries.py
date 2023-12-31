
# Create an empty dictionary
captains = {}


# Add some key-value pairs to the dictionary
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

print(captains)
# Check if "Enterprise" and "Discovery" exist; if not, add them
if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

print(captains)
# loop over a list of names to check
for ship in ["Enterprise", "Discovery", "Titanic"]:
   if not ship in captains:
       captains[ship] = "unknown"
print(captains)

# Display the contents of the dictionary, one pair at a time
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")


# Remove "Discovery"
del captains["Discovery"]


# Create dictionary by passing a list to dict()
captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyager", "Janeway"),
        ("Defiant", "Sisko"),
    ])
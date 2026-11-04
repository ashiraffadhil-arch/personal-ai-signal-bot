def calculate_probability(mines, picks): total_boxes = 25

if not isinstance(mines, int) or not isinstance(picks, int):
    raise ValueError("Values must be integers")

if not 1 <= mines <= 24:
    raise ValueError("Mines must be between 1 and 24")

if not 1 <= picks <= total_boxes - mines:
    raise ValueError("Invalid number of picks")

probability = 1.0

for i in range(picks):
    probability *= (
        (total_boxes - mines - i) /
        (total_boxes - i)
    )

return round(probability * 100, 2)


if name == "main": result = calculate_probability(3, 5)

print("MINES PROBABILITY ENGINE")
print("-----------------------")
print(f"Probability of safe picks: {result}%")
print("Note: This is mathematical probability, not a winning prediction.")

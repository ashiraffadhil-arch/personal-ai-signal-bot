import statistics

def analyze_multipliers(values):

if not values:
    raise ValueError("Multiplier data cannot be empty")

data = [float(value) for value in values]

if any(value <= 0 for value in data):
    raise ValueError("Multipliers must be positive")

if len(data) < 5:
    raise ValueError("At least 5 rounds are required")

return {
    "rounds": len(data),
    "average": round(statistics.mean(data), 2),
    "median": round(statistics.median(data), 2),
    "highest": round(max(data), 2),
    "lowest": round(min(data), 2),
    "standard_deviation": round(
        statistics.pstdev(data), 2
    )
}


if name == "main":

sample = [1.2, 2.5, 1.8, 3.0, 1.1, 4.2]

result = analyze_multipliers(sample)

print("AVIATOR STATISTICS ENGINE")
print("------------------------")

for key, value in result.items():
    print(f"{key}: {value}")

print("\nHistorical statistics do not predict future rounds.")

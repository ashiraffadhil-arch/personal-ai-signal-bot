import math
import statistics

print("================================")
print("   PERSONAL AI SIGNAL ASSISTANT")
print("================================")

def mines_probability():
    print("\n--- MINES PROBABILITY ---")

    total = 25
    mines = int(input("Idadi ya mines (1-24): "))
    picks = int(input("Idadi ya boxes unazotaka kuchagua: "))

    if not 1 <= mines <= 24 or not 1 <= picks <= 25 - mines:
        print("Taarifa ulizoingiza si sahihi.")
        return

    probability = 1

    for i in range(picks):
        probability *= (total - mines - i) / (total - i)

    print(f"Probability ya kupata boxes salama: {probability * 100:.2f}%")
    print("Hii ni hesabu ya uwezekano, si signal ya ushindi.")

def aviator_statistics():
    print("\n--- AVIATOR STATISTICS ---")

    values = input("Ingiza multipliers zilizopita (mfano 1.2,2.5,3.0): ")

    try:
        data = [float(x) for x in values.split(",")]

        if not data or any(x <= 0 for x in data):
            print("Ingiza multipliers sahihi.")
            return

        print("Idadi ya rounds:", len(data))
        print("Average:", round(statistics.mean(data), 2))
        print("Highest:", max(data))
        print("Lowest:", min(data))

        print("Kumbuka: Historia haitabiri round inayofuata.")

    except ValueError:
        print("Taarifa si sahihi.")

def main():
    while True:
        print("\n1. Mines Probability")
        print("2. Aviator Statistics")
        print("3. Exit")

        choice = input("Chagua huduma: ")

        if choice == "1":
            mines_probability()
        elif choice == "2":
            aviator_statistics()
        elif choice == "3":
            break
        else:
            print("Chaguo si sahihi.")

if __name__ == "__main__":
    main()

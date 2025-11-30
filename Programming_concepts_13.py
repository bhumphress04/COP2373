import sqlite3
import random
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# FUNCTION 1: Create database and insert 2023 population data
# ---------------------------------------------------------
def create_database():
    conn = sqlite3.connect("population_BH.db")   # initials
    cur = conn.cursor()

    # Create the table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # 10 Florida cities with sample 2023 populations
    florida_cities = {
        "Miami": 449514,
        "Orlando": 316081,
        "Tampa": 403364,
        "Jacksonville": 971319,
        "Tallahassee": 204523,
        "St. Petersburg": 261338,
        "Fort Lauderdale": 183445,
        "Gainesville": 145214,
        "Sarasota": 57730,
        "Cape Coral": 216992
    }

    # Insert 2023 data
    for city, pop in florida_cities.items():
        cur.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                    (city, 2023, pop))

    conn.commit()
    conn.close()
    print("Database created and 2023 population data inserted.\n")


# ---------------------------------------------------------
# FUNCTION 2: Simulate population for next 20 years
# ---------------------------------------------------------
def simulate_population():
    conn = sqlite3.connect("population_BH.db")
    cur = conn.cursor()

    # Retrieve 2023 values
    cur.execute("SELECT city, population FROM population WHERE year = 2023")
    rows = cur.fetchall()

    for city, pop in rows:
        current_population = pop

        # Simulate 2024–2043 (20 years)
        for year in range(2024, 2044):
            growth_rate = random.uniform(-0.02, 0.04)  # –2% decline to +4% growth
            current_population = int(current_population * (1 + growth_rate))

            cur.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                        (city, year, current_population))

    conn.commit()
    conn.close()
    print("Population simulation for 20 years completed.\n")


# ---------------------------------------------------------
# FUNCTION 3: Ask user for a city and plot population growth
# ---------------------------------------------------------
def plot_population():
    conn = sqlite3.connect("population_BH.db")
    cur = conn.cursor()

    # List available cities
    cur.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cur.fetchall()]

    print("Choose a city to view its population growth:\n")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    # User choice
    choice = int(input("\nEnter the number of the city: "))
    selected_city = cities[choice - 1]

    # Retrieve data
    cur.execute("""
        SELECT year, population 
        FROM population 
        WHERE city = ? 
        ORDER BY year
    """, (selected_city,))

    rows = cur.fetchall()
    conn.close()

    years = [row[0] for row in rows]
    populations = [row[1] for row in rows]

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker="o")
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()


# ---------------------------------------------------------
# MAIN FUNCTION TO RUN EVERYTHING
# ---------------------------------------------------------
def main():
    create_database()
    simulate_population()
    plot_population()


# Run program
if __name__ == "__main__":
    main()

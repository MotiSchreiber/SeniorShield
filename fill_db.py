import random
import datetime
import pymysql

# Function to generate random phone number
def generate_numbers(random_length, prefix=""):
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(random_length)])
    return prefix + random_numbers

# Function to generate random date
def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

def main():
    # Connect to MySQL database
    connection = pymysql.connect(host='localhost',
                                user='your_username',
                                password='your_password',
                                database='your_database')

    # Create a cursor object
    cursor = connection.cursor()

    # Define list of first names, last names, and cities in Israel
    first_names = ['David', 'Sarah', 'Daniel', 'Leah', 'Michael', 'Rachel', 'Yosef', 'Esther', 'Moshe', 'Ruth',
                'Avraham', 'Rebecca', 'Yitzhak', 'Miriam', 'Benjamin', 'Hannah', 'Shlomo', 'Chaya', 'Eliyahu', 'Tamar',
                'Yehuda', 'Deborah', 'Aharon', 'Devorah', 'Yaakov', 'Naomi', 'Shimon', 'Rivka', 'Yosefa', 'Batya']
    last_names = ['Cohen', 'Levi', 'Mizrachi', 'Peretz', 'Weiss', 'Goldberg', 'Friedman', 'Schwartz', 'Katz', 'Rosenberg',
                'Stein', 'Gutierrez', 'Azoulay', 'Green', 'Hirsch', 'Shapiro', 'Adler', 'Eisenberg', 'Weinstein', 'Klein']
    cities = ['Tel Aviv', 'Jerusalem', 'Haifa', 'Rishon LeZion', 'Petah Tikva', 'Ashdod', 'Netanya', 'Beer Sheva',
            'Holon', 'Bnei Brak', 'Ramat Gan', 'Ashkelon', 'Bat Yam', 'Herzliya', 'Kfar Saba', 'Beit Shemesh',
            'Lod', 'Ramat HaSharon', 'Nahariya', 'Modiin']

    # Insert 1000 people into the database
    for i in range(1000):
        id = generate_numbers(9)
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        birth_date = generate_random_date(datetime.date(1915, 1, 1), datetime.date(1960, 12, 31))
        mobile_phone = generate_numbers(8, "05")
        home_phone = generate_numbers(7, "03-")
        address = f"{random.randint(1, 100)} {random.choice(cities)}, Israel"
        disability_percentage = round(random.uniform(0, 100), 2)
        monthly_electricity_payment = round(random.uniform(50, 300), 2)
        monthly_water_payment = round(random.uniform(20, 100), 2)
        monthly_city_hall_taxes = round(random.uniform(100, 500), 2)
        relative_first_name = random.choice(first_names)
        relative_last_name = random.choice(last_names)
        relative_phone = generate_numbers(8, "05")
        relative_address = f"{random.randint(1, 100)} {random.choice(cities)}, Israel"
        relative_birth_date = generate_random_date(datetime.date(1950, 1, 1), datetime.date(2000, 12, 31))

        # Insert data into the database
        sql = """INSERT INTO people 
                (id, first_name, last_name, birth_date, mobile_phone, home_phone, address, 
                disability_percentage, monthly_electricity_payment, monthly_water_payment, monthly_city_hall_taxes, 
                relative_first_name, relative_last_name, relative_phone, relative_address, relative_birth_date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (id, first_name, last_name, birth_date, mobile_phone, home_phone, address, 
                disability_percentage, monthly_electricity_payment, monthly_water_payment, monthly_city_hall_taxes, 
                relative_first_name, relative_last_name, relative_phone, relative_address, relative_birth_date)
        cursor.execute(sql, values)

    # Commit changes to the database
    connection.commit()

    # Close cursor and connection
    cursor.close()
    connection.close()
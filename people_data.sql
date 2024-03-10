CREATE TABLE people (
    id VARCHAR(9) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    mobile_phone VARCHAR(20),
    home_phone VARCHAR(20),
    address VARCHAR(255),
    disability_percentage FLOAT,
    relative_first_name VARCHAR(50),
    relative_last_name VARCHAR(50),
    relative_phone VARCHAR(20),
    relative_address VARCHAR(255),
    relative_birth_date DATE
);

-- Table to store monthly payments
CREATE TABLE monthly_payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    person_id VARCHAR(9),
    payment_date DATE,
    electricity_payment DECIMAL(10, 2),
    water_payment DECIMAL(10, 2),
    city_hall_taxes DECIMAL(10, 2),
    FOREIGN KEY (person_id) REFERENCES people(id)
);

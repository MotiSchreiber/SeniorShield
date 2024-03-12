-- Truncate all tables in the database
SET FOREIGN_KEY_CHECKS = 0; -- Disable foreign key checks to avoid constraint violations

-- Truncate each table individually
TRUNCATE TABLE table1;
TRUNCATE TABLE table2;
-- Repeat this for all tables in your database

SET FOREIGN_KEY_CHECKS = 1; -- Enable foreign key checks

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

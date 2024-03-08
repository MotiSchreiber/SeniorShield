CREATE TABLE people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    mobile_phone VARCHAR(20),
    home_phone VARCHAR(20),
    address VARCHAR(255),
    disability_percentage FLOAT,
    monthly_electricity_payment DECIMAL(10,2),
    monthly_water_payment DECIMAL(10,2),
    monthly_city_hall_taxes DECIMAL(10,2),
    relative_first_name VARCHAR(50),
    relative_last_name VARCHAR(50),
    relative_phone VARCHAR(20),
    relative_address VARCHAR(255),
    relative_birth_date DATE
);

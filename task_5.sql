USE alx_book_store;

-- Reset AUTO_INCREMENT so next customer_id starts at 1
ALTER TABLE Customers AUTO_INCREMENT = 1;

-- Remove any existing row with the same email
DELETE FROM Customers WHERE email = 'cbaidoo@sandtech.com';

INSERT INTO Customers (customer_name, email, address)
VALUES ('Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
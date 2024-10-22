# SQL Query Application

## Description
This application contains SQL queries to manipulate and retrieve data from a database. Specifically, it includes a query to increase the price of all products by 10% and display the new prices along with the product names.

## Prerequisites
- A relational database management system (RDBMS) installed (e.g., MySQL, PostgreSQL, SQLite).
- A SQL client or a tool to execute SQL queries (e.g., Visual Studio Code with SQL extension, MySQL Workbench, pgAdmin).

## Setup Instructions

1. **Set Up the Database**
   - Ensure you have a database created with a table named `products`.
   - The `products` table should have the following columns:
     - `id`: Unique identifier for each product (e.g., INT).
     - `name`: Name of the product (e.g., VARCHAR).
     - `price`: Price of the product (e.g., DECIMAL or FLOAT).

   - You can create the `products` table using the following SQL command:
     ```sql
     CREATE TABLE products (
         id INT PRIMARY KEY,
         name VARCHAR(255),
         price DECIMAL(10, 2)
     );
     ```

2. **Insert Sample Data (Optional)**
   - You may want to populate the `products` table with some sample data to test the query:
     ```sql
     INSERT INTO products (id, name, price) VALUES
     (1, 'Product A', 100.00),
     (2, 'Product B', 150.00),
     (3, 'Product C', 200.00);
     ```

## Running the SQL Query

1. **Open Your SQL Client**
   - Open your SQL client or integrated development environment (IDE) such as Visual Studio Code.

2. **Connect to Your Database**
   - Establish a connection to your database using the appropriate credentials (hostname, username, password).

3. **Execute the Query**
   - Copy and paste the following SQL query into your SQL client:
     ```sql
     SELECT name, price * 1.10 AS new_price
     FROM products;
     ```

4. **View Results**
   - Execute the query. The output will display the product names along with their updated prices after applying a 10% increase.

## Example Output
For the sample data provided, the output of the query would look something like this:
```
+------------+-----------+
| name       | new_price |
+------------+-----------+
| Product A  | 110.00    |
| Product B  | 165.00    |
| Product C  | 220.00    |
+------------+-----------+
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thank you for using this SQL Query Application!

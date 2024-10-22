# Prime Factorization Application

## Description
This application provides a function to calculate the prime factorization of a given integer. The `prime_factorization` function returns a list of tuples, where each tuple contains a prime factor and its corresponding exponent.

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of Python programming.

## Setup Instructions

1. **Clone the Repository (if applicable)**  
   If you have the code in a repository, clone it using:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Python File**  
   Create a new Python file, e.g., `prime_factorization.py`, and copy the following code into it:
   ```python
   def prime_factorization(n):
       if n <= 1:
           return []

       prime_factors = []
       exponent = 0
       while n % 2 == 0:
           n //= 2
           exponent += 1
       if exponent > 0:
           prime_factors.append((2, exponent))

       for i in range(3, int(n**0.5) + 1, 2):
           exponent = 0
           while n % i == 0:
               n //= i
               exponent += 1
           if exponent > 0:
               prime_factors.append((i, exponent))

       if n > 2:
           prime_factors.append((n, 1))

       return prime_factors
   ```

3. **Test the Function**  
   In the same Python file, you can add a test section to call the function and print results. For example:
   ```python
   if __name__ == "__main__":
       number = 56  # Example number to factor
       result = prime_factorization(number)
       print(f"Prime factorization of {number}: {result}")
   ```

## Running the Application
- Run the Python file using the command:
   ```bash
   python prime_factorization.py
   ```
- The output will display the prime factorization of the specified number.

## Example
For the input `56`, the output will be:
```
Prime factorization of 56: [(2, 3), (7, 1)]
```
This indicates that \(56 = 2^3 \times 7^1\).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thank you for using this application!


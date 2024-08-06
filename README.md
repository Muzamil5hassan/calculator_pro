# calculator_pro

## Description

This is a simple console-based calculator project implemented in Python. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. The user can select the desired operation, input the values, and receive the result. The program will continue to prompt the user for operations until the user chooses to exit.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Requirements

- Python 3.x

## Usage

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/Muzamil5hassan/calculator_pro.git
    ```

2. Navigate to the project directory:
    ```sh
    cd calculator-project
    ```

3. Run the Python script:
    ```sh
    python calculate_pro.py
    ```

4. Follow the on-screen instructions to perform calculations:
    - Select the operation by entering the corresponding number.
    - Enter the values when prompted.
    - The result will be displayed on the console.
    - The menu will be displayed again for further operations or to exit.

## Code Explanation

The `cal` class contains methods for each arithmetic operation. Each method prompts the user for two input values, performs the operation, and displays the result.

- **add**: Adds two numbers and prints the result.
- **sub**: Subtracts the second number from the first and prints the result.
- **mul**: Multiplies two numbers and prints the result.
- **div**: Divides the first number by the second and prints the result.

The main loop continuously displays a menu to the user, reads their selection, and calls the appropriate method of the `cal` class instance. The loop breaks when the user selects the exit option.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to the branch.
5. Create a pull request.

By following this README, you should be able to run and use the calculator project effectively. Enjoy your calculations!

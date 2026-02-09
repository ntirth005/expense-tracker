# Expense Tracker: CSV Based Bank Statement Visualisation Using Pandas and PLotlyS
This application provides an intuitive interface for visualizing transaction data from CSV files. Users can easily upload their transaction data to generate various insightful visualizations, including cumulative balances, comparisons of credits and debits, and transaction type distributions.

Note: Run all command in the terminal.
      Extract all files in in same folder.

## Key Features
- Interactive visualizations using Plotly
- User-friendly GUI for selecting CSV files
- Multiple chart types to analyze transaction data

## Prerequisites:

    1. Python 3.x
    Required Python packages:
        1. tkinter (comes pre-installed with Python)
        2. pandas
        3. plotly
        4. pywebview
    2. Navigate to the project directory:
        cd path_to_ExpenseTracjer

## Install Required Libraries:

    You can install the required packages using the following commands:

        Using pip directly:
            pip install pandas==2.2.1 plotly==5.21.0 pywebview==3.0

        Using a requirements.txt file: If you have a requirements.txt file, you can install all the dependencies at once with:
            pip install -r requirements.txt

## Executing the Application:

    Run the Application:
        The main entry point of the application is main.py. Run the following command to start the application:

        python main.py

    Select a CSV File:
        A window will pop up allowing you to browse and select a CSV file with transaction data.
        The file should contain columns for 'Credit' and 'Debit' along with other relevant transaction details.
        
        ""Default file name is 'pass.csv'.(Use this file for testing)""

    Visualizations:
        After selecting the file, various plots will be generated and displayed in a webview window. These include:
            1. Cumulative balance over time
            2. Bar chart comparing credits and debits
            3. Pie chart for transaction type distribution
            4. Cumulative credits and debits chart

## File Descriptions:
    1. main.py:
        The main file that handles the GUI for selecting CSV files and processes the selected file.

    2. webTkinter2.py:
        Contains the plotGraphs function that opens a new webview window to display the generated Plotly figures.

    3. graphs.py:
        Contains functions to generate various Plotly visualizations based on transaction data:
            - create_transaction_balance_plot
            - create_credits_debits_bar_chart
            - create_transaction_types_pie_chart
            - create_cumulative_credits_debits_chart
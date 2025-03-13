## WebScraping
## Web Scraping Product Details with Python
This repository contains a simple web scraping script that extracts product information (Name, Price, and Stock) from a sample website and saves it into a CSV file.

## About
The project demonstrates web scraping using Python's requests and BeautifulSoup libraries to:
Extract product names, prices, and stock information from a webpage.
Clean and structure the extracted data.
Save the structured data into a CSV file for further use.

## Libraries Used
numpy: For data manipulation (optional here, but commonly used).
pandas: To create and handle dataframes, and export to CSV.
requests: To send HTTP requests and load the webpage.
BeautifulSoup (from bs4): To parse and extract content from HTML.
google.colab.files: To download the generated CSV file (specific to Google Colab usage).

## How It Works
1.Load the Webpage:
Using requests, the webpage is loaded and status is checked.
2.Parse HTML:
BeautifulSoup parses the HTML content.
3.Extract Data:
Products' names, prices, and stock information are extracted from specific HTML elements.
4.Clean Data:
Remove unnecessary whitespace and characters.
5.Save to CSV:
Data is structured into a pandas DataFrame and saved as products.csv.

## Setup and Usage
1.Clone this Repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2.Install Required Libraries: Make sure you have Python installed. Install necessary libraries:
pip install pandas requests beautifulsoup4

3.Run the Script:
You can run the script in your preferred Python environment (e.g., Jupyter Notebook, Google Colab, or directly via command line).

4.Download CSV (Optional for Google Colab): If using Google Colab, the CSV file can be downloaded using:
from google.colab import files
files.download('products.csv')

## Output
A CSV file named products.csv containing:
Name	     Price	    Stock
Product 1	  $10	     In Stock
Product 2	  $15	    Out of Stock

## Note
This project uses a static sample webpage hosted at:
https://yasaswithachowdary28.github.io/WebScraping/

The structure of the webpage is known and fixed, which makes it suitable for learning and demonstration purposes.
For dynamic or real-world sites, additional handling like JavaScript rendering may be required.

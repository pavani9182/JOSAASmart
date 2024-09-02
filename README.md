# JosaaSmart

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)

## Project Overview
The JOSAASmart website project aims to provide an interface to scrape, analyze, and visualize data from the JOSAA (Joint Seat Allocation Authority) website. The project incorporates the following key components and technologies:

- **beautifulsoup**: Beautiful Soup is a Python library used for parsing HTML and XML documents to extract and manipulate data.
- **pandas**: A versatile data manipulation library in Python, utilized to convert the scraped data into a structured DataFrame, perform data cleaning operations, and enable exploratory data analysis.
- **MySQL**: A popular open-source relational database management system, employed to store the cleaned data in a database for easy retrieval and querying.
- **Django**: A high-level Python web framework that simplifies the development of web applications, used as the backend framework for handling requests, data processing, and database operations.
- **HTML, CSS, and JavaScript**: Standard web technologies for building the frontend of the website, responsible for user interface design, interactivity, and data visualization.
- **Plotly Express**:It is a high-level Python library for creating quick, interactive, and aesthetically pleasing visualizations with minimal code.

By combining these technologies, the JOSAASmart website project enables users to scrape, clean, analyze, and visualize data from the JOSAA website, facilitating better insights and decision-making.

## Installation
To set up the JOSAASmart website project on your local machine, follow these steps:

1. Clone the project repository from GitHub

2. Navigate to the project directory

3. Create a virtual environment (optional but recommended) and activate it:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required libraries using pip:

   ```
   pip install beautifulsoup4 lxml pandas django mysqlclient plotly.express
   ```

   Ensure that you have Python and pip installed on your system, as well as a compatible web driver for selenium (e.g., ChromeDriver for Google Chrome).

5. Install MySQL and set up a database for the project. Refer to the MySQL documentation for detailed instructions on installation and configuration.

6. Configure the database settings in the Django project's settings file (`settings.py`). Update the database host, port, name, user, and password according to your MySQL setup.

## Usage
After completing the installation steps and configuring the database, you can start using the JOSAASmart website by running the Django server. Here's how:

1. Make sure you are in the project directory.

2. Start the Django development server:

   ```
   python manage.py runserver
   ```

3. Access the website by opening a web browser and navigating to

 `http://127.0.0.1:8000`.

4. Explore various sections in the website to get all-round analysis of various JOSAA rounds over past few years

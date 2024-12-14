#!/usr/bin/env python3

import csv
import os

def process_csv(csv_file):
    """Turn the contents of the CSV file into a list of lists"""
    print("Processing {}".format(csv_file))
    with open(csv_file, "r") as datafile:
        data = list(csv.reader(datafile))
    return data

def data_to_html(title, data):
    """Turns a list of lists into an HTML table"""

    # HTML Headers
    html_content = """
<html>
<head>
<title>{}</title>
<style>
table {{
    width: 50%;
    font-family: arial, sans-serif;
    border-collapse: collapse;
}}

tr:nth-child(odd) {{
    background-color: #f2f2f2;
}}

td, th {{
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}}

th {{
    background-color: #4CAF50;
    color: white;
}}
</style>
</head>
<body>
<h2>{}</h2>
<table>
""".format(title, title)

    # Add table headers
    headers = data[0]
    html_content += "<tr>"
    for header in headers:
        html_content += "<th>{}</th>".format(header)
    html_content += "</tr>"

    # Add table rows
    for row in data[1:]:  # Skip header row
        html_content += "<tr>"
        for cell in row:
            html_content += "<td>{}</td>".format(cell)
        html_content += "</tr>"

    # Closing the HTML tags
    html_content += """
</table>
</body>
</html>
"""

    return html_content

def save_html_to_file(html_content, output_filename):
    """Saves the generated HTML content to a file"""
    with open(output_filename, "w") as output_file:
        output_file.write(html_content)
    print(f"HTML content saved to {output_filename}")

def main():
    # Check if the file exists and is a CSV file
    csv_file = "data.csv"  # Change this to your CSV file path
    if not os.path.exists(csv_file):
        print(f"The file {csv_file} does not exist.")
        return
    
    # Process the CSV file
    data = process_csv(csv_file)

    # Convert CSV data to HTML
    html_content = data_to_html("CSV to HTML Report", data)

    # Save the HTML content to a file
    output_filename = "output.html"
    save_html_to_file(html_content, output_filename)

if __name__ == "__main__":
    main()
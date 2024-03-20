# Base image with Python 3.8
FROM python:3.8

# Install required libraries
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your script and any additional files
COPY . .

# Set the working directory for the script
CMD [ "python", "web_crawler.py", "https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html" ]

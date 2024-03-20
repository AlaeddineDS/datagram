DOCKER INSTRUCTIONS 

Running the Web Scraper with Docker

This document outlines the steps to run the web scraper containerized using Docker.

Prerequisites

Docker installed and running on your system. You can verify the installation by running docker -v in your terminal.

Docker Hub account (optional, but recommended for easy access and sharing).

1. Building the Image
   
If you have the Docker image already available on Docker Hub, you can skip this step and proceed to Pulling the Image.

This project uses a Dockerfile to build a container image containing all the necessary dependencies for running the scraper script.

Open a terminal and navigate to the directory containing the Dockerfile.

Run the following command to build the Docker image:

Bash

docker build -t scraper .

This command builds the image and tags it with the name scraper. You can replace scraper with a different name if desired.

2. Pulling the Image (Alternative)

If you don't want to build the image locally or have already pushed it to Docker Hub, you can pull it directly.


You'll need the full image name on Docker Hub. This typically follows the format:

<alaeddine97>/scraper:latest

Use the following command to pull the image from Docker Hub:

Bash

docker pull alaeddine97/scraper:latest

Replace the placeholders with your actual values.

3. Running the Container

Once you have the image (built locally or pulled from Docker Hub), use the following command to run a container from the image:

Bash

docker run scraper <https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html>


Explanation:

docker run: This command tells Docker to run a container from an image.


scraper: This is the name of the image you built or pulled (replace with your actual name if different).

<URL_TO_CRAWL>: This is the argument passed to the container's entrypoint script (your scraper script). It specifies the target URL for scraping.

The scraped product information will be printed to the console.

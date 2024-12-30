# Case Studies Scraper

This repository contains Python scripts designed to automate the collection and processing of case studies from AWS and Google Cloud platforms. The scripts utilize the Playwright library to interact with web pages, scrape data, and save the results for analysis.

## Repository Overview

### 1. **AWS Case Studies**
- **`AWS_links.py`**: 
  - Scrapes links to case studies from the AWS Solutions Case Studies page.
  - Navigates through multiple pages and collects URLs.
  - Saves the collected links into a CSV file for further processing.

- **`AWS_casestudies.py`**: 
  - Reads the links collected by `AWS_links.py` from a CSV file.
  - Downloads the content of each link as a PDF file.
  - Saves the corresponding URLs in text files for reference.

### 2. **Google Cloud Case Studies**
- **`gcloud_links.py`**: 
  - Scrapes links to case studies from the Google Cloud Customer Stories page.
  - Automatically clicks "More" to load additional content until the specified maximum is reached.
  - Saves the collected links into a CSV file.

- **`gcloud_casestudies.py`**: 
  - Reads the links collected by `gcloud_links.py` from a CSV file.
  - Downloads the content of each link as a PDF file.
  - Saves the corresponding URLs in text files for reference.

## Highlights

- **Automation**: Fully automated scraping and processing of data from AWS and Google Cloud.
- **Data Management**: Organizes data into directories for easy access and reference.
- **Flexibility**: Configurable parameters like the number of pages or links to process.

## Directory Structure

- **`PDF_aws/`**: Contains PDFs and text files for AWS case studies.
- **`PDF_gcloud/`**: Contains PDFs and text files for Google Cloud case studies.
- **CSV Files**: Store links for case studies (`1.csv` for AWS, `2.csv` for Google Cloud).

## Notes

- Ensure the CSV files are correctly formatted before running the scripts.
- The scripts are set to scrape a specific number of pages or links but can be modified as needed.
- Generated PDFs and text files provide both the content and metadata for each case study.

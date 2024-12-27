import asyncio
from playwright.async_api import async_playwright
import csv

async def scrape_case_studies(url, output_file, max_links=568):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)

        case_study_links = []

        while len(case_study_links) < max_links:
            # Extract case study links
            links = await page.eval_on_selector_all(
                "//a[contains(@class, 'aOrzRd')]",
                "elements => elements.map(element => element.href)"
            )

            # Add only new links while maintaining order
            for link in links:
                if link not in case_study_links:
                    case_study_links.append(link)

            if len(case_study_links) >= max_links:
                break

            # Click the "More" button
            more_button = await page.query_selector("button:has-text('More')")
            if more_button:
                await more_button.click()
                await page.wait_for_timeout(2000)  # Wait for the new content to load
            else:
                print("No more 'More' button found.")
                break

        # Save the links to a CSV file
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["link"])  # Corrected column name
            for link in case_study_links[:max_links]:  # Corrected variable
                writer.writerow([link])

        print(f"Saved {len(case_study_links)} case study links to {output_file}")
        await browser.close()

# URL of the page to scrape
url = "https://cloud.google.com/customers?hl=en&sr=IiUIARIhGh9DT1JQVVNfVFlQRV9DVVNUT01FUl9DQVNFX1NUVURZIiMIERIfGh1TVUJfUkVHSU9OX0dST1VQX0FTSUFfUEFDSUZJQygMOggaBAoCZW4oAQ"
output_file = "2.csv"

# Run the scraper
asyncio.run(scrape_case_studies(url, output_file))

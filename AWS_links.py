from playwright.async_api import async_playwright
import asyncio
import pandas as pd

async def scrape_aws_case_studies():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto('https://aws.amazon.com/solutions/case-studies/')
        await page.wait_for_load_state('networkidle')
        
        all_links = []
        max_pages = 92
        current_page = 1
        
        while current_page <= max_pages:
            # Extract links
            links = await page.eval_on_selector_all(
                "//div[contains(@class, 'm-card-img')]/a",
                "elements => elements.map(element => element.href)"
            )
            all_links.extend(links)
            print(f"Page {current_page}: Found {len(links)} links")
            
            # Navigate to next page
            next_button = await page.query_selector("//a[contains(@class, 'm-icon-angle-right m-active')]")
            if next_button and current_page < max_pages:
                await next_button.click()
                await page.wait_for_load_state('networkidle')
                await page.wait_for_timeout(2000)
                current_page += 1
            else:
                break
        
        # Save links to CSV
        df = pd.DataFrame(all_links, columns=['link'])
        df.to_csv('1.csv', index=False)
        print(f"Saved {len(all_links)} links to 1.csv")
        
        await browser.close()

asyncio.run(scrape_aws_case_studies())
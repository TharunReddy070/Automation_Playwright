from playwright.async_api import async_playwright
import asyncio
import pandas as pd
import os
from pathlib import Path

async def save_pages_as_pdf_and_links():
    # Create PDF directory if it doesn't exist
    pdf_dir = Path('PDF_aws')
    pdf_dir.mkdir(exist_ok=True)
    
    # Read links from CSV
    df = pd.read_csv('1.csv')
    links = df['link'].tolist()
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        for index, link in enumerate(links, 1):
            try:
                print(f"Processing {index}/{len(links)}: {link}")
                
                # Navigate to the page
                await page.goto(link, wait_until='networkidle')
                await page.wait_for_load_state('networkidle')
                
                # Wait for content to load
                await page.wait_for_timeout(2000)
                
                # Save page as PDF
                pdf_path = pdf_dir / f"{index}.pdf"
                await page.pdf(path=str(pdf_path), format='A4')
                print(f"Saved PDF: {pdf_path}")
                
                # Save link as .txt
                txt_path = pdf_dir / f"{index}.txt"
                with open(txt_path, "w") as f:
                    f.write(link)
                print(f"Saved link: {txt_path}")
                
            except Exception as e:
                print(f"Error processing {link}: {str(e)}")
                continue
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(save_pages_as_pdf_and_links())

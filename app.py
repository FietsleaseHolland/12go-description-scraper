from fastapi import FastAPI
from playwright.sync_api import sync_playwright

app = FastAPI()

@app.get("/omschrijving")
def omschrijving(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, wait_until="networkidle")

        page.wait_for_selector("text=Omschrijving")

        tekst = page.locator("text=Omschrijving").locator("..").inner_text()

        browser.close()

        return {"omschrijving": tekst}

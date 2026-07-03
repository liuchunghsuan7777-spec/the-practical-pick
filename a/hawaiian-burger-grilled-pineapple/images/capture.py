import sys
from playwright.sync_api import sync_playwright

html_path = sys.argv[1]
out_path  = sys.argv[2]
width     = int(sys.argv[3]) if len(sys.argv) > 3 else 800

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": width, "height": 600},
                            device_scale_factor=2)
    page.goto("file://" + html_path)
    page.wait_for_load_state("networkidle")
    el = page.query_selector("#card")
    if el:
        el.screenshot(path=out_path)
    else:
        page.screenshot(path=out_path, full_page=True)
    browser.close()
print("saved", out_path)

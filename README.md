# Web Scrapping Python

## Structured Approach

1. Understanding the website's structure - inspect HTML code to identify the elements we want to scape. Once we find these elements we need to identify their HTML tags and attributes.

2. Setting up python playground - create virtual env to keep things organized and sandboxed

  ```py
    python3 -m venv scraping-env

    source scraping-env/bin/activate  # different on windows
  ```
3. good to start with requests and beautifulSoup libraries

4. Handling pagination and dynamic content - use tools like selenium in the headless browsing section to handle pagination and scrape websites that use javascript.

5. RESPECT THE WEBSITES's ROBOT.txt and LEGAL GUIDELINES - this file will tell use what parts of the website are okay to scrape and which ones are off-limits.

6. Optimizing and scaling our scraper


# Import the urllib3 library for making HTTP requests
import urllib3

# Create a connection pool manager (reuses connections for better performance)
# and send a GET request to the given URL
r = urllib3.PoolManager().request('GET', 'https://google.com')

# Print the raw response data (HTML content of the page)
print(r.data)
# It creates a connection pool manager and sends a GET request to the specified URL.


# Create a user-agent header to mimic a real browser (helps avoid blocks from some websites)
user_agent_header = urllib3.make_headers(user_agent="<USER_AGENT>")

# Define a proxy server with the correct scheme (http:// or https:// is required)
proxy = "http://123.45.67.89:8080"  # Add http:// or https://

# Use ProxyManager to route the request through the specified proxy and apply headers
pool = urllib3.ProxyManager(proxy, headers=user_agent_header)

# Make a GET request to the target URL using the proxy and custom headers
r = pool.request('GET', 'https://www.google.com')



"""
When to Use What
  🔰Use requests for:
      Quick scripts
      Simpler sites
      Clean, readable code

  🔰Use urllib3 for:
      Advanced control (proxies, retries, pooling)
      High-performance or multi-threaded scraping
      Integrating with low-level systems
"""
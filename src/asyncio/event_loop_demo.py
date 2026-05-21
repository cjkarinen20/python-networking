import asyncio 
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Response from {url}: {response.status}")
        return await response.text()
    
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gether(*tasks)
        
urls = ['http://example.com', 'https://api.github.com', 'https://www.python.org']
asyncio.run(main(urls))
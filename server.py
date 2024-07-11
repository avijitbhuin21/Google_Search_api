# Install required libraries
from IPython.display import clear_output

!pip install fastapi nest_asyncio pyngrok uvicorn

clear_output()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from cachetools import TTLCache
import json
from google.colab import runtime
from pyngrok import ngrok
import nest_asyncio
import uvicorn
import requests

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache configuration
CACHE_TTL = 3600  # 1 hour
CACHE_MAXSIZE = 1000
cache = TTLCache(maxsize=CACHE_MAXSIZE, ttl=CACHE_TTL)

# Rate limiting
RATE_LIMIT = 10
semaphore = asyncio.Semaphore(RATE_LIMIT)

async def fetch_url(session: aiohttp.ClientSession, query: str) -> dict:
    async with semaphore:
        cache_key = f"search:{query}"
        if cache_key in cache:
            return {query: cache[cache_key]}

        url = f'https://www.google.com/search?q={query}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        async with session.get(url, headers=headers) as response:
            if response.status == 429:
                return query
            elif response.status != 200:
                raise HTTPException(status_code=response.status, detail="Failed to fetch URL")
            
            content = await response.text()
            soup = BeautifulSoup(content, 'lxml')
            center_col = soup.find('div', id='center_col')
            links = center_col.find_all('a') if center_col else []
            url_list = list(set([
                link['href'] for link in links 
                if link.get('href', '').startswith('https://') and 'support.google.com' not in link['href']
            ]))
            
            cache[cache_key] = url_list
            return {query: url_list}

@app.get("/search")
async def search(query: str):
    queries = json.loads(query)['query']
    
    if not queries:
        raise HTTPException(status_code=400, detail="Query parameter is required")
    
    if '_ip' in queries:
        if '_ip' not in cache:
            cache['_ip'] = requests.get('https://api.ipify.org?format=json').json().get('ip')
        return cache['_ip']
    
    if '_Restart_Server' in queries:
        ngrok.kill()
        runtime.unassign()
        return {"message": "Server restarting"}

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, q) for q in queries]
        results = await asyncio.gather(*tasks)

    output = {
        "failed": [result for result in results if isinstance(result, str)],
        "success": {k: v for result in results if isinstance(result, dict) for k, v in result.items()}
    }

    return output

def main():
    ngrok.set_auth_token('2hxPZaWvWe8OguY0ZlFLmW9PXTm_4Gazibfk5KjJuoqxxZQNx')  # Replace with your Ngrok auth token
    ngrok_tunnel = ngrok.connect(addr="8000", proto="http", hostname="noble-raven-entirely.ngrok-free.app")
    print("Public URL:", ngrok_tunnel.public_url)

    nest_asyncio.apply()
    uvicorn.run(app, port=8000)

if __name__ == "__main__":
    main()


## To Kill Ngrok Server Manually
# ngrok.kill()

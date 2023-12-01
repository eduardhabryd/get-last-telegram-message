import os
import aiohttp


async def send_message(message):
    external_api_url = os.getenv("EXTERNAL_API_URL")
    if external_api_url:
        payload = {"message": message}
        async with aiohttp.ClientSession() as session:
            async with session.post(external_api_url, json=payload) as response:
                print(f" [x] Sent POST request to {external_api_url}. Response: {response.status}")

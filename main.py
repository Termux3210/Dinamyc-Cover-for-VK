import asyncio 
import os

from dotenv import load_dotenv
from vkbottle import API
from cover import CoverImage

load_dotenv()
TOKEN = os.getenv("TOKEN")
USER_ID = 539544739

api = API(TOKEN)
cover = CoverImage(api, USER_ID)

async def main() -> None:
    while True:
        await cover.draw_cover()
        await cover.upload_cover()
        await asyncio.sleep(600)

if __name__ == "__main__":
    asyncio.run(main())
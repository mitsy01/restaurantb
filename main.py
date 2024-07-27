from os import getenv
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.log.log import get_log
from app.routers.start import start_router
from app.routers.clients import client_router
from app.routers.reviews import review_router


load_dotenv()


root_router = Router()
root_router.include_routers(start_router, client_router, review_router)


async def main() -> None:
    TOKEN = getenv("BOTIC_API")

    botic = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(root_router)
    await dp.start_polling(botic)


if __name__ == "__main__":
    get_log()
    asyncio.run(main())
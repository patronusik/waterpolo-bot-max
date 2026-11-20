import aiohttp
from maxbot.types import Message
from config import TEXT_SUBSCRIBE, TEXT_WELCOME, CHANNEL_ID, MAX_BOT_TOKEN
from keyboards import subscribe_kb, main_menu_kb


async def is_user_subscribed(user_id: int) -> bool:
    url = f"https://platform-api2.max.ru/chats/{CHANNEL_ID}/members"
    headers = {"Authorization": MAX_BOT_TOKEN}
    params = {"user_ids": user_id}

    try:
        # ssl=False отключает проверку сертификата для этого запроса
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params, ssl=False) as resp:
                if resp.status != 200:
                    print(f"SUBSCRIPTION API ERROR: {resp.status}", flush=True)
                    return False
                data = await resp.json()
                return len(data.get("members", [])) > 0
    except Exception as e:
        print(f"SUBSCRIPTION CHECK FAILED: {e}", flush=True)
        return False


def register(dp, bot):

    @dp.bot_started
    async def on_bot_started(update):
        user_id = update['user']['user_id']
        print(f"BOT_STARTED: user_id={user_id}", flush=True)
        await bot.send_message(
            user_id=user_id, text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb, format="markdown"
        )

    @dp.message()
    async def on_message(message: Message):
        print(f"MESSAGE: sender={message.sender.id}", flush=True)
        await bot.send_message(
            user_id=message.sender.id, text=TEXT_SUBSCRIBE,
            reply_markup=subscribe_kb, format="markdown"
        )

from config import (
    TEXT_WELCOME, TEXT_NOT_SUBSCRIBED, TEXT_ABOUT, TEXT_ADDRESSES,
    TEXT_PAID_SERVICES, TEXT_FAQ_AGE, TEXT_CONTACTS
)
from keyboards import (
    main_menu_kb, back_to_menu_kb, subscribe_kb,
    faq_kb, back_to_faq_kb,
)
from handlers.start import is_user_subscribed


def register(dp, bot):

    @dp.callback()
    async def on_callback(cb):
        user_id = None
        if hasattr(cb, "user") and cb.user is not None:
            user_id = getattr(cb.user, "id", None) or (
                cb.user.get("user_id") if isinstance(cb.user, dict) else None
            )
        if user_id is None:
            user_id = getattr(cb, "user_id", None)

        callback_id = getattr(cb, "callback_id", None)
        if callback_id:
            try:
                await bot.answer_callback(callback_id=callback_id, notification="")
            except Exception as e:
                print(f"ANSWER_CALLBACK FAILED: {e}", flush=True)

        payload = cb.payload
        print(f"CALLBACK: payload={payload}, user_id={user_id}", flush=True)

        async def show(text, keyboard):
            await bot.send_message(
                user_id=user_id, text=text,
                reply_markup=keyboard, format="markdown"
            )

        if payload == "check_sub":
            if await is_user_subscribed(user_id):
                await show(TEXT_WELCOME, main_menu_kb)
            else:
                await bot.send_message(
                    user_id=user_id, text=TEXT_NOT_SUBSCRIBED,
                    reply_markup=subscribe_kb
                )
            return

        if payload == "back_to_menu":
            await show(TEXT_WELCOME, main_menu_kb)
            return

        if not await is_user_subscribed(user_id):
            await bot.send_message(
                user_id=user_id, text=TEXT_NOT_SUBSCRIBED,
                reply_markup=subscribe_kb
            )
            return

        if payload == "about":
            await show(TEXT_ABOUT, back_to_menu_kb)

        elif payload == "addresses":
            await show(TEXT_ADDRESSES, back_to_menu_kb)

        elif payload == "paid_services":
            import os
    file_exists = os.path.exists("files/price.pdf")
    print(f"PDF EXISTS: {file_exists}", flush=True)
            try:
                await bot.send_file(
                    user_id=user_id,
                    file_path="files/price.pdf",
                    media_type="file",
                    text=TEXT_PAID_SERVICES,
                    reply_markup=back_to_menu_kb
                )
                print(f"SEND_FILE OK: user_id={user_id}", flush=True)
            except Exception as e:
                print(f"SEND_FILE FAILED: {e}", flush=True)
                await show(TEXT_PAID_SERVICES, back_to_menu_kb)

        elif payload == "faq_menu":
            await show("❓ **Часто задаваемые вопросы**\n\nВыберите вопрос:", faq_kb)

        elif payload == "faq_age":
            await show(TEXT_FAQ_AGE, back_to_faq_kb)

        elif payload == "contacts":
            await show(TEXT_CONTACTS, back_to_menu_kb)

        else:
            print(f"UNHANDLED PAYLOAD: {payload}", flush=True)

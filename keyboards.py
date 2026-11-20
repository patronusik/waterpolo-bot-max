from maxbot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_URL, SITE_URL, APPEAL_URL

subscribe_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📢 Открыть канал", url=CHANNEL_URL)],
    [InlineKeyboardButton(text="✅ Я подписан", callback_data="check_sub")]
])

main_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏊 Об учреждении", callback_data="about")],
    [InlineKeyboardButton(text="📍 Адреса учреждения", callback_data="addresses")],
    [InlineKeyboardButton(text="💳 Платные услуги", callback_data="paid_services")],
    [InlineKeyboardButton(text="❓ Часто задаваемые вопросы", callback_data="faq_menu")],
    [InlineKeyboardButton(text="📞 Справочная информация", callback_data="contacts")],
    [InlineKeyboardButton(text="🌐 Официальный сайт", url=SITE_URL)],
    [InlineKeyboardButton(text="💬 Обращения граждан", url=APPEAL_URL)],
])

back_to_menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")]
])

faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Возраст приема", callback_data="faq_age")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

back_to_faq_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад к вопросам", callback_data="faq_menu")],
    [InlineKeyboardButton(text="🏠 На главную", callback_data="back_to_menu")],
])

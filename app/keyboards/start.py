from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_global_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Список кліентів")
    builder.button(text="Додати нового кліента")
    builder.button(text="Показати список заброньованих столів")
    builder.adjust(1)
    return builder.as_markup()
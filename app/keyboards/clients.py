from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_clients_keyboard(clients: list):
    builder = InlineKeyboardBuilder()
    for client in clients:
        builder.button(text=client, callback_data=f"client_{client}")

    builder.adjust(4)
    return builder.as_markup()


def build_clnt_action_keyboard(client: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Продати кліента", callback_data=f"booked_clnt_{client}")
    builder.button(text="Видалити кліента", callback_data=f"remove_clnt_{client}")
    return builder.as_markup()
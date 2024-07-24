from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext

from app.data import open_files, clients
from app.keyboards.clients import build_clients_keyboard, build_clnt_action_keyboard
from app.forms.client import ProductForm


client_router = Router()


async def edit_or_answer(message: Message, text: str, keyboard=None, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)


@client_router.message(F.text == "Список кліентів")
async def show_clients(message: Message, state: FSMContext):
    clients = open_files.get_c()
    keyboard = build_clients_keyboard(clients)
    text = "Список кліентів"
    return await edit_or_answer(message=message, text=text, keyboard=keyboard)


@client_router.callback_query(F.data.startswith("client_"))
async def clientt_actions(call_back: CallbackQuery, state: FSMContext):
    client = call_back.data.split("_")[-1]
    keyboard = build_clnt_action_keyboard(client)
    return await edit_or_answer(
        message=call_back.message,
        text=client,
        keyboard=keyboard
        )


@client_router.message(F.text == "Додати нового кліента")
async def add_clients(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ProductForm.name)
    await message.answer(text="Введіть ім'я кліента")


@client_router.message(ProductForm.name)
async def add_client_action(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = clients.add_client(data.get("name"))
    await message.answer(text=msg)


@client_router.callback_query(F.data.startswith("booked_clnt"))
async def booked_clients(call_back: CallbackQuery, state: FSMContext):
    client = call_back.data.split("_")[-1]
    msg = client.booked_clients(client)
    await call_back.message.answer(text=msg)


@client_router.callback_query(F.data.startswith("remove_clnt_"))
async def remove_client(call_back: CallbackQuery, state: FSMContext):
    client = call_back.data.split("_")[-1]
    msg = clients.remove_client(client)
    await call_back.message.answer(text=msg)


@client_router.message(F.text == "Показати список заброньованих столів")
async def show_booked_clients(message: Message, state: FSMContext):
    booked_clients = open_files.get_booked_clients()
    msg = ""

    for i, client in enumerate(booked_clients, start=1):
        msg += f"{i}. {client}\n"

    await message.answer(text=msg)
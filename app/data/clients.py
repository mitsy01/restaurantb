import json

from app.data import list_files, open_files



def add_client(client: str) -> str:
    clients = open_files.get_clients()

    if not client in clients:
        clients.append(client)

        with open(list_files.clients, "w", encoding="utf-8") as file:
            json.dump(clients, file)

        msg = f"Кліент '{client}' додано до списку."
    else:
        msg = f"Кліент '{client}' вже є у списку."

    return msg


def booked_client(client: str) -> str:
    clients = open_files.get_clients()
    booked_clients = open_files.get_booked_clients()

    if client in clients:
        clients.remove(client)
        booked_clients.append(client)

        with open(list_files.clients, "w", encoding="utf-8") as file:
            json.dump(clients, file)

        with open(list_files.booked_clients, "w", encoding="utf-8") as file:
            json.dump(booked_clients, file)

        msg = f"Кліент '{client}' забронював стіл."
    else:
        msg = f"Кліент '{client}' відсутній у списку"

    return msg


def remove_client(client: str) -> str:
    clients = open_files.get_clients()

    if client in clients:
        clients.remove(client)

        with open(list_files.clients, "w", encoding="utf-8") as file:
            json.dump(clients, file)

        msg = f"Кліента '{client}' успішно видалено"
    else:
        msg = f"Кліент '{client}' відсутній у списку"

    return msg
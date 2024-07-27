import os
import json

from app.data import list_files


if not os.path.exists(list_files.clients):
    with open(list_files.clients, "w", encoding="utf-8") as fh:
        json.dump([], fh)

if not os.path.exists(list_files.booked_clients):
    with open(list_files.booked_clients, "w", encoding="utf-8") as file:
        json.dump([], file)
       
 
if not os.path.exists(list_files.reviews):
    with open(list_files.reviews, "w", encoding="utf-8") as file:
        json.dump([], file)


def get_clients(path: str = list_files.clients) -> list:
    with open(path, "r", encoding="utf-8") as fh:
        clients = json.load(fh)

    return clients


def get_booked_clients(path: str = list_files.booked_clients) -> list:
    with open(path, "r", encoding="utf-8") as file:
        booked_clients = json.load(file)

    return booked_clients


def get_reviews(path: str = list_files.reviews) -> list:
    with open(path, "r", encoding="utf-8") as file:
        reviews = json.load(file)

    return reviews
from typing import Union
from fastapi import FastAPI

# import password module
from module.password import hash_password, check_password

# import module
from module.exceptKey import *

# import model
from model.apartment import *
from model.bill import *
from model.people import *
from model.vehicle import *
from model.service import *
from model.pairapartmentpeople import *
from model.temporarycard import *
from model.user import *

# import database
from database import sql_insert, sql_select, sql_update, sql_delete

# Init
app = FastAPI(
    title="Apartment Management",
    description="Project for subject: Công nghệ phần mềm, Đại học Bách Khoa Hà Nội",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "apartment",
            "description": "Apartment API"
        },
        {
            "name": "bill",
            "description": "Bill API"
        },
        {
            "name": "people",
            "description": "People API"
        },
        {
            "name": "vehicle",
            "description": "Vehicle API"
        },
        {
            "name": "service",
            "description": "Service API"
        },
        {
            "name": "pair_apartment_people",
            "description": "Pair Apartment People API"
        },
        {
            "name": "temporary_card",
            "description": "Temporary Card API"
        },
        {
            "name": "user",
            "description": "User API"
        },
    ],
    contact={
        "name": "Hotamago Master",
        "url": "https://www.linkedin.com/in/hotamago/",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

# Apartment
@app.get("/apartments", tags=["apartment"])
def get_apartments():
    return sql_select("apartments", {"1": "1"})

@app.get("/apartment/{id}", tags=["apartment"])
def get_apartment(id: int):
    return sql_select("apartments", {"id": id})

@app.get("/apartments_name/{name}", tags=["apartment"])
def get_apartments_by_name(name: str):
    return sql_select("apartments", {"name": name})

@app.get("/apartment/{id}/bills", tags=["apartment"])
def get_apartment_bills(id: int):
    return sql_select("bills", {"id_apartment": id})

@app.get("/apartment/{id}/vehicles", tags=["apartment"])
def get_apartment_vehicles(id: int):
    return sql_select("vehicles", {"id_apartment": id})

@app.get("/apartment/{id}/people", tags=["apartment"])
def get_apartment_people(id: int):
    list_pair = sql_select("pairapartmentpeople", {"id_apartment": id})
    list_people = []
    for pair in list_pair:
        list_people.append(sql_select("people", {"id": pair["id_people"]})[0])
    return list_people

@app.post("/apartment", tags=["apartment"])
def post_apartment(apartment: Apartment):
    return sql_insert("apartments", apartment.dict())

@app.put("/apartment/{id}", tags=["apartment"])
def put_apartment(id: int, apartment: Apartment):
    return sql_update("apartments", apartment.dict(), {"id": id})

@app.delete("/apartment/{id}", tags=["apartment"])
def delete_apartment(id: int):
    return sql_delete("apartments", {"id": id})

# Bill
@app.get("/bills", tags=["bill"])
def get_bills():
    return sql_select("bills", {"1": "1"})

@app.get("/bill/{id}", tags=["bill"])
def get_bill(id: int):
    return sql_select("bills", {"id": id})

@app.get("/bills_name/{name}", tags=["bill"])
def get_bills_by_name(name: str):
    return sql_select("bills", {"name": name})

@app.post("/bill", tags=["bill"])
def post_bill(bill: Bill):
    return sql_insert("bills", bill.dict())

@app.put("/bill/{id}", tags=["bill"])
def put_bill(id: int, bill: Bill):
    return sql_update("bills", bill.dict(), {"id": id})

@app.delete("/bill/{id}", tags=["bill"])
def delete_bill(id: int):
    return sql_delete("bills", {"id": id})

# People
@app.get("/people", tags=["people"])
def get_peoples():
    return sql_select("people", {"1": "1"})

@app.get("/people/{id}", tags=["people"])
def get_people(id: int):
    return sql_select("people", {"id": id})

@app.get("/people/{id}/apartments", tags=["people"])
def get_people_apartments(id: int):
    list_pair = sql_select("pairapartmentpeople", {"id_people": id})
    list_apartment = []
    for pair in list_pair:
        list_apartment.append(sql_select("apartments", {"id": pair["id_apartment"]})[0])
    return list_apartment

@app.post("/people", tags=["people"])
def post_people(people: People):
    return sql_insert("people", people.dict())

@app.put("/people/{id}", tags=["people"])
def put_people(id: int, people: People):
    return sql_update("people", people.dict(), {"id": id})

@app.delete("/people/{id}", tags=["people"])
def delete_people(id: int):
    return sql_delete("people", {"id": id})

# Vehicle
@app.get("/vehicles", tags=["vehicle"])
def get_vehicles():
    return sql_select("vehicles", {"1": "1"})

@app.get("/vehicle/{id}", tags=["vehicle"])
def get_vehicle(id: int):
    return sql_select("vehicles", {"id": id})

@app.get("/vehicles_name/{name}", tags=["vehicle"])
def get_vehicles_by_name(name: str):
    return sql_select("vehicles", {"name": name})

@app.post("/vehicle", tags=["vehicle"])
def post_vehicle(vehicle: Vehicle):
    return sql_insert("vehicles", vehicle.dict())

@app.put("/vehicle/{id}", tags=["vehicle"])
def put_vehicle(id: int, vehicle: Vehicle):
    return sql_update("vehicles", vehicle.dict(), {"id": id})

@app.delete("/vehicle/{id}", tags=["vehicle"])
def delete_vehicle(id: int):
    return sql_delete("vehicles", {"id": id})

# Service
@app.get("/services", tags=["service"])
def get_services():
    return sql_select("services", {"1": "1"})

@app.get("/service/{id}", tags=["service"])
def get_service(id: int):
    return sql_select("services", {"id": id})

@app.get("/services_name/{name}", tags=["service"])
def get_services_by_name(name: str):
    return sql_select("services", {"name": name})

@app.post("/service", tags=["service"])
def post_service(service: Service, tags=["service"]):
    return sql_insert("services", service.dict())

@app.put("/service/{id}", tags=["service"])
def put_service(id: int, service: Service):
    return sql_update("services", service.dict(), {"id": id})

@app.delete("/service/{id}", tags=["service"])
def delete_service(id: int):
    return sql_delete("services", {"id": id})

# Add function

@app.post("/service_calculate", tags=["service"])
def service_calculate(service_calculate: ServiceCalculate):
    return service_calculate.run_price()

# Pair Apartment People
@app.get("/pair_apartment_people", tags=["pair_apartment_people"])
def get_all_pair_apartment_peoples():
    return sql_select("pairapartmentpeople", {"1": "1"})

@app.post("/pair_apartment_people_object", tags=["pair_apartment_people"])
def get_pair_apartment_people(pair: PairApartmentPeople):
    return sql_select("pairapartmentpeople", pair.dict())

@app.post("/pair_apartment_people", tags=["pair_apartment_people"])
def post_pair_apartment_people(pair: PairApartmentPeople):
    return sql_insert("pairapartmentpeople", pair.dict())

@app.delete("/pair_apartment_people", tags=["pair_apartment_people"])
def delete_pair_apartment_people(pair: PairApartmentPeople):
    return sql_delete("pairapartmentpeople", pair.dict())

# Temporary Card
@app.get("/temporary_cards", tags=["temporary_card"])
def get_temporary_cards():
    return sql_select("temporarycard", {"1": "1"})

@app.get("/temporary_card/{id}", tags=["temporary_card"])

def get_temporary_card(id: int):
    return sql_select("temporarycard", {"id": id})

@app.get("/temporary_cards_by_iduser/{id_people}", tags=["temporary_card"])
def get_temporary_cards_by_name(id_people: int):
    return sql_select("temporarycard", {"id_people": id_people})

@app.post("/temporary_card", tags=["temporary_card"])
def post_temporary_card(temporary_card: TemporaryCard):
    return sql_insert("temporarycard", temporary_card.dict())

@app.put("/temporary_card/{id}", tags=["temporary_card"])
def put_temporary_card(id: int, temporary_card: TemporaryCard):
    return sql_update("temporarycard", temporary_card.dict(), {"id": id})

@app.delete("/temporary_card/{id}", tags=["temporary_card"])
def delete_temporary_card(id: int):
    return sql_delete("temporarycard", {"id": id})

@app.post("/temporary_cards_where", tags=["temporary_card"])
def get_temporary_cards_where(temporary_card: TemporaryCard):
    return sql_select("temporarycard", temporary_card.dict())

# User
@app.get("/users", tags=["user"])
def get_users():
    return exceptKey(sql_select("users", {"1": "1"}), ["password"])

@app.get("/user/{id}", tags=["user"])
def get_user(id: int):
    return exceptKey(sql_select("users", {"id": id}), ["password"])

@app.get("/users_by_username/{username}", tags=["user"])
def get_users_by_username(username: str):
    return exceptKey(sql_select("users", {"username": username}), ["password"])

@app.post("/user", tags=["user"])
def post_user(user: User):
    user.password = hash_password(user.password)
    return sql_insert("users", user.dict())

@app.put("/user/{id}", tags=["user"])
def put_user(id: int, user: User):
    # # Check if password is match with database
    # list_user = sql_select("users", {"id": id})
    # if len(list_user) == 0:
    #     return False
    # if not check_password(user.password, list_user[0]["password"]):
    #     return False
    # # Hash password
    # user.password = hash_password(user.password)
    return sql_update("users", exceptKey(user.dict(), ["password"]), {"id": id})

@app.put("/user_change_password/{id}", tags=["user"])
def put_user_change_password(id: int, user: UserChangePassword):
    # Check if password is match with database
    list_user = sql_select("users", {"id": id})
    if len(list_user) == 0:
        return False
    if not check_password(user.password, list_user[0]["password"]):
        return False
    # Hash password
    user.new_password = hash_password(user.new_password)
    return sql_update("users", {"password": user.new_password}, {"id": id})

@app.delete("/user/{id}", tags=["user"])
def delete_user(id: int):
    return sql_delete("users", {"id": id})

@app.post("/user_login", tags=["user"])
def user_login(user: UserLogin):
    list_user = sql_select("users", {"username": user.username})
    if len(list_user) == 0:
        return False
    if check_password(user.password, list_user[0]["password"]):
        return True
    return False

# Run
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
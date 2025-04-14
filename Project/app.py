from fastapi import FastAPI
from functions import *
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(docs_url='/api/documentation', title="Flarion Development INC.", description="Flarion Development INC. API", version="1.0.0",)


@app.get("/")
async def index():
    return {
        "message": "Flarion Development INC.",
        "status": "API Aktif!",
    }


@app.get("/phone/{phonenumber}/{country}")
async def phone_info(phonenumber: str, country: str):
    phone = Phone()
    phone.set_phone_number(phonenumber)
    phone.set_country_code(country)

    is_number_valid,is_possible_number,number_type,isp=get_phone_info(phone.phonenumber, phone.country_code)
    
    if is_number_valid==False:
        return {
            "message": "Böyle Bir Numara Bulunmuyor",
            "Böyle Bir Numara Olması Mümkün mü?": is_possible_number
        }
    else:
        return {
            "phone_number": phone.phonenumber,
            "country_code": phone.country_code,
            "is_number_valid": is_number_valid,
            "is_possible_number": is_possible_number,
            "number_type": number_type,
            "isp": isp
        }


@app.get("/phone/{phonenumber}")
async def without_country_phone_info(phonenumber: str):
    phone = Phone()
    phone.set_phone_number(phonenumber)
    response = dummy_get_phone_info(phone.phonenumber)
    return response
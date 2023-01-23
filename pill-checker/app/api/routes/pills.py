import json
import glob
from fastapi import APIRouter
from services.pills_info import load_pill_data, scrape_data

router = APIRouter()

def fetch_pill_data(pill_name = "Blue Kenzo"):

    pill_data = load_pill_data()
    pill_data = pill_data[pill_data["Name"] == pill_name]

    return pill_data

def scrape_pill_data():

    pill_data = scrape_data()

    return pill_data    

@router.get(
    "/pills",
)
async def fetch_pill():
    return {"test" : f'{fetch_pill_data()}'}


@router.get(
    "/pills/scrape",
)
async def scrape_pill():
    return {"scrape" : f'{scrape_pill_data()}'}

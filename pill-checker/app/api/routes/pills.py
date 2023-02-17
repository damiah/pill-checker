import json
import glob
from fastapi import APIRouter, Response
import re
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder
from services.pills_info import load_pill_data, scrape_data

router = APIRouter()

def fetch_pill_data(pill_name = "Blue Kenzo"):

    pill_data = load_pill_data()
    pill_data = pill_data[pill_data["Name"] == pill_name]
    pill_data = pill_data.apply(lambda s:s.str.replace('”', ""))
    pill_data = pill_data.apply(lambda s:s.str.replace('“', ""))
    pill_data = pill_data.to_dict(orient='records')
    #to get double quotes
    pill_data = json.dumps(pill_data)

    return pill_data

def scrape_pill_data():

    pill_data = scrape_data()

    return pill_data

@router.get(
    "/pills",
)
async def fetch_pill():
    return {f'{fetch_pill_data()}'}


@router.get(
    "/pills/scrape",
)
async def scrape_pill():
    return {"scrape" : f'{scrape_pill_data()}'}

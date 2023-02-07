import os

from loguru import logger
import pandas as pd
import bs4
import requests
import glob

from core.config import CROPPED_PILL_PATH, PILL_INFO, PILL_INFO_URL

def load_pill_data():
    
    pill_info_path = PILL_INFO
    if not os.path.exists(pill_info_path):
        message = f"No pill data exists!"
        logger.error(message)
        raise FileNotFoundError(message)

    pill_data = pd.read_pickle(pill_info_path)

    return pill_data
    
def scrape_data():
    
    pill_data = requests.get(url=PILL_INFO_URL)
    soup = bs4.BeautifulSoup(pill_data.content, 'html.parser')
    tables = soup.find_all('table')
    table = tables[0]
    table_rows = table.find_all('tr')

    res = []
    for tr in table_rows[1:]:
        td = tr.find_all('td')
        #find the title
        if tr.find_all('b'):
            title = tr.find_all('b')[0].text
        elif tr.find_all('strong'):
            title = tr.find_all('strong')[0].text
        else:
            title = ''
            
        #find the url for the image
        if tr.find_all('img'):
            img_link = tr.find_all('img')[0]['data-large-file']
        else:
            img_link = ''
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        
        row.insert(0, title)
        row.insert(2, img_link)
        if row:
            res.append(row)

    df = pd.DataFrame(res, columns=["Name", "Description", "Image"])
    df.to_pickle(PILL_INFO)

    return df.head()


def find_image_saved_names(img_name):
    '''Using the name of the image from the saved pill_info.pkl file,
    we can find the possible saved cropped image names'''

    cropped_image_path_list = glob.glob(f"{CROPPED_PILL_PATH}*.png")
    possible_image_path_names = [f'{CROPPED_PILL_PATH}{img_name.replace("/", "_") + "_" + str(i)}.png'
                                             for i in range(1,5)]
    possible_image_path_names.append(f'{CROPPED_PILL_PATH}{img_name.replace("/", "_")}.png')
    
    saved_image_names = list(set(possible_image_path_names) & set(cropped_image_path_list))

    return saved_image_names

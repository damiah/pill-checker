from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from services.image_model import load_sentence_model, find_closest_pills
from core.config import UPLOADED_PILL_PATH

router = APIRouter()

@router.post("/files/")
async def create_files(files: list[bytes] = File(description="Multiple files as bytes")):
    # model = load_sentence_model()
    contents = await files[0].decode('utf-8').read() 

    # similar_images = find_closest_pills(model, files)
    return {"file_sizes": [len(file) for file in files], "similar_images": [contents]}
    # return {"file_sizes": [len(file) for file in files], "similar_images": similar_images}

@router.post("/uploadfiles/")
def upload(file: UploadFile = File(...)):

    image = file.file.read()
    upload_path = f'{UPLOADED_PILL_PATH}/{file.filename}'
    with open(upload_path, 'wb') as f:
        f.write(image)
    file.file.close()
    model = load_sentence_model()
    similar_images = find_closest_pills(model, upload_path)

    content = f"""
            <body>
            <img src="{upload_path}" alt="Trulli" width="500" height="333">
            </body>
                """
    return FileResponse(upload_path) 
    # HTMLResponse(content=content)
    # return {"message": f"Successfully uploaded {file.filename} and {similar_images}"}

@router.get("/upload/")
async def show_upload_file():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

# @router.get("/")
# async def main():
#     return FileResponse(some_file_path)
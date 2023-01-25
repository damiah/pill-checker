from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.post("/files/")
async def create_files(files: list[bytes] = File(description="Multiple files as bytes")):
    return {"file_sizes": [len(file) for file in files]}

@router.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile] = File(description="Multiple files as UploadFile")):
    return {"filenames": [file.filename for file in files]}

@router.get("/upload/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
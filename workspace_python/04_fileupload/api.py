# pip install fastapi, python-multipart, uvicorn

from fastapi import FastAPI, Form, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
from datetime import datetime
import uuid

app = FastAPI()

dir = Path('uploads')
dir.mkdir(exist_ok=True)

@app.post('/upload')
async def upload(
    # title = Form(...), # ... : 명시적으로 필수값 표시
    title = Form(),      # ...은 생략 가능하다
    content = Form(None), # None : 필수 아님
    # file1 : Form(None) # 알아서 잘 들어오긴 하지만...
    file1 : UploadFile = File(),
    file2 : list[UploadFile] = File()
):
    print('title : ', title)
    print('content : ', content)
    # print('file1 : ', file1)
    
    print('filename: ', file1.filename)
    print('size : ', file1.size)
    
    filename_og = file1.filename
    
    # print('now', datetime.now())
    # # f : 마이크로 초
    # print('now', datetime.now())
    # t = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    # filename_safe = f'{t}_{filename_og}'
    
    print('uuid.uuid4 : ', uuid.uuid4())
    filename_safe = f'{uuid.uuid4().hex}_{filename_og}'
    
    # 경로 합치기
    # "/" : Path가 지정한 결합 연산자
    target_path = dir / filename_safe
    # w : 쓰기
    # b : binary
    # with open(target, 'wb') as buffer : 
    with target_path.open('wb') as buffer :
        # buffer.write를 사용해도 되지만 큰 파일의 경우 메모리 등의 문제
        # buffer.write(file1.read())
        
        # while True :
        #     chunk = await file1.read(8 * 1024)
        #     if not chunk :
        #         break
        #     buffer.write(chunk)
        
        # shutil.copyfileobj는 조금씩 쪼개서 안전하고 효율적으로 저장할 수 있다.
        shutil.copyfileobj(file1.file, buffer)
        
    # file2 처리 여러 개 업로드 처리
    for f in file2 :
        print(f.filename)

@app.get('/download')
def download(file_name) :
    file_path = dir / file_name
    
    if not file_path.exists() :
        raise HTTPException(
            status_code=404,
            detail="파일을 찾을 수 없습니다"
        )
        
    
    return FileResponse(
        path=file_path,
        # filename=file_name,
        filename = 'a.txt',
        media_type='application/octet-stream')

        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True, host="0.0.0.0")
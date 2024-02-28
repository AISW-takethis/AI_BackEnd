from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
import json
import subprocess

app = FastAPI()

@app.post('/process_image')
async def process_image(file: UploadFile = File(...)):
    try:
        # 클라이언트로부터 받은 이미지를 /data/samples 폴더에 저장
        name_of_file = file.filename
        file_path = f'./data/samples/{file.filename}'
        with open(file_path, 'wb') as image_file:
            shutil.copyfileobj(file.file, image_file)
        
        # 이미지 처리 실행
        subprocess.run(["python", "/app/detect.py"])
        result = subprocess.run(["python", "/app/detect.py"], capture_output=True, text=True)
        print(result.stderr)    

        # 처리된 이미지 읽기
        processed_image_path = f'./output/{name_of_file}'
        # 이미지 파일 읽기
        with open(processed_image_path, 'rb') as processed_image_file:
            processed_image_data = processed_image_file.read()

        # 실행 완료한 이미지 samples 폴더에서 삭제
        if os.path.exists(processed_image_path):
            os.remove(processed_image_path)
            print(f"{processed_image_path} 파일이 삭제되었습니다.")
        if os.path.exists(processed_image_path):
            os.remove(file_path)
            print(f"{file_path} 파일이 삭제되었습니다.")

        
        # 단어 목록 받아오기
        class_file_path = './food_classes.txt'

        with open(class_file_path, 'r') as file:
            food_classes = [int(line.strip()) for line in file]


            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"{file_path} 파일이 삭제되었습니다.")
            else:
                print(f"{file_path} 파일이 존재하지 않습니다.")

        response = {\
            "processed_image": processed_image_data.hex(), \
            "food_classes": food_classes}

        # 딕셔너리를 JSON 문자열로 변환
        json_response = json.dumps(response)
        return json_response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
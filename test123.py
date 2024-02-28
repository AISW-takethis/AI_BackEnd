import subprocess

# 다른 파일 실행
subprocess.run(["python", "detect.py"])

processed_image_path = f'app/output/{file.filename}'
with open(processed_image_path, 'rb') as processed_image_file:
    processed_image_data = processed_image_file.read()
if(processed_image_data):
    print("success")
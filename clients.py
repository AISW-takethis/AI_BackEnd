import requests

url = 'http://192.168.45.102:2375/process_image'
# url = 'tcp://localhost:2375/process_image'

files = {'file': ('gimbab.JPG', open('C:/Users/Yul/yyamyyam/data/samples', 'rb'), 'image/jpeg')}
data = {'title': 'req_img', 'content': 'request for processing image'}

# API 호출
response = requests.post(url, files=files, data=data)

# 결과 수신 및 처리
result = response.json()
processed_image_data = result['processed_image']
processed_image_bytes = bytes.fromhex(processed_image_data)

# 처리된 이미지를 파일로 저장
with open('processed_image.jpg', 'wb') as file:
    file.write(processed_image_bytes)

# 결과에서 단어 리스트 추출
food_classes = result.get('food_classes', [])

# 여러 개의 단어를 가진 리스트 출력
print("food_classes:", food_classes)
import ngrok
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():

    data = request.data.decode('utf-8')  # 텍스트 데이터를 UTF-8로 디코딩
    print({"received_data": data})  # 데이터를 출력합니다.

    # 빈 응답을 204 No Content 상태 코드로 반환
    return '', 204

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
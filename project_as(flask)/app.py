from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse
import socket

app = Flask(__name__)

#URL확인 결과
res_xss = "" #XSS확인 결과
res_reliable = "" #신뢰성 사이트여부 확인 결과

#데이터 파일 읽어오기
xss_li=[]
with open('./data/xss_li.txt',encoding='utf8') as f:
    for line in f:
        xss_li.append(line.rstrip('\n'))
reliable_li=[]
with open('./data/reliable.txt', 'r') as f:
    for line in f:
        reliable_li.append(line.rstrip('\n'))

#URL확인 함수
def check_url(url): #Func: XSS체크 함수
    for i in xss_li:
        if i in url:
            return "XSS"
    return "Not XSS"

def check_reliable(url): #Func: 신뢰성 사이트 여부 확인 함수
    host = urlparse(url).hostname #대상 사이트의 DNS주소 읽기
    
    for i in reliable_li:
        if i==host:
            return "Reliable", host
    return "Not Reliable", host


@app.route("/",methods=["GET"])
def url_Result():
    url = request.args.get("url", default="null", type = str)

    res_xss = check_url(url)
    res_reliable,res_host = check_reliable(url)
    
    return jsonify(res_host, res_xss, res_reliable)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
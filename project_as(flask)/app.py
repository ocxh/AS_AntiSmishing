from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

xss_li = ["document.cookie", "<script", "</script>", "<img","window.open"]

def check_url(url):
    for i in xss_li:
        if i in url:
            return "Smishing URL"
            
    return "%s is ok"%url

@app.route("/",methods=["GET"])
def url_Result():
    url = request.args.get("url", default="null", type = str)
    res = check_url(url)
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
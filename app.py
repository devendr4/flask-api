from flask import Flask

app = Flask("test")


@app.route("/", methods=["GET"])
def test():
    return {"msg": "hello world"}

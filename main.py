from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.get("/")
def handle_get_home():
    return render_template("index.html")


@app.post("/")
def handle_post_home():
    body = request.get_json()
    print(body)
    response_data = {
        "fulfillmentResponse": {
            "messages": [
                {
                    "text": {
                        "text": ["Hi, how can I help you?"]
                    }
                },
                {
                    "payload": {
                        "richContent": [
                            [
                                {
                                    "type": "button",
                                    "icon": {
                                        "type": "chevron_right",
                                        "color": "#FF9800"
                                    },
                                    "text": "Button text",
                                    "link": "https://example.com",
                                    "event": {
                                        "name": "",
                                        "languageCode": "",
                                        "parameters": {}
                                    }
                                }
                            ]
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)

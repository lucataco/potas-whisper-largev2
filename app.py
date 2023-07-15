from potassium import Potassium, Request, Response
import torch
import whisper
import os
import base64
from io import BytesIO

app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    # Whisper model type:
    model_name = "large-v2"
    model = whisper.load_model(model_name)
    context = {
        "model": model
    }

    return context

# @app.handler runs for every call
@app.handler()
def handler(context: dict, request: Request) -> Response:
    input = request.json.get("input")
    model = context.get("model")

    # Parse out your arguments
    if input == None:
        return {'message': "No input file provided"}
    
    mp3Bytes = BytesIO(base64.b64decode(input.encode("ISO-8859-1")))
    with open('input.mp3','wb') as file:
        file.write(mp3Bytes.getbuffer())
    
    # Run the model
    result = model.transcribe("input.mp3")
    output = {"text":result["text"]}
    os.remove("input.mp3")

    return Response(
        json = {"output": output}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()
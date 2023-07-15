import banana_dev as client
from io import BytesIO
from PIL import Image
import base64

# Localhost test
my_model = client.Client(
    api_key="",
    model_key="",
    url="http://localhost:8000",
)

# Encode mp3 file
with open(f'test.mp3','rb') as file:
    mp3bytes = BytesIO(file.read())
mp3 = base64.b64encode(mp3bytes.getvalue()).decode("ISO-8859-1")

inputs = {
    "input": mp3,
}

# Call your model's inference endpoint on Banana.
# If you have set up your Potassium app with a
# non-default endpoint, change the first
# method argument ("/")to specify a
# different route.
result, meta = my_model.call("/", inputs)
print(result)

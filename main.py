from PIL import Image
from flask import (Flask, render_template, request)
import uuid

app = Flask(__name__)


@app.route('/')
def hello():


    return render_template('index.html')


@app.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    success= True
    file = request.files['filename']

    pil_image = Image.open(file)
    if pil_image.size != (512,512):
     success= False


## For debugging purposes only 
    ##pil_image.thumbnail((512, 512))

    # pil_image = pil_image.convert("RGB")
    image = Image.new("RGBA", pil_image.size, "GOLD")
    image.paste(pil_image, (0, 0), pil_image)

    ## Generate a random UUID for concatenation into the file name
    uniqueUUID = str(uuid.uuid4())
    badgeFileName = "static/files/" + uniqueUUID + ".jpg"
    ##badgeFileName = "static/files/test.jpg"

    image.convert('RGB').save(badgeFileName, "JPEG")

    ## For Debugging purposes only
    ##image.show()

    return render_template('result.html' , generatedBadgeFileName = badgeFileName,success=success)



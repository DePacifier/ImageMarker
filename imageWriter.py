from PIL import Image, ImageDraw, ImageFont


marker = Image.open("marker.png")
markerX, markerY = marker.size

def loadImage(path):
    return Image.open(path)

def picMark(pic):
    picX, picY = pic.size
    pic.paste(marker,(picX - markerX ,picY - markerY))
    
    return pic

def textMark(pic):
    picX, picY = pic.size
    draw =ImageDraw.Draw(pic)
    font = ImageFont.truetype("CuteFont-Regular.ttf", size=40)
    location = (picX // 2, picY // 2)
    text = "Dan Carr\nPhotography"
    draw.text((location), text, fill = "blue", font = font)

    return pic

#Loading An Image
image = loadImage("Screenshot (1).png")
#Using Text Marking
#textMark(image).show()
#Using Picture Marking
picMark(image).show()
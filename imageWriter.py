from PIL import Image, ImageDraw, ImageFont

image = Image.open("Screenshot (1).png")
marker = Image.open("marker.png")
markerX, markerY = marker.size

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

textMark(image).show()
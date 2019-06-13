def setup():
    global img
    img = loadImage("zdjecie.jpg")
    size(198,255)
    image(img, 0, 0)
def draw():
    if mousePressed:
        webImg = loadImage("okular1.png")
        image(webImg,50,70,width/2, height/2)
    if keyPressed:
        if key == 'S' or key == 's':
            webImg = loadImage("okular3.png")
            image(webImg,50,70,width/2, height/2)
            
#zmiana okularopodobnej rzeczy za pomocą naciśnięcia myszy i naciskaniu S naprzemian

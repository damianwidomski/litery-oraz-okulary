def setup():
    size(400,400)
    textSize(70)
def draw():
    background(0)
    text("D", width/2-50, height/2)
    text("W", width/2+20, height/2)
    fill(155)
    print(mouseX,mouseY)
    if keyPressed:
        fill(1)
        if key == 'W' or key == 'w':
            fill(255, 0, 0)
            text("W", width/2+20, height/2)
            fill(1)
    if keyPressed:
        fill(1)
        if key == 'D' or key == 'd':
            fill(255, 0, 0)
            text("D", width/2-50, height/2)
            fill(1)
    if (mouseX>=155 and mouseX<=205 and mouseY>=147 and mouseY<=200):
        text("W", width/2+20, height/2)
        fill(255)
        if keyPressed:
            if keyCode == 39 and mouseX>=155 and mouseX<=205 and mouseY>=147 and mouseY<=200:
                fill(255, 0, 0)
                text("W", width/2+20, height/2)
                fill(155)
                print(keyCode)
    if (mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200):
        text("D", width/2-50, height/2)
        fill(255)
        if keyPressed:
            fill(155)
            if keyCode == 37 and mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200:
                fill(0, 255, 0)
                text("D", width/2-50, height/2)
                fill(1)
                print(keyCode)

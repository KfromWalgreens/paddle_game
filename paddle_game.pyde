ball_y = 100
y_speed = 5
ball_x = 200
x_speed = 5
paddle_width = 100
paddle_height = 20
brick_positionX = 10
brick_height = 20
hit1 = False
hit2 = False
hit3 = False
hit4 = False
hit5 = False

def setup():
    size(500,500)
    background(255,255,255)
    rect(brick_positionX,30,100,20)
    rect(brick_positionX *10,30,100,20)
    rect(brick_positionX *20,30,100,20)
    rect(brick_positionX *30,30,100,20)
    rect(brick_positionX *40,30,100,20)
    noStroke()
def draw():
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global brick_positionX
    global brick_height
    global hit1
    global hit2
    global hit3
    global hit4
    global hit5
    background(255,255,255)
    fill(0,0,0)
    line(0,490,500,490)
    rect(mouseX - paddle_width/2, 400, paddle_width, paddle_height)
    fill(0,0,0)
    ellipse(ball_x, ball_y, 20, 20)
    fill(50,50,50)
    rect(brick_positionX,30,100,20)
    rect(brick_positionX *10,30,100,20)
    rect(brick_positionX *20,30,100,20)
    rect(brick_positionX *30,30,100,20)
    rect(brick_positionX *40,30,100,20)
    if ball_y == 390 and ball_x < mouseX + paddle_width/2 and ball_x > mouseX - paddle_width/2:
        #print("bounce bounce baby")
        y_speed = -y_speed 
    
    if ball_y > 55:
        fill(50,50,50)
        rect(brick_positionX *40,30,100,20)
        
        
    if ball_y < 55 :
        #print("bounce bounce baby")
        y_speed =  -y_speed
        if ball_x >= brick_positionX  and ball_x < brick_positionX * 10:
            hit1 = not hit1
        if ball_x >= brick_positionX *10 and ball_x < brick_positionX * 20:
            hit2 = not hit2
        if ball_x >= brick_positionX *20 and ball_x < brick_positionX * 30:
            hit3 = not hit3
        if ball_x >= brick_positionX *30 and ball_x < brick_positionX * 40:
            hit4 = not hit4
        if ball_x > brick_positionX *40:
            hit5 = not hit5 
    if hit1:
       fill(255,255,255)
       rect(brick_positionX,30,100,20)
    if hit2:
       fill(255,255,255)
       rect(brick_positionX *10,30,100,20)
    if hit3:
       fill(255,255,255)
       rect(brick_positionX *20,30,100,20)
    if hit4:
       fill(255,255,255)
       rect(brick_positionX *30,30,100,20)
    if hit5:
       fill(255,255,255)
       rect(brick_positionX *40,30,100,20) 
    
    if ball_x > 490:
        x_speed = -x_speed
    if ball_x < 10:
        #print("bounce bounce baby")
        x_speed =  -x_speed 
    
    if ball_y >= 490:
        background(0,0,0)
        fill(255, 0, 93)
        textSize(40)
        text("Game Over :)))", 130, 250)
        noLoop()
    ball_y += y_speed
    ball_x += x_speed

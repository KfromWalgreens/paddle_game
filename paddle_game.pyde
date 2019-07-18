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
hit6 = False
hit7 = False
hit8 = False
hit9 = False

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
    global hit6
    global hit7
    global hit8
    global hit9
    background(255,255,255)
    fill(0,0,0)
    line(0,490,500,490)
    rect(mouseX - paddle_width/2, 400, paddle_width, paddle_height)
    fill(240, 65, 97)
    ellipse(ball_x, ball_y, 20, 20)
    fill(50,50,50)
    rect(brick_positionX,30,100,20)
    rect(brick_positionX *10,30,100,20)
    rect(brick_positionX *20,30,100,20)
    rect(brick_positionX *30,30,100,20)
    rect(brick_positionX *40,30,100,20)
    rect(brick_positionX *10, 50, 100, 20)
    rect(brick_positionX *20, 50, 100, 20)
    rect(brick_positionX *30, 50, 100, 20)
    rect(brick_positionX *20, 70, 100, 20)
    
    # makes the paddle work and makes the ball bounce when it hits it
    if ball_y == 390 and ball_x < mouseX + paddle_width/2 and ball_x > mouseX - paddle_width/2:
        #print("bounce bounce baby")
        y_speed = -y_speed
    
  #makes the ball bounce when it hits the last row of bricks   
    if ball_y < 95 :
        #print("bounce bounce baby")
        if ball_x >= brick_positionX *10  and ball_x < brick_positionX * 20 and hit9 == False:
            y_speed =  -y_speed
            hit9 = not hit9
            
 #makes the ball bounce when it hits the last row of bricks
    if ball_y < 75 :
        #print("bounce bounce baby")
        if ball_x >= brick_positionX *10  and ball_x < brick_positionX * 20 and hit6 == False:
            y_speed =  -y_speed
            hit6 = not hit6
        if ball_x >= brick_positionX *20 and ball_x < brick_positionX * 30 and hit7 == False:
            y_speed =  -y_speed
            hit7 = not hit7
        if ball_x >= brick_positionX *30 and ball_x < brick_positionX * 40 and hit8 == False:
            y_speed =  -y_speed
            hit8 = not hit8  
            
              
                  
    #makes the ball bounce when it hits the last row of bricks
    if ball_y < 55 :
        #print("bounce bounce baby")
        if ball_x >= brick_positionX  and ball_x < brick_positionX * 10 and hit1 == False:
            y_speed =  -y_speed
            hit1 = not hit1
        if ball_x >= brick_positionX *10 and ball_x < brick_positionX * 20 and hit2 == False:
            y_speed =  -y_speed
            hit2 = not hit2
        if ball_x >= brick_positionX *20 and ball_x < brick_positionX * 30 and hit3 == False:
            y_speed =  -y_speed
            hit3 = not hit3
        if ball_x >= brick_positionX *30 and ball_x < brick_positionX * 40 and hit4 == False:
            y_speed =  -y_speed
            hit4 = not hit4
        if ball_x > brick_positionX *40 and hit5 == False:
            y_speed =  -y_speed
            hit5 = True 
            
    #makes each row of bricks disappear
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
    if hit6:
       fill(255,255,255)
       rect(brick_positionX *10,50,100,20)
    if hit7:
       fill(255,255,255)
       rect(brick_positionX *20,50,100,20)
    if hit8:
       fill(255,255,255)
       rect(brick_positionX *30,50,100,20)
    if hit9:
       fill(255,255,255)
       rect(brick_positionX *20,70,100,20)
       
       
       
    #makes the ball bounce off the top wall once all of the bricks are gone
    if ball_y < 10 and hit1 == True and hit2 == True and hit3 == True and hit4 == True and hit5 == True and hit6 == True and hit7 == True and hit8 == True and hit9 == True: 
        y_speed =  -y_speed
    if ball_y < 10 and hit2 == True:
        y_speed =  -y_speed
    if ball_y < 10 and hit3 == True: 
        y_speed =  -y_speed
    if ball_y < 10 and hit4 == True: 
        y_speed =  -y_speed
    if ball_y < 10 and hit5 == True: 
        y_speed =  -y_speed
    if hit1 == True and hit2 == True and hit3 == True and hit4 == True and hit5 == True and hit6 == True and hit7 == True and hit8 == True and hit9 == True:
        background(0,0,0)
        fill(255, 0, 93)
        textSize(40)
        text("GG :)))", 190, 250)
        noLoop()
    
   
    #keeps the ball from temp disappearing behind the whited-out bricks 
    fill(240, 65, 97)
    ellipse(ball_x, ball_y, 20, 20)    
    
    if ball_x > 490:
        x_speed = -x_speed
    if ball_x < 10:
        #print("bounce bounce baby")
        x_speed =  -x_speed 
    if keyPressed: 
        background(255,255,255)
        hit1 = False
        hit2 = False
        hit3 = False
        hit4 = False
        hit5 = False
        hit6 = False
        hit7 = False
        hit8 = False
        hit9 = False
        ball_y = 100
        y_speed = 5
        ball_x = 200
        x_speed = 5
        brick_positionX = 10
        brick_height = 20
             
    if ball_y >= 490:
        background(0,0,0)
        fill(255, 0, 93)
        textSize(40)
        text("Game Over :)))", 130, 250)

    ball_y += y_speed
    ball_x += x_speed

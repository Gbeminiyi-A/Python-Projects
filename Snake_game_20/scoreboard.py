from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 10, 'normal')

with open('data.txt', 'r') as file:
    high_score = int(file.readline())
    

class ScoreBoard(Turtle, ):

    def __init__(self, ):
        super().__init__()
        self.i = 0
        self.high_score = high_score
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.hideturtle()
        self.clear_board()
        

    def clear_board(self):
        self.clear()
        self.write(arg=f'Score: {self.i} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write(arg='GAME OVER', move=False, align=ALIGNMENT, font=FONT)


    def count_score(self):
        self.i += 1
        self.clear_board()
 

    def reset_score(self):
        if self.i > self.high_score:
            with open('data.txt', 'w') as score:
                new_score = str(self.i)
                score.write(new_score)
                self.high_score = self.i
        self.i = 0
        self.clear_board()
        
        
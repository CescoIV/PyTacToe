board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
not_won = True
player = 'x'
def updateCoord(num,player):
  board[num[0]][num[1]] = player
def play():
  
  global player
  print('Current player is: ',player)
  print('Here is the board:')
  for row in board:
    print(row)
  nums = []
  for x in input('select coordinates: input as x,y').split(','):
    nums.append(int(x))
  
  print(nums)
  
  updateCoord(nums,player)

  if player == 'x':
    player ='o'
  else:
    player = 'x'
while not_won:
  play()
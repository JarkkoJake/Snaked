from .Colors import Colors

class GameSettings:
  numberOfFood = 5
  flies = False
  eggs = False
  speed = 60
  randomRock = 0
  asteroidRate = 0
  player1Color = Colors.BLUE

  player2Color = Colros.RED
  coloredFood = False
  coloredFlies = False
  coloredEggs = False

  def changeNumberOfFood(increase):
    if increase and GameSettings.numberOfFood < 10:
      GameSettings.numberOfFood += 1
    elif not increase and GameSettings.numberOfFood > 3:
      GameSettings.numberOfFood -= 1
  
  def toggleFlies():
    GameSettings.flies = not GameSettings.flies
  def toggleEggs():
    GameSettings.eggs = not GameSettings.eggs
  
  def changeSpeed(increase):
    if increase and GameSettings.speed > 10:
      GameSettings.speed -= 10
    elif not increase and GameSettings.speed < 60:
      GameSettings.speed += 10

  def changeRandomRockCount(increase):
    if increase and GameSettings.randomRock < 30:
      GameSettings.randomRock += 5
    elif not increase and GameSettings.randomRock > 0:
      GameSettings.randomRock -= 5
  
  def changeAsteroidRate(increase):
    if increase and GameSettings.asteroidRate < 10:
      GameSettings.asteroidRate += 1
    elif not increase and GameSettings.asteroidRate < 0:
      GameSettings.asteroidRate -= 1

  def setPlayer1Color(color):
    GameSettings.player1Color = color
  def setPlayer2Color(color):
    GameSettings.player2Color = color
  
  def toggleColoredFood():
    GameSettings.coloredFood = not GameSettings.coloredFood
  def toggleColoredFlies():
    GameSettings.coloredFlies = not GameSettings.coloredFlies
  def toggleColoredEggs():
    GameSettings.coloredEggs = not GameSettings.coloredEggs

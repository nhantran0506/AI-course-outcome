from GUI import GameGUI

game = GameGUI()

while game.running:
    game.curr_menu.display()
    game.game_loop()

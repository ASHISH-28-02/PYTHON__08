"""
Author: Ninja-06
Date: 24-10-2023
Description: This is simple rock paper scissor game which is build using python.

"""

import random

class StonePaperScissor:

    input_object_mapper = {
        1: "rock",
        2:"scissor",
        3:"paper"
    }
    
    def __init__(self):

        with open('Rules.txt', 'r') as f:
            print(f.read())

    def take_user_input(self, prompt, datatype=str):
        user_input = (input(prompt))
        if datatype == int:
            user_input = int(user_input)
        return user_input
    
    def multiplayer_mode_game_play(self):
        self.player1_name = self.take_user_input('Enter the name of first player\n>> ')
        self.player2_name = self.take_user_input('Enter the name of second player\n>> ')
        playing = True
        retake_player1_input = True
        retake_player2_input = True
        while playing:

            if retake_player1_input:
                print("\n-------------- {}'s TURN --------------".format(self.player1_name))
                self.player1_choice = self.input_object_mapper.get(self.take_user_input('\nEnter your choice\n1.Rock\n2.Scissor\n3.Paper\n>> ', int))
                if self.player1_choice is None:
                    retake_player1_input = True
                    print('invalid choice please enter your input again')
                    continue

                else:
                    print("-------------- {} PICKED {} --------------".format(self.player1_name, self.player1_choice))
                    retake_player1_input = False

            if retake_player2_input:
                print("\n-------------- {}'s TURN --------------".format(self.player2_name))
                self.player2_choice = self.input_object_mapper.get(self.take_user_input('\nEnter your choice\n1.Rock\n2.Scissor\n3.Paper\n>> ',int))
                if self.player2_choice is None:
                    retake_player2_input = True
                    print('invalid choice please please enter your input again')
            
                else:
                    print("-------------- {} PICKED {} --------------".format(self.player2_name, self.player2_choice))
                    retake_player2_input = False

            if not retake_player2_input and not retake_player2_input:
                playing = False

    def computer_mode_game_play(self):
        self.player_name = self.take_user_input('Enter your name\n>> ')
        playing = True

        while playing:

                print("\n-------------- {}'s TURN --------------".format(self.player_name))
                self.player_choice = self.input_object_mapper.get(self.take_user_input('\nEnter your choice\n1.Rock\n2.Scissor\n3.Paper\n>> ', int))

                if self.player_choice is None:
                    print('invalid choice please enter your input again')
                    continue
                else:
                    print("-------------- {} PICKED {} --------------".format(self.player_name, self.player_choice))
                    playing = False

        print("\n-------------- Computer's TURN --------------")
        self.computer_choice = self.input_object_mapper.get(random.randrange(1,4))
        print("\n-------------- Computer PICKED {} --------------".format(self.computer_choice))

    def print_results(self,p1, p2):
        print('\n{} Won!!\n'.format(p1))
        print("{} Don't give up! Better luck next time.\n".format(p2))

    def compute_results(self, player1_in, player2_in, player1_name, player2_name):
        if player1_in.lower() == 'rock' and player2_in.lower() == 'paper':
            self.print_results(player2_name, player1_name)

        elif player1_in.lower() == 'paper' and player2_in.lower() == 'rock':
            self.print_results(player1_name, player2_name)

        elif player1_in.lower() == 'paper' and player2_in.lower() == 'scissor':
            self.print_results(player2_name, player1_name)

        elif player1_in.lower() == 'scissor' and player2_in.lower() == 'paper':
            self.print_results(player1_name, player2_name)

        elif player1_in.lower() == 'rock' and player2_in.lower() == 'scissor':
            self.print_results(player1_name, player2_name)

        elif player1_in.lower() == 'scissor' and player2_in.lower() == 'rock':
            self.print_results(player2_name, player1_name)
        else:
            print("\nOops!! it's a tie between {} and {}".format(player1_name, player2_name))

    def play(self):
        running = True
        while running:
            choice = self.take_user_input('\nChoose Game Mode\n 1.Multiplayer   2.Play with computer\n>> ', int)
            if choice == 1:
                self.multiplayer_mode_game_play()
                self.compute_results(self.player1_choice, self.player2_choice, self.player1_name, self.player2_name)
            elif choice == 2:
                self.computer_mode_game_play()
                self.compute_results(self.player_choice, self.computer_choice,self.player_name, 'computer')
            else:
                print('\nInvalid Input for Game Mode. Please enter valid input')
                continue
            
            stop_game = self.take_user_input('\nDo you want to continue ? Y/N')
            if stop_game.lower() == 'n':
                running = False
                

if __name__ == '__main__':
    s = StonePaperScissor()
    s.play()
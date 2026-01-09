import art
import game_data
import random


def play_game():
    def get_info():
        info = random.choice(game_data.data)
        position = game_data.data.index(info)

        name = game_data.data[position]['name']
        followers = int(game_data.data[position]['follower_count'])
        description = game_data.data[position]['description']
        country = game_data.data[position]['country']

        info2 = random.choice(game_data.data)
        while info2 == info:
            info2 = random.choice(game_data.data)
        position2 = game_data.data.index(info2)

        name2 = game_data.data[position2]['name']
        followers2 = int(game_data.data[position2]['follower_count'])
        description2 = game_data.data[position2]['description']
        country2 = game_data.data[position2]['country']


        score = 0
        game_over = False
        while not game_over:
            print(art.logo)
            print(f'Compare A: {name}, a {description}, from {country}.')
            print(art.vs)
            print(f'Against B: {name2}, a {description2}, from {country2}.')

            guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()
            if guess == 'a' and followers > followers2:
                score += 1
                print(f'You\'re right! Current score: {score}')

                name = game_data.data[position2]['name']
                followers = int(game_data.data[position2]['follower_count'])
                description = game_data.data[position2]['description']
                country = game_data.data[position2]['country']

                info2 = random.choice(game_data.data)
                position2 = game_data.data.index(info2)
                name2 = game_data.data[position2]['name']
                followers2 = int(game_data.data[position2]['follower_count'])
                description2 = game_data.data[position2]['description']
                country2 = game_data.data[position2]['country']


            elif guess == 'a' and followers2 > followers:
                print(f'Sorry, that\'s wrong. Final score: {score}')
                if input('play again?: ') == 'y':
                    play_game()
                game_over = True



            elif guess == 'b' and followers2 > followers:
                score += 1
                print(f'You\'re right! Current score: {score}')


                name = game_data.data[position2]['name']
                followers = int(game_data.data[position2]['follower_count'])
                description = game_data.data[position2]['description']
                country = game_data.data[position2]['country']

                info2 = random.choice(game_data.data)
                position2 = game_data.data.index(info2)
                name2 = game_data.data[position2]['name']
                followers2 = int(game_data.data[position2]['follower_count'])
                description2 = game_data.data[position2]['description']
                country2 = game_data.data[position2]['country']


            elif guess == 'b' and followers > followers2:
                print(f'Sorry, that\'s wrong. Final score: {score}')
                if input('play again?: ') == 'y':
                    play_game()
                game_over = True



    get_info()



play_game()

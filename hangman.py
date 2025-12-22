import random
word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]

chosen_word = random.choice(word_list)  # we choose a random word from the list
placeholder = ""
for letter in chosen_word:
    placeholder += "_"

lives = 7
ok = 1
correct_letters = []
print(placeholder)

while ok == 1:

    display = ""
    guess = input("Guess a letter: ").lower()
    guessed_a_letter = 0

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
            guessed_a_letter = 1;
        elif letter in correct_letters:
            display += letter
        else:
            display = display + "_"
    print(display)
    if guessed_a_letter == 0:
        lives -= 1
        if lives == 6:
            print(r'''
                              +---+
                              |   |
                                  |
                                  |
                                  |
                                  |
                            =========
                            ''')
        elif lives == 5:
            print(r'''
                              +---+
                              |   |
                              O   |
                                  |
                                  |
                                  |
                            =========
                            ''')
        elif lives == 4:
            print(r'''
                              +---+
                              |   |
                              O   |
                              |   |
                                  |
                                  |
                            =========
                            ''')
        elif lives == 3:
            print(r'''
                              +---+
                              |   |
                              O   |
                             /|   |
                                  |
                                  |
                            =========''')
        elif lives == 2:
            print(r'''
                              +---+
                              |   |
                              O   |
                             /|\  |
                                  |
                                  |
                            =========
                            ''')
        elif lives == 1:
            print(r'''
                              +---+
                              |   |
                              O   |
                             /|\  |
                             /    |
                                  |
                            =========
                            ''')

    if "_" not in display:
        print("You won!")
        ok = 0
    if lives == 0:
        ok = 0
        print(r'''
                          +---+
                          |   |
                          O   |
                         /|\  |
                         / \  |
                              |
                        =========
                        ''')
        print("You lost!")
        print("The word was " + chosen_word)



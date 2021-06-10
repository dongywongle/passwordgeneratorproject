'''
WIP basic password generator, kind of improvising as i go along in rgeards to functionality and goals of the project
only just within the past few weeks feeling comfortable enough to attempt solo projects.
'''

import random

def main():

        def generateletter():
            letter = random.randint(97,126)
            return chr(letter)

        def generatespecialchar():
            char_ranges = [random.randint(32,47),
                           random.randint(123, 126),
                           random.randint(58, 64),
                           random.randint(91, 96)]
            return chr(random.choice(char_ranges))

        def combinetopw():
            pass

        print(generatespecialchar())
        print(generateletter().upper())





if __name__ == ("__main__"):
    main()
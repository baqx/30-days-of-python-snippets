import random
import emoji
emojis = [emoji.emojize(':grinning_face:'), emoji.emojize(':fire:'),
          emoji.emojize(':unicorn:')]
print(''.join(random.choices(emojis, k=100)))
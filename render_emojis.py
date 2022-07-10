from functions import *
import os
from PIL import Image
import sys
import const


# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total):
	bar_len = 80
	filled_len = int(round(bar_len * count / float(total)))

	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)

	sys.stdout.write('[%s] %s%s ... %s out of %s\r' % (bar, percents, '%', count, total))
	sys.stdout.flush()


def save_image(img: Image, filename: str):
	tokens = const.EMOJI_IMAGE_DIR_PATH + [f"{filename}.png"]
	path = os.path.join(*tokens)
	img.save(path, 'PNG')


if __name__ == '__main__':
	emojis = list(get_all_emojis())
	total = len(emojis)

	for emoji_name, emoji_value, index in emojis:
		img = create_image_from_character(emoji_value)
		save_image(img, emoji_name)

		progress(index + 1, total)

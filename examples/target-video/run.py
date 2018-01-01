import shutil
import sys
from os.path import join


if __name__ == '__main__':
    target_folder = sys.argv[1]
    path = join(target_folder, 'bunny.mp4')
    shutil.copy('bunny.mp4', path)
    print('bunny_video_path = %s' % path)

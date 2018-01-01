import shutil
import sys
from os.path import join


if __name__ == '__main__':
    target_folder = sys.argv[1]
    path = join(target_folder, 'video.mp4')
    shutil.copy('Puchica-20150620.mp4', path)
    print('a_video_path = %s' % path)

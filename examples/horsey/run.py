import mutagen
import shutil
from argparse import ArgumentParser
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from os.path import join


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder',
        metavar='FOLDER', type=make_folder)
    argument_parser.add_argument(
        '--video',
        required=True)

    args = argument_parser.parse_args()
    path = join(args.target_folder, args.video)
    shutil.copy(args.video, path)
    print('horse_video_path = %s' % path)

import argparse
import glob
from pyexiftool import exiftool


class ImageImporter:
    def __init__(self):
        print('hello')


def main():
    parser = argparse.ArgumentParser()
    for key, option in argument_options.items():
        parser.add_argument(key, **option)
    args = parser.parse_args()

    print('{} -> {}, {}, {}'.format(
        args.sources, args.targets, args.digit, args.pad))
    iimp = ImageImporter()

    iimp.sources = args.sources

    files = glob.glob(args.source + '/*')
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata_batch(files)
        for d in metadata:
            print("{:20.20} {:20.20}".format(
                d["SourceFile"], d["EXIF:DateTimeOriginal"]))
            for key, value in d.items():
                if(key == 'MakerNotes:ShutterCount'):
                    print('{} {}'.format(key, value))


argument_options = {
        'sources': {
            'type': str,
            'help': 'import source as directory',
            },
        'targets': {
            'type': str,
            'help': 'output directory for renamed file',
            },
        '--digit': {
            'type': int,
            'default': 6,
            'help': 'shutter count format on filename',
            },
        '--pad': {
            'type': str,
            'default': '0',
            'help': 'padding character of shutter count'
            },
        '--suffix': {
            'type': str,
            'help': 'filename suffix',
            },
        '--prefix': {
            'type': str,
            'help': 'filename prefix',
            }
        }

if __name__ == '__main__':
    main()

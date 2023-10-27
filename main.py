import argparse
import os

from pytube import YouTube


if __name__ == '__main__':
    video_formats = ['video', 'audio']
    project_dir = os.getcwd()
    default_path = [str(os.path.join(project_dir, 'results'))]

    parser = argparse.ArgumentParser(
        prog='YouTubeDownloader',
        description='Program downloads the video from the given link from the youtube platform.',
    )

    parser.add_argument('--url', type=str, nargs=1, dest='url', required=True)
    parser.add_argument('--format', type=str, nargs=1, dest='format', choices=video_formats, required=True)
    parser.add_argument('--dest', type=str, default=default_path, nargs=1, dest='dest_path', required=False)

    args = parser.parse_args()

    try:
        stream_query = YouTube(args.url[0]).streams

        if args.format[0] == video_formats[0]:
            stream = stream_query.get_highest_resolution()
        else:
            stream = stream_query.get_audio_only()

        stream.download(output_path=args.dest_path[0])

    except Exception as e:
        print('There was an error during command execution:\n' + str(e))


import argparse
import requests

API_URL = 'http://localhost:5000'  # Change to your deployed API URL if needed

def upload_image(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(f'{API_URL}/upload', files={'file': f})
    print(response.json())

def list_files():
    response = requests.get(f'{API_URL}/files')
    print(response.json())

def download_file(filename):
    response = requests.get(f'{API_URL}/download/{filename}')
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'{filename} downloaded.')
    else:
        print(response.json())

def delete_file(filename):
    response = requests.delete(f'{API_URL}/delete/{filename}')
    print(response.json())

parser = argparse.ArgumentParser(description='Image Processing CLI Tool')
subparsers = parser.add_subparsers(dest='command')

upload_parser = subparsers.add_parser('upload')
upload_parser.add_argument('--file', required=True)

list_parser = subparsers.add_parser('list')

download_parser = subparsers.add_parser('download')
download_parser.add_argument('--file', required=True)

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('--file', required=True)

args = parser.parse_args()

if args.command == 'upload':
    upload_image(args.file)
elif args.command == 'list':
    list_files()
elif args.command == 'download':
    download_file(args.file)
elif args.command == 'delete':
    delete_file(args.file)
else:
    parser.print_help()

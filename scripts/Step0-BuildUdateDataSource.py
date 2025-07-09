import urllib.request
import gzip
import io
import pandas as pd
import os

URL_DOWNLOAD = "https://datasets.imdbws.com/"
FILES = [
    "title.basics.tsv.gz",
    "name.basics.tsv.gz",
    "title.ratings.tsv.gz",
    "title.principals.tsv.gz",
    "title.crew.tsv.gz"
]

OUTPUT_DIR = "download"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_and_save_file(file_name):
    url = URL_DOWNLOAD + file_name
    print(f"Downloading {file_name} ...\n")

    # Download gzipped content
    response = urllib.request.urlopen(url)
    compressed_data = response.read()

    # Decompress
    uncompressed = gzip.decompress(compressed_data)

    # Save to TSV file
    tsv_file = os.path.join(OUTPUT_DIR, file_name.replace('.gz', ''))
    with open(tsv_file, 'w', encoding='utf-8') as f:
        f.write(uncompressed.decode('utf-8'))

    print(f"Saved {tsv_file}\n")

def main():
    for file in FILES:
        try:
            download_and_save_file(file)
        except Exception as e:
            print(f"Failed {file}: {e}")

# Execute  
main()

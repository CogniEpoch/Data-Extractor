import os
import zipfile

def extract_data(src_dir, dst_dir, ignore_files=None, stop_files=None):
    """
    Extract data from ZIP files in the source directory to the destination directory.
    """
    for filename in os.listdir(src_dir):
        if filename.endswith('.zip'):
            if ignore_files and filename in ignore_files:
                continue
            if stop_files and filename in stop_files:
                break
            with zipfile.ZipFile(os.path.join(src_dir, filename), 'r') as zip_ref:
                zip_ref.extractall(dst_dir)

    print('All ZIP files extracted successfully!')

# Example usage
src_dir = '/content/'
dst_dir = '/content/unzipped'
ignore_files = ['this.zip', 'that.zip']
stop_files = ['these.zip', 'those.zip']

extract_data(src_dir, dst_dir, ignore_files, stop_files)

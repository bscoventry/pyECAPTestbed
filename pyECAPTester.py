import pyeCAP
import requests
from tqdm import tqdm
import zipfile
import os
if __name__ == '__main__':
    # Download the example data into the current directory
    # This may take a while since the files are large
    # urls = ['https://gin.g-node.org/Jtrevathan/pyeCAP/raw/master/data/pnpig191126-191204-174838.zip',
    #         'https://gin.g-node.org/Jtrevathan/pyeCAP/raw/master/data/pnpig191126-191204-175046.zip']
    # for url in urls:
    #     response = requests.get(url, stream=True)
    #     total_size_in_bytes= int(response.headers.get('content-length', 0))
    #     block_size = 1024 #1 Kibibyte
    #     progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    #     with open(f'{url.split("/")[-1]}', "wb") as f:
    #         for block in response.iter_content(block_size):
    #             progress_bar.update(len(block))
    #             f.write(block)
    #     progress_bar.close()
    #     if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
    #         raise Exception("File download failed.")
            
    # print("Files Downloaded! - Unzipping.")

    # for url in urls:
    #     with zipfile.ZipFile(f'{url.split("/")[-1]}', 'r') as z:
    #         z.extractall(f'./')
    #     os.remove(f'{url.split("/")[-1]}')
    # print("Files Unzipped Successfully!")

    # path to directory containing the TDT tank
    directory = r"pnpig191126-191204-174838"
    data = pyeCAP.Ephys(directory)

    data.plot(x_lim=(0, 5))
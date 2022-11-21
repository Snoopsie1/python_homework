import urllib.request
from pathlib import Path


def download(url, to=None):
    """
    Download a remote file specified by a URL to a 
    local directory.

    :param url: str
        URL pointing to a remote file.
        
    :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """

    if to == None:
        urllib.request.urlretrieve(url,"befkbhalderstatkode.csv")
    else:
        Path(to).mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url,to+"befkbhalderstatkode.csv")
    
    print("Download succesful!")
    

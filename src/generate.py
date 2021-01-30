from num2words import num2words
import os
import gzip
from tqdm import tqdm

dir_path = os.path.dirname(os.path.realpath(__file__))


def data_path(file_name: str) -> str:
    return os.path.join(dir_path, "..", "data", file_name)


MAX_INT = int(1e6)

with gzip.open(data_path("en.txt.gz"), "wt") as fh:
    for i in tqdm(range(MAX_INT)):
        fh.write(num2words(i, lang="en") + "\n")

with gzip.open(data_path("fr.txt.gz"), "wt") as fh:
    for i in tqdm(range(MAX_INT)):
        fh.write(num2words(i, lang="fr") + "\n")

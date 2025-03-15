"""制作只含 frykit_data 里地名字符的字体"""

import os
import string
import subprocess
from itertools import chain

import pandas as pd

from frykit_data import DATA_DIRPATH

chrs = list(string.printable)
for data_source in ["amap", "tianditu"]:
    df = pd.read_csv(DATA_DIRPATH / "china" / data_source / "cn_district.csv")
    for key in ["province_name", "city_name", "district_name"]:
        chrs.extend(chain.from_iterable(df[key].to_list()))

chrs = sorted(set(chrs))
text = "".join(chrs)

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(text)

input_filepath = ""
output_filepath = "zh_font.otf"

subprocess.run(
    [
        "fonttools",
        "subset",
        str(input_filepath),
        "--text-file=text.txt",
        f"--output-file={output_filepath}",
    ]
)

os.remove("text.txt")

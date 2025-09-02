from base64 import b64decode
from pathlib import Path
from os import listdir

import orjson

from whisper_save.cipher import decrypt
from whisper_save import TARGET_DIR


def main():
    for file in listdir(TARGET_DIR):
        file_path = Path(TARGET_DIR) / file

        if file_path.is_dir():
            continue
        if not any(map(file_path.name.endswith, [".gs", ".hs", ".random", ".rms"])):
            continue
        output_path = file_path.with_name(file_path.name + ".json")

        with open(file_path, mode="r", encoding="utf-8") as f:
            ct = b64decode(f.read().strip())

        pt = decrypt(ct)
        json_expand = orjson.dumps(
            orjson.loads(pt),
            option=orjson.OPT_INDENT_2,
        )

        with open(output_path, mode="wb") as f:
            f.write(json_expand)


if __name__ == "__main__":
    main()

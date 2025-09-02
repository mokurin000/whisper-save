from base64 import b64encode
from pathlib import Path
from os import listdir

import orjson

from whisper_save.cipher import encrypt
from whisper_save import TARGET_DIR


def main():
    for file in listdir(TARGET_DIR):
        file_path = Path(TARGET_DIR) / file

        if file_path.is_dir():
            continue
        if not file_path.name.endswith(".json"):
            continue
        output_path = file_path.with_name(file_path.name.removesuffix(".json"))

        with open(file_path, mode="rb") as f:
            data = orjson.loads(f.read())

        ct: bytes = encrypt(data)
        b64 = b64encode(ct)

        with open(output_path, mode="wb") as f:
            f.write(b64)
            f.write(b"\r\n")


if __name__ == "__main__":
    main()

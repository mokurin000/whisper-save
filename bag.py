from os import SEEK_SET
import orjson


def main():
    with open("bag.json", "rb+") as f:
        content = f.read().rstrip(b",")
        raw = orjson.loads(content)

        f.seek(0, SEEK_SET)
        f.truncate(0)

        if isinstance(raw, str):
            obj: dict = orjson.loads(raw)
        else:
            obj: str = orjson.dumps(raw).decode()

        f.write(orjson.dumps(obj, option=orjson.OPT_INDENT_2))


if __name__ == "__main__":
    main()

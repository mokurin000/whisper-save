import orjson
from Crypto.Cipher import DES
from Crypto.Cipher._mode_cbc import CbcMode
from Crypto.Util.Padding import unpad, pad


def cipher() -> CbcMode:
    key = b"Sikanuan"
    iv = b"921f492a"
    return DES.new(key, mode=DES.MODE_CBC, iv=iv)


def decrypt(ct: bytes) -> bytes:
    pt_pad = cipher().decrypt(ct)
    return unpad(pt_pad, 8)


def encrypt(data: dict) -> bytes:
    pt = orjson.dumps(data)
    pt_pad = pad(pt, 8)
    return cipher().encrypt(pt_pad)

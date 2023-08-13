import datetime

import jwt

payload = {
    "my_name": "Vova",
    "password": "htgdhdhdthtdhfhghd434gfd",
}


def coding_jwt(payload: dict) -> str:
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    payload['iat'] = datetime.datetime.utcnow()

    encode_jwt = jwt.encode(
        payload=payload,
        key="secret",
        algorithm="HS256"
    )
    return encode_jwt


def decoding_jwt(token_jwt: str) -> dict:
    try:
        decoded = jwt.decode(
            token_jwt,
            key="secret",
            algorithms=['HS256'])
        return decoded
    except:
        return {}


print(coding_jwt(payload))
print(decoding_jwt(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJteV9uYW1lIjoiVm92YSIsInBhc3N3b3JkIjoiaHRnZGhkaGR0aHRkaGZoZ2hkNDM0Z2ZkIiwiZXhwIjoxNjkxOTI5MDc3LCJpYXQiOjE2OTE5MjgxNzd9.X9y64XTeOWgKAv9J5MdX9J40_VYuqQPMEXdOr49ZjQI"))

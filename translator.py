import asyncio
from googletrans import Translator

LANGUAGE = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "la": "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh-cn": "Chinese (Simplified)",   # prefer zh-cn / zh-tw with googletrans
    "es": "Spanish"
}

def pick_dest_code():
    while True:
        user_code = input(
            "Please input desired language code. To see the language code list enter 'options' \n"
        ).strip().lower()

        if user_code == "options":
            print("Code : Language")
            for k, v in LANGUAGE.items():
                print(f"{k} => {v}")
            print()
            continue

        if user_code in LANGUAGE:
            print(f"You have selected {LANGUAGE[user_code]}")
            return user_code

        print("It's not a valid language code!")

async def main():
    dest = pick_dest_code()

    # Using translate.googleapis.com reduces token issues
    async with Translator(service_urls=['translate.googleapis.com']) as translator:
        while True:
            string = input(
                "\nWrite the text you want to translate: \nTo exit the program write 'close'\n"
            )

            if string.strip().lower() == "close":
                print("\nHave a nice Day!")
                break

            try:
                result = await translator.translate(string, dest=dest)
            except Exception as e:
                print(f"Translation failed: {e}")
                continue

            print(f"\n{LANGUAGE[dest]} translation: {result.text}")
            if getattr(result, "pronunciation", None):
                print(f"Pronunciation : {result.pronunciation}")

            src_name = LANGUAGE.get(result.src, result.src)
            print(f"Translated from : {src_name}")

if __name__ == "__main__":
    asyncio.run(main())

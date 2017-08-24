bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'ドウイタシマシテ',
    'さようなら': 'サヨウナラ',
    'かわいいね': 'アリガトウ',
    }

while True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break

    if not response:
        response = '何ヲ言ッテイルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
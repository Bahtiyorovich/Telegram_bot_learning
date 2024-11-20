import requests
token = "7825689825:AAFnsCEtXKrID2SlXtDmR7RrHVygHJRMf40"
method = 'sendMessage'
# method = 'sendDice'
response = requests.post(
        url = f'https://api.telegram.org/bot{token}/{method}',
        # data = {'chat_id': 5226898995, 'text':'Hello User'}
        # data = {'chat_id': 5226898995, 'emoji': '🏀'}
        data = {'chat_id': 5226898995, 'text': 'https://youtu.be/pqAotH_HYXY?si=X1ZINNzQ5LupbxX6'}
    ).json()

print(response)

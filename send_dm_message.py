#DM送信処理 引き数のIDリストから各IDにDMを送信
def send_message(userIDlist, twitter, json):
    msg_text = 'リスカが止まらないこと山の如く'
    
    pollingTime = 70
    headers = {"content-type": "application/json"}
    url = "https://api.twitter.com/1.1/direct_messages/events/new.json"
    for userID in userIDlist:
        param = {"event": {"type": "message_create", "message_create": {"userID": {"recipient_id": userID}, "message_data": {"text": msg_text}}}}
        twitter.post(url, headers = headers, data = json.dumps(param))
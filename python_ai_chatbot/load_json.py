import json

def json_to_messages(file_path):
    """
    JSONファイルを読み込み、ベクトル化に必要な情報を抽出してリストとして返す。
    
    Args:
        file_path (str): 読み込むJSONファイルのパス

    Returns:
        list: 各メッセージのテキストとタイムスタンプを含む辞書のリスト
    """
    with open(file_path, 'r') as f:
        json_data = json.load(f)
        messages = [{"text": msg["text"], "timestamp": msg["ts"]} for msg in json_data]

        return messages

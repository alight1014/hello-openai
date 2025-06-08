# -*- coding: utf-8 -*-
import argparse
import openai
from openai import OpenAI

# 配置設定
CONFIG = {
    "model": "gpt-4o-search-preview",
    "web_search_options": {
        "search_context_size": "high",
        "user_location": {
            "type": "approximate",
            "approximate": {
                "country": "TW",
                "city": "Taipei",
                "region": "Taiwan",
            }
        },
    },
    "api_key": "your_api_key"
}

def chat_with_search(content, config=None):
    """
    使用 OpenAI 的搜尋功能進行聊天

    Args:
        content (str): 用戶的訊息內容
        config (dict, optional): 配置設定，如果沒有提供則使用預設配置

    Returns:
        str: AI 的回應內容
    """
    if config is None:
        config = CONFIG

    client = OpenAI(api_key=config["api_key"])

    response = client.chat.completions.create(
        model=config["model"],
        web_search_options=config["web_search_options"],
        messages=[
            {"role": "user", "content": content}
        ]
    )

    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="使用 OpenAI 搜尋功能進行聊天")
    parser.add_argument("-q", "--query", type=str, required=True, help="要詢問的問題或內容")
    parser.add_argument("-m", "--model", type=str, help="指定使用的模型")

    args = parser.parse_args()

    # 如果有指定模型，更新配置
    config = CONFIG.copy()
    if args.model:
        config["model"] = args.model

    result = chat_with_search(args.query, config)
    print(result)

if __name__ == "__main__":
    main()



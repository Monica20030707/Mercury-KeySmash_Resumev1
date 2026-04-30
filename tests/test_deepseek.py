import anthropic
import os
import sys

# Try to find the API key in several common environment variables
api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("DEEP_SEEK_API_KEY")
base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.deepseek.com/anthropic")

if not api_key:
    print("Error: No API key found!")
    print("Please run: export ANTHROPIC_API_KEY='your-sk-key-here'")
    sys.exit(1)

print(f"Using Base URL: {base_url}")
print(f"Key starts with: {api_key[:6]}... (length: {len(api_key)})")

client = anthropic.Anthropic(
    base_url=base_url,
    api_key=api_key
)

try:
    message = client.messages.create(
        model="deepseek-chat",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": "Hi, are you DeepSeek? Please reply with a short sentence."
            }
        ]
    )
    print("\n--- Response ---")
    print(message.content[0].text)
    print("----------------\n")
except Exception as e:
    print(f"\nAPI Error: {e}")
    if "401" in str(e):
        print("\nPossible reasons for 401:")
        print("1. Your DeepSeek key is typed incorrectly.")
        print("2. You are using an Anthropic key with a DeepSeek URL (or vice-versa).")
        print("3. Your DeepSeek account has no credits/balance.")
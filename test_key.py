import google.genai as genai
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
API_CONFIG_PATH = BASE_DIR / "config" / "api_keys.json"

def _get_api_key() -> str:
    with open(API_CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["gemini_api_key"]

# Проверяем, можем ли мы получить ключ
try:
    api_key = _get_api_key()
    print(f"[OK] Ключ загружен: {api_key[:10]}...")
    
    # Создаем клиент (как в main.py)
    client = genai.Client(api_key=api_key, http_options={"api_version": "v1beta"})
    
    # Попробуем простой запрос
    model = client.models.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content("Привет!")
    print(f"[OK] Ответ от Gemini: {response.text}")
    print("[OK] Ключ работает!")
    
except Exception as e:
    print(f"[ERROR] Ошибка: {e}")
    import traceback
    print(f"[DETAILS] Подробности ошибки:\n{traceback.format_exc()}")


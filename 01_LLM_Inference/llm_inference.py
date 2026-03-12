"""
LLM Interface Layer

Provides a reusable client for interacting with LLM providers.
"""

import os
import json
from typing import List, Dict, Any

from openai import OpenAI

class LLMCLient:
    def __init__(
            self,
            model: str = "gpt-4o-mini",
            temperature: float = 0.2,
            max_tokens: int = 500,
            api_key: str = None
    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

        api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

    def chat(self, messages: List[Dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content
    
    def send_prompt(self, system_prompt:str, user_prompt:str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return self.chat(messages)
    
    def structured_chat(
            self,
            system_prompt:str,
            user_prompt:str
    ) -> Dict[str, Any]:
        messages = [
            {
                "role": "system",
                "content": system_prompt + "\n Return output as valid JSON."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
        response_text = self.chat(messages)
        return self.parse_json(response_text)
    
    def parse_json(self, text:str) -> Dict[str, Any]:
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON", "raw_output": text}
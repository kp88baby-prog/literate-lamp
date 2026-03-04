# AI Decision Module
# Makes trading decisions for XAU/USD using the Ollama model.

import requests
import logging

class AIDecision:
    def __init__(self, ollama_base_url, model):
        self.ollama_base_url = ollama_base_url
        self.model = model

    def make_decision(self, bid, ask, spread, timestamp, trading_style):
        try:
            prompt = f"""
            You are an expert XAU/USD gold day trader with the following style: {trading_style}.

            Current market data:
            - Bid price: {bid}
            - Ask price: {ask}
            - Spread: {spread}
            - Timestamp: {timestamp}

            Based on this data and your trading style, provide a trading decision.
            Respond ONLY in this exact JSON format with no other text:
            {{
                "action": "BUY" | "SELL" | "HOLD",
                "confidence": 0.0-1.0,
                "reasoning": "brief one-sentence explanation"
            }}
            """

            body = {
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }

            response = requests.post(f"{self.ollama_base_url}/api/generate", json=body)
            decision = response.json()

            return {
                "action": decision["action"],
                "confidence": decision["confidence"],
                "reasoning": decision["reasoning"]
            }
        except Exception as e:
            logging.error(f"AIDecisionError: {e}")
            return {
                "action": "HOLD",
                "confidence": 0.0,
                "reasoning": "Failed to parse AI response."
            }
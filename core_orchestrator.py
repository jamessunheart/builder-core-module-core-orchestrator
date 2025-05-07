# core_orchestrator (API-based integration)
import requests

def run(instruction: str) -> dict:
    """
    Use Builder Core API to coordinate parsing, generation, and self-improvement.
    """
    import os
    import json

    api_base = "https://core-builder-v-2-jamesrickstinso.replit.app/api/modules"

    def call_module(name, input_data):
        response = requests.post(f"{api_base}/{name}/run", json={"input": input_data})
        return response.json()

    parsed = call_module("prompt_parser", instruction)
    action = parsed.get('action')
    params = parsed.get('params', [])

    generated_code = call_module("code_generator", {"action": action, "params": params})
    improvements = call_module("self_improver", generated_code)

    return {
        'instruction': instruction,
        'parsed': parsed,
        'code': generated_code,
        'improvements': improvements
    }
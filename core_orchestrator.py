# Optimized core_orchestrator
import requests

def run(instruction: str) -> dict:
    """
    Dynamically orchestrate parsing, generation, and improvement via internal API calls.
    """
    import json
    api_base = "https://core-builder-v-2-jamesrickstinso.replit.app/api/modules"

    def call_module(module, payload):
        try:
            response = requests.post(f"{api_base}/{module}/run", json={"input": payload})
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    # Step 1: Parse
    parsed = call_module("prompt_parser", instruction)
    action = parsed.get("action")
    params = parsed.get("params", [])

    # Step 2: Generate
    gen_input = {"action": action, "params": params}
    generated = call_module("code_generator", gen_input)

    # Step 3: Improve
    improvements = call_module("self_improver", generated)

    return {
        "instruction": instruction,
        "parsed": parsed,
        "generated": generated,
        "improvements": improvements
    }
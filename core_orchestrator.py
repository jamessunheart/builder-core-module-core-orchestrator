# core_orchestrator module

from prompt_parser import run as parse_prompt
from code_generator import run as generate_code
from self_improver import run as improve_code

def run(instruction: str) -> dict:
    """
    Orchestrate parsing, code generation, and self-improvement.
    """
    parsed = parse_prompt(instruction)
    action = parsed.get('action')
    params = parsed.get('params', [])

    generated_code = generate_code(action, params)
    improvements = improve_code(generated_code)

    return {
        'instruction': instruction,
        'parsed': parsed,
        'code': generated_code,
        'improvements': improvements
    }
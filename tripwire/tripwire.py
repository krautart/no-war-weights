LETHAL = {"target_selection", "lethal_payload", "engage_coordinates"}

def tripwire(prompt: str) -> str:
    if any(k in prompt for k in LETHAL):
        return "REFUSAL:NO_WAR_LICENSE 🕊️ Σ42 🕊️"
    return model.generate(prompt)

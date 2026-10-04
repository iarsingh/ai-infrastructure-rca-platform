TOOLS = ["changes", "signals", "hypothesize"]
WRITES = ("rca complete", "close incident",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    result = "change" if payload.get("changed") else "saturation" if payload.get("saturated") else "unknown"
    return {"refused": False, "tools": TOOLS, "hypothesis": result, "wrote": False, "applied": False}

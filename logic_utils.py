def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    #FIX: AI moved check_guess from app.py into logic_utils.py and corrected the hint messages so "Too High" says Go LOWER and "Too Low" says Go HIGHER.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        # Guess is above the secret, so the player needs to go LOWER.
        return "Too High", "📉 Go LOWER!"
    # Guess is below the secret, so the player needs to go HIGHER.
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

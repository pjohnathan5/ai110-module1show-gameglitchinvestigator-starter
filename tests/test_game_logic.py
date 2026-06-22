from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_lower():
    # The bug: when guess > secret the message must say LOWER, not HIGHER.
    _, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected 'LOWER' in message for high guess, got: {message!r}"
    assert "HIGHER" not in message, f"Message for high guess must not say HIGHER, got: {message!r}"

def test_too_low_message_says_higher():
    # Mirror of the bug: when guess < secret the message must say HIGHER, not LOWER.
    _, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected 'HIGHER' in message for low guess, got: {message!r}"
    assert "LOWER" not in message, f"Message for low guess must not say LOWER, got: {message!r}"

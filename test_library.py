import library


def test_short_password():
    assert not library.passcode_checker("abc123")


def test_missing_lowercase():
    assert not library.passcode_checker("ABC123456")


def test_missing_uppercase():
    assert not library.passcode_checker("abc123456")


def test_missing_special_character():
    assert not library.passcode_checker("Abc123456")


def test_contains_space():
    assert not library.passcode_checker("Abc 123456")


def test_contains_non_ascii():
    assert not library.passcode_checker("Abc1234ß56")

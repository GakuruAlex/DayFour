from head_or_tail import heads_or_tails

def test_heads_or_tails_with_one():
    assert heads_or_tails(1) == "Heads"
def test_heads_or_tails_with_zero():
    assert heads_or_tails(0) == "Tails"
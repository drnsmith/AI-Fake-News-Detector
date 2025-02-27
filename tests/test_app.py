from app.fact_checker import check_fact

def test_fact_checker():
    text = "The earth is flat."
    credibility = check_fact(text)
    assert isinstance(credibility, str)
    assert credibility in ["factual", "misleading", "satire"]

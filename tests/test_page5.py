# tests/test_page5.py
def test_page5_advanced_features(page):
    page.goto("http://localhost:8501/page5")

    # Check the title
    assert page.title() == "page5"
    # Check for the presence of the header
    assert page.inner_text("h1") == "Page 5 - Advanced Features"

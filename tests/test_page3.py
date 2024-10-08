# tests/test_page3.py
def test_page3_multimedia(page):
    page.goto("http://localhost:8501/page3")

    # Check the title
    assert page.title() == "page3"
    # Check for the presence of the header
    assert page.inner_text("h1") == "Page 3 - Multimedia and Layouts"

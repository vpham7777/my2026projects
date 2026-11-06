def test_successful_login(page, base_url):
  # 1. Navigate to the page
  page.goto(base_url)

  # 2. Grab inputs via distinct locators (ID, Placeholder, Test ID)
  page.locator("#username").fill("admin")
  page.get_by_placeholder("Enter password").fill("admin123")

  # 3. Perform the click event
  page.locator('[data-testid="submit-login"]').click()

  # 4. Verify text content updates post-navigation
  assert page.locator("h1").inner_text() == "Welcome, Admin!"
  assert page.locator("#status").inner_text() == "Success"


def test_failed_login(page, base_url):
  page.goto(base_url)

  # Explicitly locating elements via their connected labels
  page.get_by_label("Username:").fill("wrong_user")
  page.get_by_label("Password:").fill("wrong_pass")
  page.get_by_role("button", name="Log In").click()

  assert page.locator("h1").inner_text() == "Invalid Credentials"
  assert page.locator("#status").inner_text() == "Failed"

def test_product_table_elements_exist(page, base_url):
  page.goto(base_url)

  # Practice targeting table structural nodes
  table_rows = page.locator("#product-table tbody tr")
  assert table_rows.count() == 3

  # Target specific product row metadata
  first_row_title = page.locator('[data-id="101"] .product-name')
  assert first_row_title.inner_text() == "Developer Coffee Mug"


def test_cart_quantity_interaction(page, base_url):
  page.goto(base_url)

  # Select the input field inside the row grid and alter its state
  qty_input = page.locator('[data-testid="qty-input-102"]')
  qty_input.fill("5")

  # Register a listener for the native browser alert event triggered by the button click
  page.on(
      "dialog", lambda dialog: [assert_dialog(dialog), dialog.accept()]
  )

  def assert_dialog(dialog):
    assert "Added 5 item(s) to your cart!" in dialog.message

  # Trigger click
  page.locator('[data-testid="add-btn-102"]').click()

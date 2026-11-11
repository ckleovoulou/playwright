# Checkout — test plan

**Page(s):** `/inventory.html` → `/cart.html` → `/checkout-step-one.html` → `/checkout-step-two.html` → `/checkout-complete.html`
**Preconditions:** logged in as `standard_user`

## Locators found
| Element | Locator |
|---|---|
| Add to cart (per product) | `get_by_test_id("add-to-cart-<product-slug>")` |
| Cart link | `.shopping_cart_link` |
| Cart badge | `.shopping_cart_badge` |
| Checkout button | `get_by_role("button", name="Checkout")` |
| First / Last name, Postal code | `get_by_placeholder("First Name" / "Last Name" / "Zip/Postal Code")` |
| Continue button | `get_by_role("button", name="Continue")` |
| Error message | `get_by_test_id("error")` |
| Item total | `.summary_subtotal_label` |
| Finish button | `get_by_role("button", name="Finish")` |
| Confirmation header | `.complete-header` |

## Scenarios

### 1. User can buy a product end to end  `smoke`
**Steps**
1. Add "Sauce Labs Backpack" to the cart and open the cart.
2. Click Checkout, fill first name, last name and postal code, click Continue.
3. Click Finish.

**Expected**
- Overview shows `Item total: $29.99`.
- Confirmation page shows `Thank you for your order!`.
- Cart badge is gone.

### 2. Cart shows exactly the products that were added  `regression`
**Steps**
1. Add "Sauce Labs Backpack" and "Sauce Labs Bolt T-Shirt", open the cart.

**Expected**
- Cart lists exactly those two products, in that order.

### 3. Removing a product in the cart leaves the others  `regression`
**Steps**
1. Add "Sauce Labs Backpack" and "Sauce Labs Bike Light", open the cart.
2. Remove "Sauce Labs Backpack".

**Expected**
- Only "Sauce Labs Bike Light" remains; badge shows `1`.

### 4. Item total adds up the prices of all products  `regression`
**Steps**
1. Add Backpack ($29.99) and Bike Light ($9.99), go to checkout overview.

**Expected**
- `Item total: $39.98`.

### 5. Checkout requires a postal code  `regression`
**Steps**
1. Add a product, start checkout, fill first and last name only, click Continue.

**Expected**
- Error `Error: Postal Code is required`; user stays on step one.

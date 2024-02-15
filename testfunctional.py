from functional import Login, Account, address, addingproduct, cart, logout, productsearch


def test_all_functions():
    Login.test_successful_login()
    productsearch.test_product_search()
    addingproduct.test_add_cart()
    cart.test_cart()
    Account.test_account()
    logout.test_logout()


Login.test_successful_login()
productsearch.test_product_search()
addingproduct.test_add_cart()
cart.test_cart()
Account.test_account()
logout.test_logout()

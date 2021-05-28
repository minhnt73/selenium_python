class ProductDetailLocator:
    product_img = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img'
    view_lager_icon = '//span[@class = "span_link no-print"]'
    product_name = '//span[@class = "child"]'
    close_icon = '//a[@title = "Close"]'
    quantity_field = '//input[@id = "quantity_wanted"]'
    add_to_cart_button = '//*[@id="add_to_cart"]/button/span'
    popup_messg = '//p[@class = "fancybox-error"]'
    popup_messg_close = '//a[@title = "Close"]'
    mess_confirm = "//div[@class = 'layer_cart_product col-xs-12 col-md-6']//h2"
    close_icon_popup = '//span[@title = "Close window"]'
    cart_btn = '//div[@class = "shopping_cart"]//a[@title = "View my shopping cart"]'
    product_in_cart = '//*[@id="product_1_1_0_0"]/td[2]/p'
    # ------------------------------BAI TAP 12_____________________________________

    share_twitter_btn = '//button[@class= "btn btn-default btn-twitter"]'
    twitter_btn_page = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div[3]/div/div/span/span'
    id_twitter = '//input[@name = "session[username_or_email]"]'
    pw_twitter = "//input[@name = 'session[password]']"
    login_button = "//span[contains(text(), 'Log in')]"
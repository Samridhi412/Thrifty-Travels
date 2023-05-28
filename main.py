from booking.booking import Booking
try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency=input("Type in your currency value"))
        bot.select_place_to_go(input("Where you want to go?"))
        bot.select_dates(check_in_date=input("What is the check in date in format(YYYY-MM-DD)?"),
                         check_out_date=input("What is the check out date in format(YYYY-MM-DD)?"))
        bot.select_adults(int(input("How many people?")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh() # A workaround to let our bot grab data
        bot.report_results()
except Exception as e:
    if "in PATH" in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Driver \n'
            'Windows: \n'
            '  set PATh=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
           )
    else:
        raise
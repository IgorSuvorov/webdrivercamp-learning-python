#!/usr/bin/python3
quote = "There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch."

quote = quote.split('--')[1].split('obvious')[0].replace('and ', '').strip() + ' unless'

print(quote)

def stock_availability(some_list, command, *args):

    if command == "delivery":
        for el in args:
            some_list.append(el)
    elif command == "sell":
        if args:
            for el in args:
                while el in some_list:
                    some_list.pop(some_list.index(el))

                if str(el).isdigit():
                    for _ in range(el):
                        if some_list:
                            some_list.pop(0)
    else:
        some_list.pop(0)
    return some_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

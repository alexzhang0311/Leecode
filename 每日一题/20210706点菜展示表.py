orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]

def displayTable(orders):
    foods = sorted(list(set([i[2] for i in orders])))
    tables = sorted(list(set([int(i[1]) for i in orders])))
    header = ["Table"] + foods
    detail_info = ["0" for i in range(len(header))]
    outcome=[header]
    table_orders=[]
    for table in tables:
        for order in orders:
            if order[1] == str(table):
                table_orders.append(order)
        detail_info[0]=str(table)
        for key,food in enumerate(foods):
            flag = 0
            for table_order in table_orders:
                if table_order[2] == food:
                    flag += 1
            detail_info[key + 1] = str(flag)
        outcome.append(detail_info)
        table_orders=[]
        detail_info = ["0" for i in range(len(header))]
    return outcome

print(displayTable(orders))





# a = [1,2,3,4]
# b = [5,6,7,8]
# c= []
# c.append(a)
# c.append(b)
# print(c)

import prettytable as pt

def show_ticket(row_num):
    tp=pt.PrettyTable()
    tp.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
        tp.add_row(lst)
    print(tp)
def order_ticlet(row_num,row,colum):
    tb=pt.PrettyTable()
    
if __name__ == "__main__":
    row_num=13
    show_ticket(row_num)
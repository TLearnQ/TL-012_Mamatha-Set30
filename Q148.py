def classify(rec):
    cost=rec["cost"]
    sales=rec["sales"]
    profit=cost/sales
    if cost<sales and profit<sales:
        return "Low Marigin"
    elif cost>sales and profit>sales:
        return "Peak"
    elif cost<=sales and profit>=sales:
        return "healthy"
    else:
        return "loss"
record={"cost":10000,"sales":20000}
print(classify(record))    
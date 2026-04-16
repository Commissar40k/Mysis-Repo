import csv
rows=[]
filesMerge=["data\daily_sales_data_0.csv", "data\daily_sales_data_1.csv", "data\daily_sales_data_2.csv"]
for i in filesMerge:
    with open(i, newline="") as csvfile:
        reader=csv.reader(csvfile, delimiter=",", quotechar=" ")
        for row in reader:
            if row[0]=="pink morsel":
                #print(str(float(row[1][1:len(row[1])])*float(row[2]))+ ", " +row[3]+ ", " +row[4])
                rows.append([str(float(row[1][1:len(row[1])])*float(row[2])), row[3], row[4]])
with open('data\daily_sales_data_MERGED.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Sales"]+["Date"]+["Region"])
    for i in rows:
        writer.writerow(i)

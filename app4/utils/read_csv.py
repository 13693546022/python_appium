import csv

class CSVUtil():
    def __init__(self,filePath):
        self.filePath = filePath

    def list_data(self):
        # 读取CSV文件
        values_rows=[]
        with open(self.filePath,"r",encoding="utf-8") as f:
            f_csv=csv.reader(f)
            next(f_csv)# 如果从第2行行开始读取数据，则加入该行代码
            for r in f_csv:
                values_rows.append(r)
        return values_rows

if __name__=="__main__":
    fp="./test_data3.csv"
    util=CSVUtil(fp)
    print(util.list_data())
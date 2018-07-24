import time
from multiprocessing import Pool
from spider import parse_link
from indexspider import parse_index

# 多进程
def main(data):
    url = data['url']
    print(url)
    mongo_table = data['name']
    # 因为有的职位是以'.'开头的，比如.Net,数据表名不能以.开头
    if mongo_table[0] == '.':
        mongo_table = mongo_table[1:]
    # 我们把之前抓取职位所有招聘信息的程序整理为parse_link()函数
    # 这个函数接收职位url，页码，和数据库表名为参数
    parse_link(url, mongo_table)


if __name__ == '__main__':
    t1 = time.time()

    pool = Pool(processes=4)

    datas = (data for data in parse_index())
    pool.map(main, datas)
    pool.close()
    pool.join()

    print(time.time() - t1)
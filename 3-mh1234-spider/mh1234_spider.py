from gi_spider import *
import os.path

def main():
    print('\n-- mh1234_spider v0.1 --\n')

    mh_id = input('漫画id：')
    path = os.path.normcase(input('储存路径：'))
    
    comic_url = 'https://www.mh1234.com/comic/' + mh_id + '/'

    mh1234 = gi_spider()
    content = mh1234.get_html(comic_url)
    book_conent = mh1234.find_it(content, 'ul', 'id', 'chapter-list-1')
    book_list = re.findall(r'<a href="/comic/.*?/(.*?).html">', book_conent)
    book_name_list = re.findall(r'<a.*?>(.*?)<i></i></a>', book_conent)

    for i in range(len(book_list)):
        j = 0
        
        os.mkdir(path + book_name_list[i])
        print('正在下载：' + book_name_list[i] + '...')

        while j >= 0:
            try:
                print(str(j+1) ,end='/')
                page_url = 'https://img.wszwhg.net/image/view/?chapter_id=' + book_list[i] + '&index=' + str(j)
                mh1234.copy_file(page_url, path + book_name_list[i] + '/' + str(j+1)+'.jpg')
            
            # 到终点的索引会返回404
            except Exception as result:
                print('错误')
                print(result)
                break
            
            j += 1
        
    print('全部下载完毕')

if __name__ == '__main__':
    main()
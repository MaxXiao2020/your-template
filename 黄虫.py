import re,requests,os

from lxml import etree

def download_pics (url):

    response = requests.get (url,headers = headers1)

    base_link = etree.HTML (response.text).xpath ('//div[@class="main-image"]//img/@src')[0][0:-6] #提取首张图片的下载地址

    page_info = etree.HTML (response.text).xpath ('//div[@class="pagenavi"]//span/text()')    #提取当前系列图片的页码信息列表

    max_page = int(page_info[-2])   #提取图片的最大页码

    for i in range(1,max_page+1):

        page= str (i).zfill(2)

        download_link = base_link+ str(page)+'.jpg'

        headers = {'Referer':url+'{}'.format (i),'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

        response = requests.get (download_link,headers = headers)

        pic_name = download_link[-9:-4]

        print ('目前第{}套妹子,共{}张  正在下载第{} 张图片......'.format (list_cnt,max_page,i))

        with open (save_path +'\\'+pic_name+'.jpg','wb') as f:

            f.write (response.content)

def get_list (url):  

    global list_cnt,save_path

    list_cnt = 1

    reponse = requests.get (url,headers = headers1)

    regax = '\d\d\w\:.+\>'

    list_pool = re.findall (regax,reponse.text)

    for li in list_pool:

        url = li.split(' ')[2].split('"')[1]

        save_path = '美女套图\\EP'+str(list_cnt).zfill(4)

        if not os.path.exists(save_path):   #新建一个存放图片的目录

            os.mkdir(save_path)

        download_pics (url)

        list_cnt += 1

        

def main ():

    if not os.path.exists('美女套图'):   #新建一个存放图片的目录

        os.mkdir('美女套图')

    input ('本程序将采集全网套图，采集时间会因站点图片增加而延长，确定采集请按回车键')

    os.startfile ('美女套图')

    get_list (url)

if __name__ == '__main__':

    url = 'https://www.mzitu.com/all/'

    headers1 = {'user-agent': 'Mozilla/5.0'}

    main ()

# 파이썬 크롤링 기초
#  urllib 사용법 기본 및 기본 스크랩핑

import urllib.request  as req

# 파일 URL
img_url = 'https://upload.wikimedia.org/wikipedia/en/4/45/Birdy_%28Birdy_album%29.png'
html_url = 'http://www.google.com'

save_path1 = 'C:/python_crawl/crawl_file/test.jpg'
save_path2 = 'C:/python_crawl/crawl_file/index.html'

try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('DownLoad Failled')
    print(e)
else:
    print(header1.get_content_type)
    print(header2.get_content_type)

    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    # 성공
    print('Download Succed!')
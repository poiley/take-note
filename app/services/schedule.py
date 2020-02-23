import requests, json, time
from bs4 import BeautifulSoup

prefix      = 'https://'
site        = 'schedules.wsu.edu'
campus      = 'Pullman'
year        = 2020
quarter     = 1

base_url    = '{}{}/List/{}/{}{}'.format(prefix, site  , campus, year, quarter)


def _get_days(s):
    return ''.join([i for i in s if i.isalpha()])

def _get_time(s):
    return ''.join([i for i in s if not i.isalpha()]).replace(',', '').split('-')

def get_urls(initial_url):
    r           = requests.get(initial_url, requests.utils.default_headers())
    soup        = BeautifulSoup(r.content, 'html.parser')
    table       = soup.find('ul', {'class': 'prefixList'})

    urls        = []
    for url in table.findAll('a'):
        urls.append((url.string.strip(), '{}/{}'.format(initial_url, '/'.join(url.attrs['href'].split('/')[4:]))))
    
    return urls


def get_classes_given_urls(urls):
    classes = { 'written' : 0, 'classes' : [] }

    for subdir in urls:
        r       = requests.get(subdir[1], requests.utils.default_headers())
        soup    = BeautifulSoup(r.content, 'html.parser')
        table   = soup.find('tbody')

        d          = {}
        department = ""
        course_num = ""
        title      = ""
        for row in table.findAll('tr'):
            if row.attrs['class'][0] == 'course_title':
                course_title_split  = [x for x in row.find('td').string.split(' ') if x]
                department          = course_title_split[0]
                course_num          = int(course_title_split[1])
                title               = ' '.join(course_title_split[2:])
            elif 'section' in row.attrs['class']:
                try:
                    d['section']        = row.find('td', {'headers' : 'sched_sec'}).find('a').string
                    d['professor']      = row.find('td', {'headers' : 'sched_instructor'}).string
                    d['days']           = _get_days(row.find('td', {'headers' : 'sched_days'}).string)
                    d['start'], d['end']= _get_time(row.find('td', {'headers' : 'sched_days'}).string)
                    d['hall']           = row.find('td', {'headers' : 'sched_loc'}).string
                except:
                    continue
            
            d['dept']               = department
            d['course_num']         = course_num
            d['title']              = title

            classes['classes'].append(d)
    
    classes['written'] = int(time.time())
    
    return classes


def to_json():
    urls = get_urls(base_url)
    classes = get_classes_given_urls(urls)

    with open('static/data/wsu_classes.json', 'r+') as f:
        json.dump(classes, f)

    return classes


def get_classes(): 
    with open('static/data/wsu_classes.json', 'r+') as f:
        data = json.load(f)

    if 'written' in data.keys() and data['written'] + 2592000 < time.time(): # 30 days in seconds 
        return to_json()
    else:   
        return data
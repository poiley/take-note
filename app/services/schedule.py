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
    r = ''.join([i for i in s if not i.isalpha()]).replace(',', '').split('-')
    if r == ['']:
        return 'Online', 'Online'
    return r

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
        r          = requests.get(subdir[1], requests.utils.default_headers())
        soup       = BeautifulSoup(r.content, 'html.parser')
        table      = soup.find('tbody')

        section    = ""
        professor  = ""
        course_num = ""
        title      = ""
        for row in table.findAll('tr'):
            lecture = { 'dept': subdir[0] }

            if row.attrs['class'][0] == 'course_title':
                course_title_split      = [x for x in row.find('td').string.split(' ') if x]

                course_num  = int(course_title_split[1])
                title       = ' '.join(course_title_split[2:])
            elif 'section' in row.attrs['class']:
                section_raw              = row.find('td', {'headers' : 'sched_sec'})
                if section_raw is None:
                    lecture['section']   = section
                else:
                    lecture['section']   = section_raw.find('a').string
                    section              = lecture['section']

                if 'lab' in section.lower():
                    continue

                professor_raw            = row.find('td', {'headers' : 'sched_instructor'})
                if professor_raw is None:
                    lecture['professor'] = professor
                else:
                    lecture['professor'] = professor_raw.string
                    professor            = lecture['professor']
                    if lecture['professor'] == '':
                        lecture['professor'] = 'No Professor'

                lecture['days'] = _get_days(row.find('td', {'headers' : 'sched_days'}).string)
                lecture['start'], lecture['end'] = _get_time(row.find('td', {'headers' : 'sched_days'}).string)
                lecture['hall'] = row.find('td', {'headers' : 'sched_loc'}).string
                
                lecture['course_num']   = course_num 
                lecture['title']        = title

                print('Writing Lecture to data structure -- {} {} {}, starts at {}, taught by {}'.format(lecture['dept'], lecture['course_num'], lecture['title'], lecture['start'], lecture['professor']))
                classes['classes'].append(lecture)
    
    classes['written'] = int(time.time())
    
    return classes


def to_json():
    urls = get_urls(base_url)
    classes = get_classes_given_urls(urls)

    print('Writing Lecture data structure to file...')
    with open('static/data/wsu_classes.json', 'w', encoding='utf-8') as f:
        json.dump(classes, f, ensure_ascii=False, indent=4)
    print('Wrote to file.')
    
    return classes


def get_classes(): 
    with open('static/data/wsu_classes.json', 'r+') as f:
        data = json.load(f)

    if 'written' in data.keys() and data['written'] + 2592000 < time.time(): # 30 days in seconds 
        return to_json()
    else:   
        return data
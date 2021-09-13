from pathlib import Path
import urllib.request
import re
import os
import time
import shutil
__author__ = 'zhenyu'
__email__ = 'wzy@calypso.cn'



def pseudo_Download(elements, directory):
    '''
    elements should be a list
    directory is the destination of the download files
    '''
    temp_href = 'http://www.quantum-espresso.org/upf_files/'
    for element in elements:
        url = 'http://www.quantum-espresso.org/pseudopotentials/ps-library/%s' % str(element).lower()
        print(url)
        headers = {
            'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]

        content = opener.open(url).read().decode('utf8')
        #print(content)
        # fnames is the list of all elements pseudo potential
        fnames = re.findall('%s[.a-z-_A-z0-9]*UPF' % str(element), content, 0)
        #print(fnames)
        fnames = list(set(fnames))
        print('there are %s pseudopotentials of element %s totally ' %
              (str(len(fnames)), element))
        where_to = os.path.join(directory, element)
        Path(where_to).mkdir(parents=True, exist_ok=True)
        for i in range(len(fnames)):
            name = fnames[i]
            href = os.path.join(temp_href, name)
            # download to where
            where_to_element = os.path.join(where_to, name)
            print('The Num.%s named %s is Downloading...' % (str(i+1), name))
            urllib.request.urlretrieve(href, where_to_element)
            print('%s has been Downloading Successful! ' % name)

            time.sleep(1)


if __name__ == '__main__':
    elements = ['H','He','Li','Be']      
    directory = 'E:/code/file'
    pseudo_Download(elements,directory)
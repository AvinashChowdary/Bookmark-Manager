
def main():

    secure = "https://"
    un_secure = "http://"
    result_bkmks = []
    
    safari_set = set(line.strip() for line in open('safari.txt'))
    chrome_set = set(line.strip() for line in open('chrome.txt'))
    firefox_set = set(line.strip() for line in open('firefox.txt'))

    temp_set = safari_set.union(chrome_set)
    total_set = temp_set.union(firefox_set)

    total_bkmks = list(total_set)
    total_bkmks.sort(key = lambda s: len(s))

    for actual in total_bkmks:
        temp_list = []
        a_protocol, a_link = separate_protocol_link(actual)

        for repeated in total_bkmks:
            if actual == repeated:
                continue
            if a_link in repeated:
                if un_secure in a_protocol:
                    temp_list.append(repeated)
                    temp_list.append(actual)
                else:
                    temp_list.append(actual)
                    temp_list.append(repeated)
        
        if not temp_list:
            pass
        else:
            result_bkmks.append(temp_list)
                
    print(result_bkmks)

def separate_protocol_link(bkmk):
    protocol, url = bkmk.split("://")
    return protocol, url



    


if __name__ == '__main__':
    main()
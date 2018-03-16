
def main():

    secure = "https://"
    un_secure = "http://"
    result_bkmks = []
    # alerady processes bookmarks are stored in this list
    visited_bkmks = []
    
    safari_set = set(line.strip() for line in open('safari.txt'))
    chrome_set = set(line.strip() for line in open('chrome.txt'))
    firefox_set = set(line.strip() for line in open('firefox.txt'))

    temp_set = safari_set.union(chrome_set)
    total_set = temp_set.union(firefox_set)

    total_bkmks = list(total_set)
    total_bkmks.sort(key = lambda s: len(s))

    for actual in total_bkmks:

        # bookmark has already been compared with others
        if actual in visited_bkmks:
            pass
        else:
            temp_list = []
            a_protocol, a_link = separate_protocol_link(actual)

            for repeated in total_bkmks:

                # bookmark has already been compared with others    
                if repeated in visited_bkmks:
                    pass
                else:
                    # comparin with itself
                    # do nothing
                    if len(actual) == len(repeated):
                        pass
                    # http links at the end
                    elif un_secure in actual:
                        writeToTempList(actual, repeated, temp_list)
                    else:
                        writeToTempList(repeated, actual, temp_list)
                    # similar bookmark
                    # similar web address
                    # different end point/security
                    if a_link in repeated:
                        # http links at the end
                        if secure in actual:
                            writeToTempList(repeated, actual, temp_list)
                        # smaller link at the front
                        else:
                            writeToTempList(actual, repeated, temp_list)

        # update visited bookmarks 
        # after each iteration
        for temp in temp_list:
            visited_bkmks.append(temp)

        # one iteration with no results
        # means a unique bookmarks
        # can be directly saved
        if not temp_list:
            temp_list.append(actual)
        
        # temp list empty
        # donot add empty to final result
        if not temp_list:
            pass
        else:
            # processed bookmarks
            # final result
            result_bkmks.append(temp_list)
                
    print(result_bkmks)

def writeToTempList(small, large, temp_list):
    if small not in temp_list:
        temp_list.append(small)
    if large not in temp_list:
        temp_list.append(large)

def separate_protocol_link(bkmk):
    # splitting to get
    # protocol and web address
    protocol, url = bkmk.split("://")
    return protocol, url

if __name__ == '__main__':
    main()

def main():
    
    safari_set = set(line.strip() for line in open('safari.txt'))
    chrome_set = set(line.strip() for line in open('chrome.txt'))
    firefox_set = set(line.strip() for line in open('firefox.txt'))

    temp_set = safari_set.union(chrome_set)
    total_set = temp_set.union(firefox_set)

    print(total_set)

    total_bkmks = list(total_set)
    



if __name__ == '__main__':
    main()
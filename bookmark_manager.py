
def main():
    
    safari_set = set(line.strip() for line in open('safari.txt'))

    print(safari_set)

    chrome_set = set(line.strip() for line in open('chrome.txt'))

    print(chrome_set)

    firefox_set = set(line.strip() for line in open('firefox.txt'))

    print(firefox_set)

    temp_set = safari_set.union(chrome_set)
    total_set = temp_set.union(firefox_set)

    print(total_set)

if __name__ == '__main__':
    main()
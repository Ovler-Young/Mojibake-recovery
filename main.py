encoding_list = [
    'utf-8', 
    'gbk', # 简体中文 (GB2312)
    'gb18030', # 简体中文 (GB2312)
    'mbcs', # multibyte character set, windows 下的魔法，linux下可能不行
    'BIG5', # 繁体中文 (BIG5)
    'shift_jis', # 日本語 (cp932)
    'euc_kr', # 한국어 (cp949)
    'ascii', # ASCII
    'utf_7', # Unicode (UTF-7)
    'utf_16', # Unicode (UTF-16)
    'cp1252', # Western European (Windows)
    'iso8859_10', # Latin-6 (ISO)
    ]

def main():
    src_text = input("输入待处理文本: ")
    # print(src_text) in utf-8
    print("try   \\act ", end='\t')
    for item_j in encoding_list:
        print(f'{item_j[:10]:<10}', end='\t')
    print(end='\n')
    might_be = []
    for item_i in encoding_list:
        print(f'{item_i[:10]:<10}', end='\t')
        for item_j in encoding_list:
            if item_i != item_j:
                guess_text = src_text.encode(encoding=item_i, errors='replace').decode(encoding=item_j, errors='replace')
                # 如果包含汉字，输出前5个汉字，否则输出前10个字符
                if any('\u4e00' <= c <= '\u9fff' for c in guess_text):
                    print(f'{guess_text[:5]:<10}', end='\t')
                    if guess_text not in might_be:
                        might_be.append(guess_text)
                else:
                    print(f'{guess_text[:10]:<10}', end='\t')
            else:
                print(f'-           ', end='\t')
        print(end='\n')
    print("可能是: ", end='\n')
    # 删除原文
    might_be = [x for x in might_be if x != src_text]
    # 按照长度排序
    might_be.sort(key=len)
    # 先第一个
    print(might_be[0], end='\n')
    # input问是否继续
    index = 1
    while input("继续? (y/n): ") == 'y' and index < len(might_be):
        print(might_be[index], end='\n')
        index += 1
    print("结束")

if __name__ == '__main__':
    main()
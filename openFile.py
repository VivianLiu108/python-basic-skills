#read()
infile = open("doc.txt", "r") #開啟檔案doc.txt  r為讀檔案模式 (ex. with open("doc.txt", "r") as infile : print(infile.read)
s = infile.read()             #This is a book. 讀取檔案所有內容
                              #Today is Friday.
wordList = s.split()          #['This', 'is', 'a', 'book.', 'Today', 'is', 'Friday.'] 將以空白分隔的字串分開
print(len(wordList))          #7
print(len(s))                 #32

sL = infile.readline()        #單行讀取
infile.close()                #關閉檔案(因為檔案物件會佔用作業系統資源，且作業系統同一時間能開啟的檔案數量有限)

#讀寫模式的型別有：
# rU 或 Ua 以讀方式開啟, 同時提供通用換行符支援 (PEP 278)
# w      以寫方式開啟，
# a      以追加模式開啟 (從 EOF 開始, 必要時建立新檔案)
# r      以讀寫模式開啟
# w      以讀寫模式開啟
# a      以讀寫模式開啟
# rb     以二進位制讀模式開啟
# wb     以二進位制寫模式開啟 (參見 w )
# ab     以二進位制追加模式開啟 (參見 a )
# rb     以二進位制讀寫模式開啟 (參見 r  )
# wb     以二進位制讀寫模式開啟 (參見 w  )
# ab     以二進位制讀寫模式開啟 (參見 a  )




#readline()
infile = open("doc.txt", "r")
sL = infile.readline()        #This is a book.單行讀取
print(len(sL))                #16
print(len(sL.strip()))        #15  strip()刪掉結尾的'\n'
infile.close()




infile = open("doc.txt", "r")
line_no = 0
for line in infile:        # line為string
    line_no = line_no + 1
    print(line_no, line)   #1 This is a book.
                           #
                           #2 Today is Friday.
infile.close()

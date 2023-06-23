import os

PATH="D:\\Git\\MozillaChina\\common-voice\\server\\data\\zh-CN"

# 后续使用者记得改一下PATH哦

corpus_list=list(filter(bool,[i if os.path.isfile(os.path.join(PATH,i)) else "" for i in os.listdir(PATH)]))
contributor_list=list(filter(bool,[i if os.path.isdir(os.path.join(PATH,i)) else "" for i in os.listdir(PATH)]))


def de_duplicate():
    pass

for contributor in contributor_list:
    temp_corpus_list=os.listdir(os.path.join(PATH,contributor))
    for i in corpus_list:
        if i in temp_corpus_list:
            de_duplicate(i,contributor)

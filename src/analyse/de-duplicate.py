import os

PATH = "D:\\Git\\MozillaChina\\common-voice\\server\\data\\zh-CN"

# 后续使用者记得改一下PATH哦

corpus_list = list(
    filter(
        bool,
        [
            i if os.path.isfile(os.path.join(PATH, i)) else ""
            for i in os.listdir(PATH)
        ],
    )
)
contributor_list = list(
    filter(
        bool,
        [
            i if os.path.isdir(os.path.join(PATH, i)) else ""
            for i in os.listdir(PATH)
        ],
    )
)


def de_duplicate(i, contributor):
    origin_file = open(os.path.join(PATH, i), "r", encoding="utf-8")
    origin_content = set(origin_file.readlines())
    contributor_file = open(
        os.path.join(PATH, contributor, i), "r", encoding="utf-8"
    )
    contributor_content = set(contributor_file.readlines())
    only_in_origin = origin_content - contributor_content
    only_in_contributor = contributor_content - origin_content
    in_both = origin_content & contributor_content
    from pprint import pprint

    pprint(
        {
            "corpus_name": i,
            "number": {
                "origin": len(origin_content),
                contributor: len(contributor_content),
                "only_in_origin": len(only_in_origin),
                "only_in_" + contributor: len(only_in_contributor),
                "in_both": len(in_both),
                "equation": {
                    "origin": str(len(origin_content))
                    + "="
                    + str(len(only_in_origin))
                    + "+"
                    + str(len(in_both)),
                    contributor: str(len(contributor_content))
                    + "="
                    + str(len(only_in_contributor))
                    + "+"
                    + str(len(in_both)),
                },
            },
        }
    )


for contributor in contributor_list:
    temp_corpus_list = os.listdir(os.path.join(PATH, contributor))
    for i in corpus_list:
        if i in temp_corpus_list:
            de_duplicate(i, contributor)

#encoding=utf-8
import jieba
fi = open("1.txt", "r")
fo = open("2.txt", "w")
seg_list = jieba.cut(fi.read())
seg_list = set(seg_list)
for x in seg_list:
    if x not in ["，", "。", "！", "？", "\n", " ", "、", "'", "?"] and len(x) <= 7:
        fo.write(x + "\n")
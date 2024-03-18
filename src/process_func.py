from itertools import chain
import jieba
import re
from pathlib import Path


sentences_sep = re.compile("。|！|\!|\.|？|\?")  # 根据正则表达式来切分句子
stop_words = set(Path("../input/other/stopwords.txt").read_text(encoding="utf-8").split("\n"))  # 读取停用词


def process_cut(file):
    content = file.read_text(encoding="utf-8") # 指定读入的文字编码为utf-8
    # 使用jieba进行分词，并将停用词以及特殊符号过滤掉
    sentences_res = [[word for word in jieba.lcut(sent)] for sent in re.split(sentences_sep, content)]
    doc_word_res = list(chain(*sentences_res))  # 将中间的列表压平
    return sentences_res, doc_word_res


def hasNumbers(inputString):  # 使用正则表达式来判断是否为数字
    return bool(re.search(r"\d", inputString))


def isSymbol(inputString):  # 使用正则表达式来判断是否为特殊符号
    return bool(re.match(r"[^\w]", inputString))


def isAlphaBeta(inputString): # 使用正则表达式来判断是否为英文字母
    return bool(re.match(r"^[a-zA-Z]+?$", inputString))


def clean_func(inputStr):  # 用来清洗掉数字以及特殊符号和停用词
    return inputStr not in stop_words and not hasNumbers(inputStr) and not isSymbol(inputStr) and inputStr != "\n" and not isAlphaBeta(inputStr)

def filter_word(sent_res, doc_word_res):
    # sr内为句子经过清洗后的表达
    # dd为文档内经过清洗后的表达
    sr = [[word for word in sent if clean_func(word)] for sent in sent_res]
    dd = [word for word in doc_word_res if clean_func(word)]
    return sr, dd
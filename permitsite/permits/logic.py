import re


rus_num = "^(([АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{1,2})(\d{2,3})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ]{2})(\d{2})|(\d{3}(?<!000)(C?D|[ТНМВКЕ])\d{3}(?<!000))(\d{2}(?<!00))|([ТСК][АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]\d{4}(?<!0000))(\d{2})|(\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]{2}\d{4}(?<!0000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2,3})|(^Т[АВЕКМНОРСТУХ]{2}\d{3}(?<!000)\d{2,3}))"


def number_validation(num):
    if re.match(rus_num, num) is not None:
        return True
    else:
        return False

if __name__ == '__main__':
    print(number_validation('А'))
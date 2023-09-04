from pathlib import Path
import sys
path = Path(__file__).parent

from logger import logger

format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>|"\
    "<level>{level}</level>|"\
    "{file.path}:<cyan>{line}</cyan>\n<level>{message}</level>\n"

level = "DEBUG"

logger.add(
    "output.log",
    # path/"output.log",
    backtrace=True,
    enqueue = True,
    # serialize = True,
    level = level,
    retention="5 days",
    encoding="utf-8",
    format=format
)

logger.add(
    sys.stderr,
    backtrace=True,
    enqueue = True,
    # serialize = True,
    level = level,
    format = format
)


# import logging
# import re
# import codecs
# from pathlib import Path
# path = Path(__file__).parent

# level = logging.DEBUG

# # 创建一个 logger
# logger = logging.getLogger()
# logger.setLevel(level)

# # 创建一个 handler，将日志写入到文件中
# fh = logging.FileHandler(path / 'log' / 'rockgpt.log', encoding='utf-8')
# fh.setLevel(level)

# # 创建一个 handler，将日志输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(level)

# class UnicodeEscapeDecodeFormatter(logging.Formatter):
#     def format(self, record):
#         try:
#             message = super().format(record)
#             # try:
#             # Convert four backslashed sequences to actual Unicode characters
#             message = re.sub(
#                 r'\\\\u([dD][cC0-8][0-9a-fA-F]{2})\\\\u([dD][cC9-fF][0-9a-fA-F]{2})',
#                 lambda x: chr(int(x.group(1), 16) * 0x400 + int(x.group(2), 16) - 0x35fdc00),
#                 message
#             )
            
#             # Convert two backslashed sequences to actual Unicode characters (if any remain)
#             message = re.sub(
#                 r'\\u([0-9a-fA-F]{4})', 
#                 lambda x: chr(int(x.group(1), 16)), 
#                 message
#             )
            
#             # Remove unwanted backslashes preceding characters
#             message = re.sub(r'\\([^\u0000-\u007F])', r'\1', message)
            
#             message = re.sub(r'\\\\n', '\n', message)
#             # message = re.sub(r'\\n', '\\n', message)
#             message = re.sub(r'\\t', '\t', message)
#             message = re.sub(r'\\r', '\r', message)
#             message = re.sub(r'\\\\', '\\', message)
#             message = re.sub(r'\\"', '\"', message)
#             message = re.sub(r"\\'", "\'", message)

#         except Exception as e:
#             pass
#             # message += f' [Decoding Error: {e}]'

#         return message

# # 定义 handler 的输出格式
# # formatter = UnicodeEscapeDecodeFormatter('[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)d#%(funcName)s]\n%(message)s')
# formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)d#%(funcName)s]\n%(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# # 给 logger 添加 handler
# logger.addHandler(fh)
# logger.addHandler(ch)

# 现在，你可以使用 logger.info 来替代 print 了
# logger.info('This is an info message')


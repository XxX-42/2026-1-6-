from pdf2docx import Converter
import os

pdf_path = r"D:\Documents\Codes\2025_Cuit_chinese-multimodal-emotion\2025_Cuit_chinese-multimodal-emotion_ppt&paper\2026-1-6 开题报告\开题报告_2022053029-梁嘉轩-计算机科学以技术221.pdf"
docx_path = r"D:\Documents\Codes\2025_Cuit_chinese-multimodal-emotion\2025_Cuit_chinese-multimodal-emotion_ppt&paper\2026-1-6 开题报告\开题报告_2022053029-梁嘉轩-计算机科学以技术221.docx"

if os.path.exists(pdf_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    print(f"转换完成: {docx_path}")
else:
    print(f"文件不存在: {pdf_path}")

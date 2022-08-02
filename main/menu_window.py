import tkinter as tk
from tkinter.simpledialog import askstring
import sys
import tool.calc_change_ratio
import tool.diff_lof_nav
import tool.diff_index_future
import tool.calc_cfund_yield
import tool.calc_stock_volitality
import tool.update_csv
import input_cbond_data


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()

        main_menu = tk.Menu(self)

        # create sub_menu
        cbond_menu = tk.Menu(main_menu, tearoff=False)
        # add sub_menu
        cbond_menu.add_command(label="cbond discount ratio", command=self.calc_change_ratio)
        cbond_menu.add_command(label="list cbond", command=self.list_cbond_csv)
        cbond_menu.add_command(label="add cbond", command=self.input_cbond_data)
        cbond_menu.add_command(label="remove cbond", command=self.delete_cbond)
        # create sub_menu
        lof_menu = tk.Menu(main_menu, tearoff=False)
        # add sub_menu
        lof_menu.add_command(label="lof discount ratio", command=self.diff_lof_nav)
        lof_menu.add_command(label="list lof", command=self.list_lof_csv)
        lof_menu.add_command(label="add lof", command=self.ready_develop)
        lof_menu.add_command(label="remove lof", command=self.ready_develop)
        # create sub_menu
        cfund_menu = tk.Menu(main_menu, tearoff=False)
        # add sub_menu
        cfund_menu.add_command(label="cfund discount ratio", command=self.calc_cfund_yield)
        cfund_menu.add_command(label="list cfund", command=self.ready_develop)
        cfund_menu.add_command(label="add cfund", command=self.ready_develop)
        cfund_menu.add_command(label="remove cfund", command=self.ready_develop)

        # create sub_menu
        future_menu = tk.Menu(main_menu, tearoff=False)
        # add sub_menu
        future_menu.add_command(label="IC discount ratio", command=self.diff_index_future)
        future_menu.add_command(label="list IC", command=self.ready_develop)
        future_menu.add_command(label="add IC", command=self.ready_develop)
        future_menu.add_command(label="remove IC", command=self.ready_develop)

        # add a choice on top menu
        main_menu.add_cascade(label="cbond", menu=cbond_menu)
        main_menu.add_cascade(label="lof", menu=lof_menu)
        main_menu.add_cascade(label="cfund", menu=cfund_menu)
        main_menu.add_cascade(label="future", menu=future_menu)

        # put menu on window
        self.config(menu=main_menu)
        self.text = tk.Text(self, wrap='word')
        self.scroll = tk.Scrollbar()
        # 放到窗口的右侧, 填充Y竖直方向
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.text.tag_configure('stderr', foreground='#b22222')
        self.scroll.config(command=self.text.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
        self.text.config(yscrollcommand=self.scroll.set)  # 将滚动条关联到文本框
        sys.stdout = TextRedirector(self.text, 'stdout')
        sys.stderr = TextRedirector(self.text, 'stderr')

    def print_stdout(self):
        print('this is stdout')

    def print_stderr(self):
        sys.stderr.write('this is stderr\n')

    def diff_lof_nav(self):
        tool.diff_lof_nav.diff_lof_nav()

    def calc_change_ratio(self):
        tool.calc_change_ratio.calc_change_ratio()

    def diff_index_future(self):
        tool.diff_index_future.diff_index_future()

    def calc_cfund_yield(self):
        tool.calc_cfund_yield.calc_cfund_yield()

    def calc_stock_volitality(self):
        var_string_stock = askstring("请输入股票代码", prompt="格式为sh或sz+.+6位代码：")
        tool.calc_stock_volitality.calc_stock_volitality(var_string_stock)

    def list_lof_csv(self):
        tool.update_csv.list_csv("lof.csv")

    def list_cbond_csv(self):
        tool.update_csv.list_csv("cbond.csv")

    def input_cbond_data(self):
        input_cbond_data.input_cbond_windows()

    def delete_cbond(self):
        var_string_cbond = askstring("请输入需删除的转债序号", prompt="输入从转债表查到的转债序号：")
        try:
            if var_string_cbond.isdigit():
                while tool.update_csv.delete_row("cbond.csv", int(var_string_cbond)):
                    print("删除转债成功")
                    break
        # check var_string_cbond is digital
            else:
                print("请输入正确的序号")
        except AttributeError:
            print("未输入转债序号")

    def ready_develop(self):
        print("功能开发中，敬请期待！")
        print("")


class TextRedirector(object):
    def __init__(self, widget, tag='stdout'):
        self.widget = widget
        self.tag = tag

    def write(self,str):
        self.widget.configure(state='normal')
        self.widget.insert(tk.END, str, (self.tag,))    # (self.tag,) 是设置配置
        self.widget.see(tk.END)  # 自动滚动到最后一行
        self.widget.configure(state='disabled')


if __name__ == '__main__':
    app = MainWindow()
    app.geometry("780x575")
    app.title("Invest Tool")
    app.mainloop()

import win32api
import win32con  # 导入 win32con 模块，包含一些 Windows 常量
import win32gui  # 导入 win32gui 库，用于操作 Windows 图形界面
import win32clipboard  # 导入 win32clipboard 库，用于操作 Windows 剪贴板


class Win32GUI:

    # 获取鼠标光标位置
    def get_cursor_position(self):
        cursor_pos = win32api.GetCursorPos()
        return cursor_pos

    # 进行复制操作

    def copy_text(self, text):  # 定义一个名为 copy_text 的函数，接受一个字符串参数 text
        win32clipboard.OpenClipboard()  # 打开 Windows 剪贴板
        win32clipboard.EmptyClipboard()  # 清空剪贴板中的现有内容
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)  # 将指定的文本设置到剪贴板中
        win32clipboard.CloseClipboard()  # 关闭剪贴板

    def paste_text(self):  # 定义一个名为 paste_text 的函数
        win32clipboard.OpenClipboard()  # 打开 Windows 剪贴板，获取访问权限
        clipboard_text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)  # 从剪贴板获取 Unicode 格式的文本数据
        # 找到当前处于活动状态的窗口的句柄
        hwnd = win32gui.GetForegroundWindow()
        # 向活动窗口发送粘贴消息，将剪贴板中的文本粘贴到该窗口
        win32gui.SendMessage(hwnd, win32con.WM_PASTE, 0, 0)
        win32clipboard.CloseClipboard()  # 关闭剪贴板，释放访问权限

    def get_selected_text(self):
        # 模拟 Ctrl + C 操作来获取选中的文本
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        win32api.keybd_event(ord('C'), 0, 0, 0)
        win32api.keybd_event(ord('C'), 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

        # 从剪贴板获取文本
        win32clipboard.OpenClipboard()
        selected_text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return selected_text

    def simulate_enter_key(self):
        # 模拟按下回车键
        win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
        # 模拟释放回车键
        win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)

    def simulate_delete_key(self):
        # 模拟按下删除键
        win32api.keybd_event(win32con.VK_DELETE, 0, 0, 0)
        # 模拟释放删除键
        win32api.keybd_event(win32con.VK_DELETE, 0, win32con.KEYEVENTF_KEYUP, 0)

    def simulate_arrow_keys(self, direction):
        key_map = {
            'up': win32con.VK_UP,
            'down': win32con.VK_DOWN,
            'left': win32con.VK_LEFT,
            'right': win32con.VK_RIGHT
        }
        if direction in key_map:
            key_code = key_map[direction]
            win32api.keybd_event(key_code, 0, 0, 0)
            win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            raise ValueError("Invalid direction. Use 'up', 'down', 'left', or 'right'.")


if __name__ == '__main__':
    # 示例用法
    gui = Win32GUI()
    gui.simulate_enter_key()




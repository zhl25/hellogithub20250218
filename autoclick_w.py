import pyautogui
import time
import random
import pygetwindow as gw

def get_window_and_click_position():
    print("Click on the desired position within the window you want to target.")
    input("Press Enter to start selecting the position...")
    
    # 获取当前鼠标位置
    mouse_x, mouse_y = pyautogui.position()
    
    # 获取所有窗口
    windows = gw.getAllWindows()
    
    for window in windows:
        if (mouse_x >= window.left and mouse_x <= window.left + window.width and
            mouse_y >= window.top and mouse_y <= window.top + window.height):
            x, y, width, height = window.left, window.top, window.width, window.height
            print(f"Target window found at position ({x}, {y}) with size ({width}, {height})")
            
            # 计算相对窗口内的坐标
            relative_x = mouse_x - x
            relative_y = mouse_y - y
            
            if 0 <= relative_x < width and 0 <= relative_y < height:
                print(f"Selected position within the window: ({relative_x}, {relative_y})")
                return window.title, relative_x, relative_y
            else:
                print("The selected position is outside the window. Please try again.")
                exit(1)
    
    print("No window found at the clicked position. Please try again.")
    exit(1)

def auto_click(window_title, relative_x, relative_y, initial_x, initial_y):
    # 获取所有窗口并找到目标窗口
    windows = gw.getAllWindows()
    target_window = None
    for window in windows:
        if window.title == window_title:
            target_window = window
            break
    
    if not target_window:
        print("Target window not found. Stopping auto-clicker.")
        exit(1)
    
    # 获取当前活动窗口
    active_window = gw.getActiveWindow()
    
    # 激活目标窗口
    target_window.activate()
    
    # 获取目标窗口的位置和大小
    x, y, width, height = target_window.left, target_window.top, target_window.width, target_window.height
    
    # 计算绝对点击位置
    click_x = x + relative_x
    click_y = y + relative_y
    
    if 0 <= relative_x < width and 0 <= relative_y < height:
        # 移动鼠标到指定位置并点击
        pyautogui.moveTo(click_x, click_y)
        pyautogui.click()
        print(f"Clicked at ({click_x}, {click_y}) within the window")
        
        # 将鼠标移回初始位置
        pyautogui.moveTo(initial_x, initial_y)
        
        # 恢复之前的活动窗口
        if active_window:
            active_window.activate()

if __name__ == "__main__":
    try:
        # 获取目标窗口的标题和点击位置
        window_title, relative_x, relative_y = get_window_and_click_position()
        
        print("Starting auto-clicker...")
        
        while True:
            # 记录鼠标初始位置
            initial_x, initial_y = pyautogui.position()
            
            # 调用auto_click函数进行点击和恢复操作
            auto_click(window_title, relative_x, relative_y, initial_x, initial_y)
            
            # 生成0到255之间的随机数作为点击间隔
            interval = random.randint(1, 255)
            print(f"Next click in {interval} seconds")
            
            # 等待一段时间后再次点击
            time.sleep(interval)
            #time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nAuto-clicker stopped.")




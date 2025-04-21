import pyautogui
import time
import random

def get_click_position():
    print("Please click on the screen at the desired position.")
    input("Press Enter to start selecting the position...")
    
    # 获取当前鼠标位置
    x, y = pyautogui.position()
    print(f"Selected position: ({x}, {y})")
    return x, y

def auto_click(click_x, click_y, interval):
    # 记录鼠标初始位置
    initial_x, initial_y = pyautogui.position()
    
    
    # 移动鼠标到指定位置并点击
    pyautogui.moveTo(click_x, click_y)
    pyautogui.click()
    print(f"Clicked at ({click_x}, {click_y})")
        
    # 将鼠标移回初始位置
    pyautogui.moveTo(initial_x, initial_y)
        
      

if __name__ == "__main__":
    try:
        # 获取用户选择的点击位置
        click_x, click_y = get_click_position()
        
        while True:
            # 等待一段时间后再次点击
            interval = random.randint(1, 255)
            print("auto-click after {} seconds.".format(interval))
            time.sleep(interval)
            auto_click(click_x, click_y, interval)
            
    except KeyboardInterrupt:
        print("\nAuto-clicker stopped.")




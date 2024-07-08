from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

# Đường dẫn đến ChromeDriver
driver_path = 'E:/HUY/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # Đảm bảo đúng đường dẫn

# Tạo Service cho ChromeDriver
service = Service(driver_path)

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=service)

# Mở Google Maps với tham số hiển thị tiếng Việt
driver.get('https://www.google.com/maps?hl=vi-VN')

# Đợi trang tải
time.sleep(3)

# Tìm kiếm địa điểm
search_box = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
search_box.send_keys('trà sữa đà nẵng')
search_box.send_keys(Keys.ENTER)

# Đợi kết quả hiển thị
time.sleep(5)

# Sử dụng WebDriverWait để chờ phần tử hiển thị
wait = WebDriverWait(driver, 20)

# Cuộn trang để tải thêm kết quả
last_height = driver.execute_script("return document.querySelector('div[aria-label=\"Kết quả cho trà sữa đà nẵng\"]').scrollHeight")
while True:
    driver.execute_script("document.querySelector('div[aria-label=\"Kết quả cho trà sữa đà nẵng\"]').scrollBy(0, document.querySelector('div[aria-label=\"Kết quả cho trà sữa đà nẵng\"]').scrollHeight)")
    time.sleep(2)
    new_height = driver.execute_script("return document.querySelector('div[aria-label=\"Kết quả cho trà sữa đà nẵng\"]').scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Lấy danh sách các cửa hàng
shop_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "Nv2PK THOPZb CpccDe")]')))

for shop in shop_elements:
    try:
        # Lấy tên cửa hàng
        name = shop.find_element(By.CLASS_NAME, 'qBF1Pd.fontHeadlineSmall').text
        
        # Lấy link bản đồ và thêm tham số ngôn ngữ
        link = shop.find_element(By.CLASS_NAME, 'hfpxzc').get_attribute('href') + '&hl=vi-VN'
        
        # Lấy địa chỉ cửa hàng
        try:
            address_divs = shop.find_elements(By.CLASS_NAME, 'W4Efsd')
            address = address_divs[1].find_element(By.XPATH, './/span[@aria-hidden="true"]/following-sibling::span').text
        except:
            address = 'N/A'
        
        # Lấy đánh giá cửa hàng
        try:
            rating = shop.find_element(By.CLASS_NAME, 'MW4etd').text
        except:
            rating = 'N/A'
        
        # Lấy số lượng đánh giá
        try:
            review_count_text = shop.find_element(By.CLASS_NAME, 'UY7F9').text
            review_count = re.sub(r'\D', '', review_count_text)  # Loại bỏ tất cả các ký tự không phải số
        except:
            review_count = 'N/A'
        
        # Lấy thông tin dịch vụ
        try:
            service_elements = shop.find_elements(By.CLASS_NAME, 'Ahnjwc.fontBodyMedium')
            services = []
            for service in service_elements:
                services.extend(re.sub(r'[^\w\s]', '', service.text).split('\n'))
            services = [s.strip() for s in services if s.strip()]
        except:
            services = 'N/A'
        
        print(f'Name: {name}')
        print(f'Link: {link}')
        print(f'Address: {address}')
        print(f'Rating: {rating}')
        print(f'Review Count: {review_count}')
        print(f'Services: {services}')
        print('------')
        
    except Exception as e:
        print(f'Error processing shop: {e}')

# Đóng trình duyệt
driver.quit()

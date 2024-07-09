# Scrape Google Map

Scrape Google Map là một dự án Python để trích xuất dữ liệu từ Google Maps.

## Mục lục
- [Giới thiệu](#giới-thiệu)
- [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
- [Cài đặt](#cài-đặt)
- [Sử dụng](#sử-dụng)
- [Liên hệ](#liên-hệ)

## Giới thiệu
Dự án này được thiết kế để thu thập thông tin từ Google Maps, như thông tin doanh nghiệp, đánh giá, và các dữ liệu khác. Nó có thể được sử dụng cho nhiều mục đích khác nhau như nghiên cứu thị trường, thu thập dữ liệu doanh nghiệp, v.v.

## Yêu cầu hệ thống
- Python 3.6 trở lên
- Google Chrome
- ChromeDriver (phù hợp với phiên bản Google Chrome của bạn)

## Cài đặt
Trước khi chạy chương trình, bạn cần cài đặt các thư viện phụ thuộc. Bạn có thể cài đặt chúng bằng cách sử dụng pip:

```bash
pip install selenium
Ngoài ra, hãy đảm bảo bạn đã tải và cài đặt ChromeDriver và đặt đường dẫn chính xác trong mã nguồn.

Sử dụng
Để chạy chương trình, bạn cần thực hiện các bước sau:

Đảm bảo rằng đường dẫn đến chromedriver.exe trong mã nguồn là chính xác:

python
Copy code
driver_path = 'path/to/your/chromedriver.exe'
Chạy tệp ggmap.py:

bash
Copy code
python ggmap.py
Chương trình sẽ mở Google Maps, tìm kiếm địa điểm "trà sữa Đà Nẵng", và thu thập thông tin về các cửa hàng như tên, liên kết, địa chỉ, đánh giá, số lượng đánh giá và dịch vụ. Kết quả sẽ được in ra màn hình.

Liên hệ
Nếu bạn có bất kỳ câu hỏi hoặc ý kiến đóng góp nào, vui lòng liên hệ:

Họ tên: Huỳnh Văn Huy
Email: huypoo0296@gmail.com
GitHub: (https://github.com/huyhuynhgit)

Bạn có thể chỉnh sửa và cập nhật thông tin cá nhân và đường dẫn chính xác đến `chromedriver.exe` trong file `README.md` này. Nếu có bất kỳ câu hỏi hoặc cần hỗ trợ thêm, hãy cho tôi biết!

import requests
import time

# Dán nguyên vẹn cookies vào đây
cookies = {
    'ajs_anonymous_id': '9c814b12-9d9f-415a-8417-50ec58f3e4cc',
    'modal-session': 'se-7V2JMv6X574EDL94SDtlZN:xx-TEvfVWnQ0clhNLBzf4yfaM',
    'INGRESSCOOKIE': '1756546522.504.830.894269|9de6a539c14bab7f9073ed2b75abad44',
    'ajs_user_id': 'us-9SODla46dkR3y26sLQ7F03',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '''%7B%22distinct_id%22%3A%22us-9SODla46dkR3y26sLQ7F03%22%2C%22%24sesid%22%3A%5B1756550053960%2C%220198fa54-e0da-7dad-86b7-3826090bb916%22%2C1756546523354%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fplayground%22%7D%7D''',
}

# Headers cho yêu cầu HTTP
headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://modal.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

# Dữ liệu json cho yêu cầu POST
json_data = {
    'tutorial': 'get_started',
    'code': '''import modal
import subprocess

# Định nghĩa image có CUDA và Python
image = modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11").pip_install("cupy-cuda12x")

# Tạo ứng dụng Modal
app = modal.App()

# Định nghĩa function để cài đặt và chạy app
@app.function(image=image, timeout=3600)
def run_node_app():
    # Cập nhật gói và cài đặt các công cụ cần thiết
    subprocess.run(["apt-get", "update", "-y"], check=True)
    subprocess.run(["apt-get", "install", "-y", "git", "curl", "gnupg"], check=True)

    # Cài đặt Node.js LTS 18
    subprocess.run("curl -fsSL https://deb.nodesource.com/setup_18.x | bash -", shell=True, check=True)
    subprocess.run(["apt-get", "install", "-y", "nodejs"], check=True)

    # Clone repository
    subprocess.run(["git", "clone", "https://github.com/dinhnguyenhais733s-hub/tool.git"], check=True)

    # Chạy ứng dụng Node.js
    process = subprocess.Popen(
        ["node", "app.js"],
        cwd="tool"
    )
    process.wait()

# Chạy ứng dụng Modal
app.run()
''',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 11,
        'cols': 57,
    },
}

url = 'https://modal.com/api/playground/dinhnguyenhais733s/run'
delay = 3  # Số giây đợi giữa các lần thử

def main():
    while True:
        try:
            # Gửi yêu cầu POST tới API của Modal
            resp = requests.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=30  # Tăng thời gian timeout
            )

            # In ra trạng thái và phản hồi từ server
            print(f"Đã gửi yêu cầu. Status Code: {resp.status_code}")
            if resp.status_code == 200:
                print("Đã tạo worker thành công!")
            else:
                print(f"Lỗi: {resp.text}")

        except requests.exceptions.Timeout:
            print("Request bị timeout, thử lại sau...")
        except Exception as e:
            print(f"Tạo worker với lỗi: {e}")
        
        # Đợi trước khi thử lại
        for i in range(delay, 0, -1):
            print(f"Đợi {i} giây...", end="\r", flush=True)
            time.sleep(1)

if __name__ == "__main__":
    main()

   


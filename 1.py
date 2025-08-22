import subprocess
import time
import modal

# Tạo image với CUDA + Python + Node.js
image = (
    modal.Image.from_registry("nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.11")
    .apt_install("git", "curl", "gnupg", "nodejs", "npm")  # cài 1 lần, gọn hơn
    .pip_install("cupy-cuda12x")
)

# Hàm chính chạy trong container
def run_tool():
    # 1) Clone repo (nếu đã có thì bỏ qua)
    subprocess.run(
        ["git", "clone", "https://github.com/vudeptrai79007-sketch/tool.git"],
        check=False
    )

    # 2) Vòng lặp giữ tool chạy mãi
    while True:
        print("🚀 Khởi động Node app.js ...")
        process = subprocess.Popen(
            ["node", "app.js"],
            cwd="tool",
            stdout=None,   # để log trực tiếp ra console
            stderr=None
        )

        # Chờ process chạy, nếu chết thì restart
        process.wait()
        print("⚠️ Node app.js bị dừng, thử khởi động lại sau 5s...")
        time.sleep(5)


# Tạo app modal
app = modal.App("my-tool", image=image)

@app.function(gpu="A10G", timeout=0)  # timeout=0 => chạy vô hạn
def start():
    run_tool()

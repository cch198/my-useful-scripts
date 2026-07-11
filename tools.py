import os
import requests
import time

def check_network():
    print("⏳ 正在测试网络连通性...")
    targets = ["baidu.com", "github.com"]
    for target in targets:
        # 适配手机终端的 ping 命令 count 参数
        response = os.system(f"ping -c 3 {target} > /dev/null 2>&1")
        if response == 0:
            print(f"✅ 连通 {target} 正常")
        else:
            print(f"❌ 连通 {target} 失败，请检查代理或网络")

def get_public_ip():
    print("\n🌍 正在获取当前外网 IP...")
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        if response.status_code == 200:
            ip = response.json().get("ip")
            print(f"🚀 当前外网 IP 编录: {ip}")
    except Exception as e:
        print("⚠️ 无法获取外网 IP，可能需要科学上网环境。")

if __name__ == "__main__":
    print("=== 个人百宝箱工具启动 ===")
    check_network()
    get_public_ip()
    print("=========================")

import subprocess
import os


def push_to_github(repo_path, commit_message, remote_url):
    try:
        # 初始化 Git 仓库（如果尚未初始化）
        subprocess.run(["git", "init"], cwd=repo_path, check=True)
        # 打印 Git 仓库状态
        subprocess.run(["git", "status"], cwd=repo_path, check=True)
        # 添加所有文件
        subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
        # 再次打印 Git 仓库状态
        subprocess.run(["git", "status"], cwd=repo_path, check=True)
        # 提交更改
        subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)
        # 检查是否已经存在远程仓库
        result = subprocess.run(["git", "remote", "-v"], cwd=repo_path, stdout=subprocess.PIPE, text=True)
        if "origin" not in result.stdout:
            # 添加远程仓库，使用 SSH 格式的 URL
            remote_url = "git@github.com:Fat-Jerry/Fat-Jerry.git"
            subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=repo_path, check=True)
        else:
            print("Remote 'origin' already exists.")
        # 推送至远程仓库
        subprocess.run(["git", "push", "-u", "origin", "master"], cwd=repo_path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    # 项目路径，根据实际情况修改
    repo_path = "G:/测试工具/pythonProject"
    # 提交信息，根据实际情况修改
    commit_message = "Initial commit"
    # GitHub 远程仓库的 URL，根据实际情况修改
    remote_url = "git@github.com:Fat-Jerry/Fat-Jerry.git"
    push_to_github(repo_path, commit_message, remote_url)
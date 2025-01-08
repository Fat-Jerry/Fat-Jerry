import subprocess
import os


def push_to_github(repo_path, commit_message, remote_url):
    try:
        # 创建.gitignore 文件，添加不需要被 Git 管理的文件或目录
        with open(os.path.join(repo_path, ".gitignore"), "w") as f:
            f.write("System Volume Information/\n")
        # 初始化 Git 仓库
        subprocess.run(["git", "init"], cwd=repo_path, check=True)
        # 添加所有文件
        subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
        # 提交更改
        subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)
        # 添加远程仓库
        subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=repo_path, check=True)
        # 推送至远程仓库
        subprocess.run(["git", "push", "-u", "origin", "master"], cwd=repo_path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    # 项目路径，根据实际情况修改
    repo_path = "G:\测试工具\pythonProject"
    # 提交信息，根据实际情况修改
    commit_message = "Initial commit"
    # GitHub 远程仓库的 URL，根据实际情况修改
    remote_url = "https://github.com/Fat-Jerry/Fat-Jerry.git"
    push_to_github(repo_path, commit_message, remote_url)


# github 上传本地文件的流程；
# 首先是安装git
# sudo apt-get install git
# ssh-keygen -t rsa -C "yours@qq.com"
# git config --global user.name "DAVEZJ"
# git config --global user.email "your@qq.com"
# ssh -T git@github.com

# 初始化
# git init
# git add .
# git commit -m "frist commit"
# 在github上创建一个仓库
# git remote rm origin # 清空当前远程origin
# git remote add origin https://github.com:你的账号名/你刚才新建的仓库名.git
# git push -u origin master #可能失败可以使用下面的
# git push -u origin +master #这是强制push
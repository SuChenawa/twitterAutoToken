# twitterAutoToken
Auto get twitter guest token
1. Frok本仓库。
2. 将/github/workflows/get_token.yml中的第8、9行取消注释。
3. 将第48行的your email-address改成自己的github注册邮箱。
4. 将第49行的your username改成自己的用户名。
5. 在Actions处启用本仓库的actions功能。
6. 可以手动执行一次，看能否成功获取到token。token位于/guest/token.json
7. 最后添入config.json的api地址为：https://raw.githubusercontent.com/你的github用户名/twitterAutoToken/main/guest/token.json

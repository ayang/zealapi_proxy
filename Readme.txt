一个go.zealdocs.org的代理

go.zealdocs.org是一个zeal docsets下载的中间服务，不储存docsets,只是通过302跳转到实际的docsets地址。
但是跳转的地址会出现打不开的情况，导致文档不能下载。比如tokyo.kapeli.com最近是连不上的，我们需要把跳转修改到其他镜像地址，如sanfrancisco.kapeli.com。

运行

需要安装requests, flask两个库，然后运行

flask --app main run

zeal自身也得修改，将下载地址指向本服务。
下载zeal源代码，将src/libs/ui/docsetsdialog.cpp 60行改动：

constexpr char RedirectServerUrl[] = "https://go.zealdocs.org/d/%1/%2/latest";
改为
constexpr char RedirectServerUrl[] = "http://localhost:5000/d/%1/%2/latest";

然后按照zeal文档编译zeal并运行就可以正确下载文档了。
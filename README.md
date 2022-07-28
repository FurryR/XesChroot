# XesChroot - 学而思上的chroot容器

这是一个简单的，运行在学而思上的 `chroot` 容器。你可以用它来干几乎任何事情，就像在 `proot` 容器里那样。

## 怎么用？

用法十分简单：您只需指定一个镜像链接，然后编写一段脚本就可以了！

一旦在 `XesChroot.py` 里指定了这些内容，直接运行就能得到一个临时 `chroot` 容器。

**注意：不考虑持久化存储。学而思本身的条件使得数据极易泄露，故您不应该在上面存放任何持久数据。**

一旦打开 `XesChroot.py`，您将可以看到 `chrootUrl` 和 `firstRunScript`。

`chrootUrl`：指定为根文件系统的网络地址。只要是 `requests`库支持的协议均可以指定！但是文件类型必须为 `tar.xz`（网络上的后缀名可以改为别的，但下载下来会自动变成 `tar.xz`。）

**建议：您不应当指定一个访问速度太慢的地址，或者让文件系统过大。用户的时间是有限的。**

`firstRunScript`：指定为系统的初始化脚本。在这里尽情发挥你的想象力吧！配合 `busybox` 的 `wget` 组件，您可以轻松访问网络——但在那之前请先设定 `/etc/resolv.conf`。

**建议：初始化脚本应当足够快速，这样用户不会等太久。如果初始化脚本比较慢，可以积极输出进度，让用户有反馈感。**

## 这个项目的优点何在？

**我很自豪地宣布，它是学而思上第一个成功实现 `chroot` 的项目！并且难以被他人模仿。**

而且，这个项目也可以在别的限制不严，且允许访问 `/tmp` 目录的远程编译器上使用。

当然，如果您想写一个别的版本，您可以利用我对[fakechroot](https://github.com/dex4er/fakechroot "Github")的分支：[fakechroot+fakeroot](https://github.com/FurryR/fakechroot "Github")来轻松完成。但是，请别忘记用 `GPL`开源协议开源！

## 我想用学而思的镜像加速，怎么做？

实际上用到了学而思网站项目存文件的原理。请跟随以下步骤做：

1. 新建一个 `Python` 网站项目或 `Python `游戏。
2. 打开开发者工具，并切换到 `Network`。然后过滤除 `Fetch/XHR` 之外的请求。
3. 上传您的文件。
4. 打开您刚刚上传的文件。您将看到有一个新的 `GET` 请求（文件名不一样但是后缀一样）。复制请求的 `URL`，然后你可以用这个 `URL` 获得文件。

## 开源协议、免责声明和抗议

**本项目基于 `AGPLv3` 开源协议。所有基于本项目的开发（包括网络服务）都应以 `AGPLv3` 协议开源。**

**本项目不是学而思官方认可的。对好未来集团造成的一切损失，开发者完全免责。**

**此外，一旦您使用本项目，即代表您自愿承担一切法律责任。**

**本项目开发初衷仅为学习目的用，禁止将此项目用于可能违反用户所在地区法律的用途。**

**呼吁：请开放 `ptraces` 或 `namespaces`！至少让我们可以使用 `proot` 或 `unshare`，这样我们的程序会更多彩，而不是仅仅关注编程助手！**

## 堆积如山的工作、一遍又一遍的训斥、无数次的打回并不能磨灭我们年少时对编程的纯粹热爱。

凌 致。
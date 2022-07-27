import lzma, base64

a = input("输入要压缩的文件名：")
b = input("输入输出的文件名：")
r = ""
counter = 1
with open(a, "rb") as f:
    r = base64.b64encode(lzma.compress(f.read(), preset=9)).decode()
print("Stage 1 completed")
with open(b, "w") as t:
    for i in range(0, len(r)):
        t.write(r[i])
        if counter == 100:
            counter = 0
            t.write("\n")
        counter += 1
print("Stage 2 completed")
print("压缩完成。")

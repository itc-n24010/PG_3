#書き込みモードでオープン(中身は上書きされる)
write_file = open('n24010.txt', 'w')
write_file.write("こんにちは、n24010さん\n")
write_file.close()

print("テキストファイルに保存されました！")
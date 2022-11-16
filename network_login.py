import requests,os,datetime

url = "http://10.10.100.2/0.htm"
header = {
    "Content-Type": "application/x-www-form-urlencoded",
}
data = "DDDDD=19823680253&upass=34611565ccf1cc725a17b6d11fed2711123456782&R1=0&R2=1&para=00&0MKKey=123456&v6ip="

stream = open(f"{os.getcwd()}/network_login.log", "a")
errorCount = 0
while True:
    try:
        if errorCount >= 10:
            stream.writelines(f"[ERROR] {datetime.datetime.now()} Connection failed :)\n")
            stream.close()
            break
        response = requests.post(url, data, headers=header, timeout=5)
        if response.ok:
            stream.writelines(f"[INFO] {datetime.datetime.now()} Connection Success :)\n")
            stream.close()
            break
    except:
        errorCount += 1
        stream.writelines(f"[WARN] {datetime.datetime.now()} Connection retrying {errorCount} :(\n")
        continue

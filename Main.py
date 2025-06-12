import requests

# === Cấu hình (bạn cần thay bằng dữ liệu thật) ===
access_token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6Im9ubFYwTnBrTnQwMmZzZkRoeFNtYjlLMDdsZlBpbVZWRjFvSS1hTERZQ2siLCJhbGciOiJSUzI1NiIsIng1dCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSIsImtpZCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yZGZmMDlhYy0yYjNiLTQxODItOTk1My0yYjU0OGUwZDBiMzkvIiwiaWF0IjoxNzQ5MTQ1NDc4LCJuYmYiOjE3NDkxNDU0NzgsImV4cCI6MTc0OTE0OTM3OCwiYWlvIjoiazJSZ1lOaktubWJTcWZsMWE0bkE1a0tuQ1p2S0FRPT0iLCJhcHBfZGlzcGxheW5hbWUiOiJBcHBVcGxvYWRTaGFyZVBvaW50IiwiYXBwaWQiOiJhMGIwMTE5ZC0wYmRlLTQ3NDYtYTVjMi0yZjhhZjA5MjNlY2EiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yZGZmMDlhYy0yYjNiLTQxODItOTk1My0yYjU0OGUwZDBiMzkvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiJiMzI2YTYzNi00MDZjLTQ5OWItYWM3YS0yZTg0NjdjOGQzNzIiLCJyaCI6IjEuQVZRQXJBbl9MVHNyZ2tHWlV5dFVqZzBMT1FNQUFBQUFBQUFBd0FBQUFBQUFBQUNpQUFCVUFBLiIsInN1YiI6ImIzMjZhNjM2LTQwNmMtNDk5Yi1hYzdhLTJlODQ2N2M4ZDM3MiIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJBUyIsInRpZCI6IjJkZmYwOWFjLTJiM2ItNDE4Mi05OTUzLTJiNTQ4ZTBkMGIzOSIsInV0aSI6IlBHQlVpeEJOVmttNWVZR3hsUUk5QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjA5OTdhMWQwLTBkMWQtNGFjYi1iNDA4LWQ1Y2E3MzEyMWU5MCJdLCJ4bXNfZnRkIjoiREZ2cWZrcEdVRWNseXFBeXBVNFZqY3MxN1lnaXhULUdNRVQ3V0Q0OFVWMEJhMjl5WldGemIzVjBhQzFrYzIxeiIsInhtc19pZHJlbCI6IjcgOCIsInhtc19yZCI6IjAuNDJMbFlCSmlEQkVTNFdBWEV0aGhQalZ4ei1WdGJ2dUNrb0o3OGxlM0FrVTVoUVNZWXVQMVprNVhjMXYwU1hDeVNPaUNKVUJSRGlFQlpnWUlPQUNsQVEiLCJ4bXNfdGNkdCI6MTM4NDA3NDAzNH0.P9qXzVh8azVppdgQWtx31PpPqoXuDM5k4ESUxhKigde9eOYz26RQYxtsddnRcuEgr3kpJuVj-N3WViyWIT60SCeBmsKQ78AV36oDVWmCeKhNPTREva5Q_H5HJRdnnshvUhsULacbruRiJL6ji-AXBcXxZilPf6Gn5bSI2xMFwTkPeLs0-FFY8P8Q4IXRvCWN5G9Bxfy7lS5PWpmerAxAiy4J8PmzwlzXkY2BO28DQNAiyi-qNIiG29vndVfbixS1M40VMpPVrWVVbSK1PvP1mK3wFgd0Qq1TMnJ9c7pU5D4Vim9AJPsuEvnCusbKBl3EWOhPuABxa7jxQsN9ERwghA'  # Dán token vào đây
site_id = 'uithcm.sharepoint.com,822c0867-8acd-4deb-8a72-5621eec2f4e7,ee52b1f0-e0c4-44f2-a107-45cb899518a0'  # Site ID đã lấy được
drive_id = 'b!Zwgsgs2K602KclYh7sL05_CxUu7E4PJEoQdFy4mVGKDk2CUrGI04Qq90aup_LZF7'  # Drive ID của thư mục Shared Documents

# === Thông tin file cần upload ===
local_file_path = 'hello.txt'        # File local
upload_to_path = 'Shared Document/hello.txt'  # Thư mục trên SharePoint

def upload_file_to_sharepoint():
    with open(local_file_path, 'rb') as f:
        file_content = f.read()

    url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root:/{upload_to_path}:/content"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/octet-stream"
    }

    response = requests.put(url, headers=headers, data=file_content)

    if response.status_code in [200, 201]:
        print("✅ Upload thành công!")
        print("📄 File URL:", response.json().get("webUrl"))
    else:
        print("❌ Lỗi khi upload:")
        print(response.status_code)
        print(response.text)

if __name__ == "__main__":
    upload_file_to_sharepoint()

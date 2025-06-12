import os
import requests
from msal import ConfidentialClientApplication

# ======= CẤU HÌNH ========
client_id = "a0b0119d-0bde-4746-a5c2-2f8af0923eca"
tenant_id = "2dff09ac-2b3b-4182-9953-2b548e0d0b39"
client_secret = "nUY8Q~n2UYbRWDwYAI1dXYQIx.mucKjiBgH2Gcqh"

file_path = r"D:\SourceCode\Python\Hello.txt"  # File cần upload
upload_file_name = os.path.basename(file_path)

# SharePoint Site
site_url = "https://graph.microsoft.com/v1.0/sites/uithcm.sharepoint.com:/sites/LearnSharePoint"


# =========================

def get_access_token():
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    scope = ["https://graph.microsoft.com/.default"]

    app = ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret
    )

    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception("Could not obtain access token", result)

def get_drive_id(token, site_url):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(site_url, headers=headers)
    response.raise_for_status()
    site_id = response.json()["id"]
    print (site_id)
    drive_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drive"
    drive_resp = requests.get(drive_url, headers=headers)
    drive_resp.raise_for_status()
    return drive_resp.json()["id"]

def upload_file(token, drive_id, file_path, file_name):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "text/plain"
    }

    upload_url = f"https://graph.microsoft.com/v1.0/drives/{drive_id}/root:/{file_name}:/content"

    with open(file_path, "rb") as f:
        data = f.read()

    response = requests.put(upload_url, headers=headers, data=data)
    response.raise_for_status()
    print("✅ Upload thành công:", response.json()["webUrl"])

if __name__ == "__main__":
    try:
        print("🔑 Lấy token...")
        token = get_access_token()

       
        print("📂 Lấy drive_id...")
        #drive_id = get_drive_id(token, site_url)
        drive_id = "b!Zwgsgs2K602KclYh7sL05_CxUu7E4PJEoQdFy4mVGKDk2CUrGI04Qq90aup_LZF7"
        print(drive_id)


        print("⬆️ Upload file lên SharePoint...")
        upload_file(token, drive_id, file_path, upload_file_name)

    except Exception as e:
        print("❌ Lỗi:", e)

import requests
from Authorization import Authorization # Authorization.py에서 Authorization 클래스 임포트


# --- API 및 인증 정보 ---
API_URL = ""
API_KEY_STR = ""  # 문자열 형태의 API Key
API_SECRET_HEX_STR = "" # 16진수 문자열 형태의 API Secret


# --- 4. API 요청 및 응답 처리 ---

print("------------------")
print("1.엘리베이터 부르기")
print("2.로봇 탑승 상태 전송")


while True:
    choice = input("원하는작업을 선택하세요")

    if choice != "1" and choice != "2":
        print("잘못된 선택입니다. 1 또는 2를 입력하세요.")
        continue

    if choice == "1":
        try:
            res = requests.post(API_URL, headers=API_HEADER, json=API_BODY, timeout=10)

            print(f"\n--- 엘리베이터를 부릅니다")
            print(f"Status Code: {res.status_code}")

            if res.text:
                print("Response Body:")
                try:
                    response_json = res.json()
                    print(response_json)
                    if res.status_code != 200 and "message" in response_json: # 실패 메시지 추가 확인
                        print(f"Server Error Message: {response_json.get('message')} (Code: {response_json.get('code')})")
                except requests.exceptions.JSONDecodeError:
                    print(res.text)
            else:
                print("Response Body: (No content)")

            if 200 <= res.status_code < 300:
                print("\nAPI call successful!")

            else:
                print(f"\nAPI call failed or returned a non-success status.")

        except requests.exceptions.Timeout:
            print("\nAPI call failed: Request timed out.")
            exit(1)
        except requests.exceptions.RequestException as e:
            print(f"\nAPI call failed due to a RequestException: {e}")
            exit(1)




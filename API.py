import requests
from Authorization import Authorization # Authorization.py에서 Authorization 클래스 임포트
from Robot import Robot # Robot.py에서 Robot 클래스 임포트

# --- API 및 인증 정보 ---
API_URL = ""
API_KEY_STR = ""  # 문자열 형태의 API Key
API_SECRET_HEX_STR = "" # 16진수 문자열 형태의 API Secret

# --- 4. API 요청 및 응답 처리 ---
Robot = Robot(API_KEY_STR, API_SECRET_HEX_STR)

message_id = ""  # 예시 메시지 ID   
serviceStatus = ""
call = {'elId': 'E999999937', 
        'mode': 'auto',
        'currentFloor': '2',
        'direction': 'up',
        'doorStatus': 'close',
        'registedUpHallCall': '1',
        'registedDnHallCall': '',
        'registedCarCall': '',
        'messageId': '8dc999e2a5b742e08469566a6fcd4049151013',
        'thingInfo': '',
        'serviceStatus': 'sourceFloorCallConfirmed'}
while True:
    print("------------------------------")
    print("현대 엘리베이터 Tings API 연동")
    print("------------------------------")
    print("  1.엘리베이터 부르기")
    print("  2.로봇 탑승 상태 전송")
    print("------------------------------")
    print("  3.엘리베이터 부르기 취소")
    print("  4.연동 엘리베이터 상태 조회")
    print("------------------------------")
    print("  0.프로그램종료")

    choice = input("원하는작업을 선택하세요")

    if choice == "0" :
        print("프로그램을 종료합니다.")
        break

    if choice != "1" and choice != "2" and choice != "3" and choice!="4" and choice != "0": 
        print("잘못된 선택입니다. 1 또는 2를 입력하세요.")
        continue

    if choice == "1":
        try:
            destination_floor = input("목적 층을 입력하세요 (예: 1, 2, 3): ")
            res =Robot.elevator_call(line_id="L99999937", destination_floor=destination_floor)

            print(f"\n--- 엘리베이터를 부릅니다")
            print(f"Status Code: {res.status_code}")

            if res.text:
                print("Response Body:")
                try:
                    response_json = res.json()
                    print(response_json)
                    messageid= response_json.get("messageId", "No messageId in response")
                    serviceStatus = response_json.get("serviceStatus", "No serviceStatus in response")
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

    if choice == "2":
        if not message_id:
            print("먼저 엘리베이터를 호출한 후에 로봇 상태를 전송하세요.")
            continue
        
        try:
            res = Robot.robot_status_sender(message_id, serviceStatus)
        
            print(f"\n--- 로봇의 상태를 전송합니다")
            print(f"Status Code: {res.status_code}")
            print(f"message ID: {message_id}")
            print(f"service Status: {serviceStatus}")
            print(f"\n--- 로봇의 상태를 전송합니다")
            print()

        except requests.exceptions.HTTPError as e:
            print(f"\nAPI call failed: HTTP error occurred: {e}")


        if 200 <= res.status_code < 300:
            print("\nAPI call successful!")

        else:
            print(f"\nAPI call failed or returned a non-success status.")

    if choice == "3" : 
        try:
            res = Robot.elevator_call_cancel(message_id=message_id)
            print(f"\n--- 엘리베이터 호출을 취소합니다")
            print(res.json()) 
        except requests.exceptions.RequestException as e:
            print(f"API call failed: {e}")
            exit(1)
        except requests.exceptions.Timeout:
            print("Request timed out.")
            exit(1)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error : {e}")
            exit(1)

    if choice =="4":
        try:
            res = Robot.get_elevator_status(message_id=message_id)
            print(f"\n--- 엘리베이터 상태를 조회합니다")
            print(f"Status Code: {res.status_code}")
            if res.text:
                print("Response Body:")
                try:
                    response_json = res.json()
                    print(response_json)
                except requests.exceptions.JSONDecodeError:
                    print(res.text)
            else:
                print("Response Body: (No content)")

        except requests.exceptions.RequestException as e:
            print(f"API call failed: {e}")
            exit(1)
        except requests.exceptions.Timeout:
            print("Request timed out.")
            exit(1)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error : {e}")
            exit(1)
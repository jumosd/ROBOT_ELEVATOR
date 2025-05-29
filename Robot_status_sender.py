

class RobotStatusSender:
    """
    - EL-Thing 서비스 연동 상태(현재 단계)
    - sourceFloorWaiting : Thing의 EL 탑승 전 대기 상태
    - sourceFloorGettingOn : Thing의 EL 탑승 중 상태
    - sourceFloorGotOn : Thing의 EL 탑승 완료 상태
    - destinationFloorGettingOff : Thing의 EL 하차 중 상태
    - destinationFloorGotOff : Thing의 EL 하차 완료 상태
    - destinationFloorGetOffReject : Thing의 EL 하차 보류
    """
    endpoint = "/api/v1/el/call/thing/messageid/{messageid}/status/{robot_status}"

    def __init__(self, messageid, robot_status):
        self.messageid = messageid
        self.robot_status = robot_status

    def send_status(self):
        # Simulate sending the status to a server or logging system
        print(f"Robot ID: {self.messageid}, Status: {self.robot_status}")
from signIn import check_and_sign, get_user_info
import time
from api import duration

for i in range(0,duration*12):
    current_time = time.strftime("%m-%d %H:%M:%S", time.localtime())
    print(current_time)
    if check_and_sign():
        print("签到成功")
        break
    time.sleep(5)
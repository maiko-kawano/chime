import schedule
import time
from datetime import datetime
from playsound import playsound

# 音楽を再生するタスク
def play_music():
    print(f"アラームを再生します {datetime.now().strftime('%H:%M:%S')}")
    try:
        playsound("chime.mp3")
    except Exception as e:
        print(f"音楽再生エラー: {e}")

# 平日（MondayからFriday）の特定の時刻に音楽を再生
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
times = ["10:00", "10:50", "11:00", "12:00", "13:00", "13:50", "14:00", "14:50", "15:00"]

START_TIME = "9:59"
END_TIME = "15:01"

# 平日の各時刻にスケジュールを設定
for day in weekdays:
    for t in times:
        getattr(schedule.every(), day).at(t).do(play_music)

# スケジュールを実行
while True:
    now = datetime.now().strftime("%H:%M")
    if START_TIME <= now < END_TIME:
        schedule.run_pending()  
        time.sleep(1)
    elif now >= END_TIME:
        print("本日の訓練は終了です")
        break
    else:
        schedule.run_pending()
        time.sleep(1)

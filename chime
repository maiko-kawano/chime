import schedule
import time
from playsound import playsound

def play_music():
    # 音楽ファイルのパスを指定して音楽を再生
    playsound("chime.mp3")

# 平日（MondayからFriday）に共通の時刻で音楽を再生する
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
times = ["10:50", "11:00", "12:00", "13:00", "13:50", "14:00", "14:50"]

# 平日の各時刻に音楽を再生するスケジュールを設定
for day in weekdays:
    for t in times:
        getattr(schedule.every(), day).at(t).do(play_music)


# 無限ループでスケジュールを確認し続ける
while True:
    schedule.run_pending()
    time.sleep(1)

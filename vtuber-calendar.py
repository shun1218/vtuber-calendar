import datetime

from youtube_info import YoutubeInfo
from vtuber import Vtuber
from upcoming_event import UpcomingEvent

if __name__ == '__main__':
    vtubers = Vtuber().find_all()
    for vtuber in vtubers:
<<<<<<< HEAD
        updated_time = YoutubeInfo(vtuber.updated_at).get_info(vtuber)
=======
        updated_time = YoutubeInfo().get_info(vtuber)
>>>>>>> origin/master
        # 時間変換
        vtuber.updated_at = updated_time.strftime('%Y-%m-%d %H:%M:%S')
        Vtuber().update(vtuber)
        # 放送を取り止めたスケジュール削除
        upcoming_events = UpcomingEvent().find_by_vtuber_id(vtuber.vtuber_id)
        for upcoming_event in upcoming_events:
<<<<<<< HEAD
            YoutubeInfo(vtuber.updated_at).check_video(vtuber.calendar_id, upcoming_event.event_id, upcoming_event.video_id)
=======
            YoutubeInfo().check_video(vtuber.calendar_id, upcoming_event.event_id, upcoming_event.video_id)
>>>>>>> origin/master

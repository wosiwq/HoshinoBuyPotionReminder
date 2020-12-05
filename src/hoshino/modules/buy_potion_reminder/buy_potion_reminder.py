import pytz
import random
from datetime import datetime
from hoshino import Service, R

sv = Service('buy_potion_reminder', enable_on_default=False, help_='买药提醒')


@sv.scheduled_job('cron', hour='*/6')
async def hour_call():
    pic = R.img(f"BuyPotion{random.randint(1, 3)}.jpg").cqcode
    msg = f'骑士君，该上线买经验药水啦~\n{pic}'
    await sv.broadcast(msg, 'buy_potion_reminder')

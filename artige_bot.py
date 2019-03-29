#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import psutil
from instabot_py import InstaBot
from pympler import asizeof

InstaBot.log_file_path = 'archive/'
bot = InstaBot(
    login="",  # Enter username (lowercase). Do not enter email!
    password="", like_per_day=2000,
    comments_per_day=0,
    tag_list=['اثر_هنری', 'نوروز', 'تابلو_خط', 'تابلوخط', 'تزیینات_چوبی', 'خطاطی', 'خطنقاشی', 'خوشنویسی', 'دیوارکوب', 'زیرلعابی', 'ساعت_دیواری', 'سفال', 'سفالگری', 'سینی', 'سینی_چوبی', 'صنایع_دستی', 'صنایع_چوب', 'صنایع_چوبی', 'صنایعدستی', 'صنایعدستیایران', 'ظرف_پذیرایی', 'ظرف_پذیرایی_خاص', 'ظرف_چوبي_خاص', 'ظرف_چوبی', 'ظروف_سفالی', 'ظروف_سفالی_تزئینی', 'ظروف_سفالی_رنگی', 'مبلمان', 'مبلمان_خاص', 'مبلمان_دست_ساز', 'مبلمان_چوبی', 'نقاشی', 'نقاشیخط', 'نوروز', 'هفتسین', 'هنر_دست', 'هنر_چوب', 'هنروخلاقیت', 'هنرچوب', 'پریشان_نویسی', 'پریشاننویسی', 'چوبی_تزئینی', 'گلدان', 'گلدان_خاص', 'گلدان_چوبی', 
        ],
    tag_blacklist=["rain", "thunderstorm",'fallower','فالوور','فالور', 'f4f', 'دزرتاریوم', 'دخترانه', 'ساعت_جیشاک', 'ورق_طلا', 'فست_فود', 'استیک', 'دیش_گاردن', 'لاکچری', 'جیشاک', 'پسرانه', 'سقف_کاذب', 'نیوشادرینکس', 'موسسه', 'ساختمان_لوکس_تهران', 'غذای_جدید', 'فشن_شو', 'علوم', 'vivarium', 'استخر', 'معلم', 'غذای_کم_کالری', 'آشپز', 'هتل', 'سوشی', 'مدرسه_غیرانتفاعی_تمام_هوشمند_دخترانه_نگرش', 'دانش_آموز', 'تراریوم', 'زنگ', 'سالاد', 'مرغ', 'casio_g_shock', 'دسر', 'زیست_محیطی', 'غذا', 'نیوشا', 'هوای_پاک', 'هفته_مد', 'نیوشانیک', 'g_shock', 'نئوکلاسیک', 'casio', 'تالار', 'فشن', 'لاکچری_لایف', 'فضا', 'نمای_کلاسیک', 'terrarium', 'روز_ودر', 'گوشت', 'سلبریتی', 'ویواریوم', 'نوشیدنی_های_کمک_سلامت_نیوشا', 'رابیتس', 'جنیفر_لوپز', 'غذای_رژیمی', 'لکسوس', 'بیمارستان', 'تورکیش', 'جراحی', 'سانتافه', 'دندانپزشکی_زیبایی', 'تور_ارزان', 'بنز', 'دکتر', 'داروخانه', 'تجهیزات_پزشکی', 'هیوندای', 'موبایل_فروشی', 'برنج', 'تور', 'پرادو', 'لامبورگینی', 'تویوتا', 'مبلماناداری', 'مبلمان_مدرن_ادوا', 'كابينتكلاسيك', 'lamello', 'مبلمان_لوکس', 'كابينت_هايگلاس', 'مبلمان_اداري', 'مبلماناداري', 'azartel', 
            ],
    user_blacklist={},
    max_like_for_one_tag=500,
    follow_per_day =200,
    follow_time= 6,
    unfollow_per_day=1000,
    unlike_per_day=0,
    unfollow_recent_feed= False, #True,
    # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
    time_till_unlike= None , #3 * 24 * 60 * 60,  # 3 days
    unfollow_break_min=15,
    unfollow_break_max=30,
    user_max_follow=10000,
    # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
    user_min_follow=10,
    log_mod=1,
    proxy="", # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[],
#        ["this", "the", "your"],
#        ["photo", "picture", "pic", "shot"],
#        ["is", "looks", "is 👉", "is really"],
#        [
#            "great", #            "super", #            "good", #            "very good", #            "good", #            "wow", #            "WOW", #            "cool", #            "GREAT", #            "magnificent", #            "magical", #            "very cool", #            "stylish", #            "beautiful", #            "so beautiful", #            "so stylish", #            "so professional", ##            "lovely", #            "so lovely", #            "very lovely", #            "glorious", #            "so glorious", #            "very glorious", #            "adorable", #            "excellent", #            "amazing", #        ],
#        [".", "🙌", "... 👏", "!", "! 😍", "😎"],
#    ],
    # Use unwanted_username_list to block usernames containing a string
    # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    # 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        "second", "stuff", "project", "free", "keren", "indo", "sex", "toko", "jual", "murah", "jam", "kaos", "case", "baju", "corp", "tas", "grosir", "karpet", "sosis", "salon", "skin", "care", "tech", "rental", "beauty", "express", "kredit", "collection", "impor", "preloved", "follow", "follower", "gain", ".id", "_id", "bags",   
        ],
    unfollow_whitelist=["example_user_1", "example_user_2"],
    # Enable the following to schedule the bot. Uses 24H
    end_at_h = 2, # Hour you want the bot to stop
    end_at_m = 00, # Minute you want the bot stop, in this example 23:30
    start_at_h = 7, # Hour you want the bot to start
    start_at_m = 30, # Minute you want the bot to start, in this example 9:10 (am).
    unfollow_not_following=True,
    unfollow_inactive=False, #True,
    unfollow_probably_fake=True, #False,
    unfollow_selebgram=False,
    )

# enforce firefox 65 on ubuntu user_agent string
bot.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
pid = os.getpid()
py = psutil.Process(pid)
def write_log_tweak(bot, turn):
    import types
    import logging
    fh = logging.FileHandler('./machine.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    _logger = logging.getLogger('artige bot')
    _logger.addHandler(fh)
    
    bot_log = bot.write_log
    n = 0
    def mem_check_wrapper(self, log_text):
        nonlocal n
        bot_log(log_text)
        if n % turn == 0:
            _logger.debug('============= Run   %d =======', n)
            _logger.debug('CPU%%      \t%s', psutil.cpu_percent())
            _logger.debug('CPU times  \t %s', psutil.cpu_times())
            _logger.debug('cpu_count  \t%s', psutil.cpu_count())
            _logger.debug('CPU stats  \t%s', psutil.cpu_stats())
            _logger.debug('CPU Freq   \t %s', psutil.cpu_freq())
            _logger.debug('bot size   \t%s MB', asizeof.asizeof(bot) /2.**20)
            _logger.debug('memoryUse  \t%s MB', py.memory_info()[0]/2.**20)
            _logger.debug('VM         \t%s', psutil.virtual_memory()._asdict())
        n += 1
    
    bot.write_log = types.MethodType(mem_check_wrapper, bot)

write_log_tweak(bot, 1000)

while True:
    bot.mainloop()


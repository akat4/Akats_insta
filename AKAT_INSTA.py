import instaloader
import os
import time
import pyfiglet 
os.system("pip install pyfiglet")
A = "\033[1;91m"  #احمر
B = "\033[1;90m" #ابيض ضعيف 
C = "\033[1;97m" #ابيض
E = "\033[1;92m"  #اخضر
H = "\033[1;93m" #اصفر
L = "\033[1;95m" #وردي
M = "\033[1;94m" #ازرك
i = "_"
print(H+pyfiglet.figlet_format("By\nSFAH", font="slant"))
print("By SFAH")
print("I named this tool after my girlfriend Claire")
print("\033[1;95mI named this tool after my girlfriend Claire")
# استخراج مسار ملف المستخدم وكلمة المرور
credentials_file = 'credentials.txt'  # حدد مسار الملف هنا

with open(credentials_file, 'r') as file:
    lines = file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

# تسجيل الدخول إلى حساب Instagram
L = instaloader.Instaloader()
L.context.log('Logging in...')
L.login(username, password)

# المستخدم المستهدف
target_username = 'arig.2022'

# إنشاء مجلد لتخزين الصور المستهدفة
if not os.path.isdir(target_username):
    os.mkdir(target_username)

# تحميل معلومات الحساب المستهدف
profile = instaloader.Profile.from_username(L.context, target_username)

# التسميات التوضيحية للصور المستهدفة
captions = []
for post in profile.get_posts():
    captions.extend(post.caption_hashtags)
    time.sleep(2)
print('Captions:')
print(captions)

# التعليقات للمنشورات المستهدفة
comments = []
for post in profile.get_posts():
    post_comments = post.get_comments()
    for comment in post_comments:
        comments.append(comment.text)
        time.sleep(2)
print('Comments:')
print(comments)

# عدد المتابعين
followers = []
for follower in profile.get_followers():
    followers.append(follower.username)
    time.sleep(2)
print('Followers:')
print(followers)

# المتابعون
followees = []
for followee in profile.get_followees():
    followees.append(followee.username)
    time.sleep(2)
print('Followees:')
print(followees)

# البريد الإلكتروني للمتابعين المستهدفين
fwers_emails = []
for follower in profile.get_followers():
    try:
        follower_info = L.get_user_info(follower.username)
        if follower_info.email is not None:
            fwers_emails.append(follower_info.email)
    except:
        pass
    time.sleep(2)
print('Followers emails:')
print(fwers_emails)

# البريد الإلكتروني للمستخدمين المتابعين بالهدف
fwings_emails = []
for followee in profile.get_followees():
    try:
        followee_info = L.get_user_info(followee.username)
        if followee_info.email is not None:
            fwings_emails.append(followee_info.email)
    except:
        pass
    time.sleep(2)
print('Followees emails:')
print(fwings_emails)

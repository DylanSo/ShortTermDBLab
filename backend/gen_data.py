from faker import Faker
import random

course_list = []

fake = Faker("zh-CN")

dept = {
    '01': '计算机学院'
}
computer_major = {
    '01': '嵌入式系统',
    '02': '计算机科学与技术'
}
major_no = ['01', '02']
class_list = ['01', '02']
m1_class_persons_sum = [0, 0]
m2_class_persons_sum = [0, 0]
sex_list = ['男', '女']
title_list = ['讲师', '副教授', '教授']
if_graduate = ['在读', '已毕业']
source_addr_list = ['浙江杭州', '浙江丽水', '上海', '北京', '山西运城', '山东青岛',
                    '广东广州', '江苏苏州', '江苏南京', '浙江温州', '浙江台州', '浙江宁波',
                    '福建福州', '湖南长沙', '湖北武汉']


# 生成随机地址
def source_addr():
    return random.sample(source_addr_list, 1)[0]


# 生成随机性别
def sex():
    return random.sample(sex_list, 1)[0]


# 生成随机职称
def title():
    return random.sample(title_list, 1)[0]


# 生成随机班级
def g_class():
    return random.sample(class_list, 1)[0]


def major():
    return random.sample(major_no, 1)[0]


def g_num(num):
    if int(num / 10) == 0:
        return '0' + str(num)
    return str(num)


# 生成随机邮箱
def generate_random_email():
    # 用数字0-9 和字母a-z 生成随机邮箱。
    list_sum = [j for j in range(10)] + ["a", "b", "c", "d", "e", "f", "g", "h", 'i', "j", "k",
                                         "l", "M", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                                         "w", "x", "y", "z"]
    email_str = ""
    email_suffix = ["@163.com", "@qq.com", "@gmail.com", "@mail.hk.com", "@yahoo.co.id", "@outlook.com"]
    for j in range(5):
        a = str(random.choice(list_sum))
        email_str = email_str + a

    # 随机拼接不同的邮箱后缀
    return email_str + random.choice(email_suffix)


# gen_teacher
def gen_teacher():
    teacher_list = []
    for i in range(5):
        # 使用Faker库生成假数据,将其转为字典格式,方便插入数据库
        t_no = ['T0001', 'T0002', 'T0003', 'T0004', 'T0005']
        ctx = {
            't_no': t_no[i],
            't_name': fake.name(),
            't_dept': 'D01',
            't_sex': sex(),
            't_age': fake.random_int(30, 60),
            't_title': title(),
            't_phone': fake.phone_number(),
            't_email': generate_random_email(),
            't_password': '123456'
            # 't_password': fake.password(special_chars=False),
        }
        teacher_list.append(ctx)
    return teacher_list


# gen_student
def gen_student():
    student_list = []
    for i in range(100):
        # 使用Faker库生成假数据,将其转为字典格式,方便插入数据库
        ctx = {
            's_no': '',
            's_name': fake.name(),
            's_sex': sex(),
            's_age': fake.random_int(18, 21),
            's_source': source_addr(),
            's_credit': 0,
            's_cno': g_class(),
            's_mno': major(),
            's_password': '123456',
            's_ifGraduate': '在读'
        }
        student_list.append(ctx)

    # count students' number
    for index in range(len(student_list)):
        if student_list[index]['s_mno'] == '01':
            if student_list[index]['s_cno'] == '01':
                m1_class_persons_sum[0] = m1_class_persons_sum[0] + 1
                student_list[index]['s_no'] = 'S2020' + '01' + student_list[index]['s_mno'] + student_list[index][
                    's_cno'] + g_num(m1_class_persons_sum[0])
            else:
                m1_class_persons_sum[1] = m1_class_persons_sum[1] + 1
                student_list[index]['s_no'] = 'S2020' + '01' + student_list[index]['s_mno'] + student_list[index][
                    's_cno'] + g_num(m1_class_persons_sum[1])
        elif student_list[index]['s_mno'] == '02':
            if student_list[index]['s_cno'] == '01':
                m2_class_persons_sum[0] = m2_class_persons_sum[0] + 1
                student_list[index]['s_no'] = 'S2020' + '01' + student_list[index]['s_mno'] + student_list[index][
                    's_cno'] + g_num(m2_class_persons_sum[0])
            else:
                m2_class_persons_sum[1] = m2_class_persons_sum[1] + 1
                student_list[index]['s_no'] = 'S2020' + '01' + student_list[index]['s_mno'] + student_list[index][
                    's_cno'] + g_num(m2_class_persons_sum[1])
        student_list[index]['s_cno'] = 'CLS01' + student_list[index]['s_mno'] + student_list[index]['s_cno']
        student_list[index]['s_mno'] = 'M' + student_list[index]['s_mno']
    return student_list


def save_txt(f_name, save_list):
    with open('D:\\project\\ShortTermDBLab\\backend\\data\\' + f_name + '.txt', 'a',
              encoding='utf-8') as f:  # 使用with open()新建对象f
        for item in save_list:
            st = ''
            for value in item.values():
                st = st + str(value) + ','
            st = st[:-1]
            f.write(st + '\n')  # 写入数据，文件保存在上面指定的目录，加\n为了换行更方便阅读
        f.close()


t_list = gen_teacher()
for index in range(len(t_list)):
    print(t_list[index])
save_txt('teachers', t_list)

stu_list = gen_student()
for index in range(len(stu_list)):
    print(stu_list[index])
save_txt('students', stu_list)

print('嵌入式01人数：', m1_class_persons_sum[0])
print('嵌入式02人数：', m1_class_persons_sum[1])
print('计科01人数：', m2_class_persons_sum[0])
print('计科02人数：', m2_class_persons_sum[1])

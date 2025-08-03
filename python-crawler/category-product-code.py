import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

# 크롤링 대상 카테고리 번호 리스트
t_no_list = [
    742, 743, 744, 745, 746, 747, 749, 753, 754, 755, 757, 761, 764, 766, 769,
    770, 771, 775, 776, 780, 781, 782, 783, 784, 788, 792, 795, 798, 799, 800,
    801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815,
    816, 817, 822, 823, 824, 825, 826, 828, 829, 830, 831, 832, 834, 835, 836,
    837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851,
    852, 853, 854, 855, 856, 857, 858, 859, 861, 862, 863, 864, 865, 866, 867,
    868, 869, 870, 874, 875, 876, 877, 878, 879, 880, 881, 884, 885, 886, 888,
    889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903,
    905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919,
    920, 921, 922, 923, 924, 925, 927, 928, 929, 930, 931, 932, 933, 934, 935,
    937, 953, 959, 988, 989, 999, 1023, 1032, 1033, 1034, 1038, 1039, 1040, 1043,
    1044, 1045, 1055, 1056, 1057, 1058, 1060, 1061, 1064, 1080, 1082, 1083, 1084,
    1085, 1123, 1124, 1125, 1126, 1221, 1222, 1316, 1317, 1318, 1319, 1362, 1598,
    1729, 1755, 1819, 1824, 1827, 1828, 1829, 1841, 1913, 2833
]

base_url = "https://www.lklab.com/product/product_list.asp?t_no="
results = []

# 정규식 패턴: g_no=뒤의 숫자만 추출
g_no_pattern = re.compile(r"g_no=(\d+)")


for t_no in t_no_list:
    url = f"{base_url}{t_no}"
    print(f"[INFO] 카테고리 {t_no} 크롤링 중...")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"  ❌ HTTP 오류: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        # p.thumb > a[href] 탐색
        for p in soup.select("p.thumb a[href]"):
            href = p["href"]
            match = g_no_pattern.search(href)
            if match:
                g_no = match.group(1)
                results.append({"t_no": t_no, "g_no": g_no})

        time.sleep(0.5)  # 서버 과부하 방지

    except Exception as e:
        print(f"  ⚠️ 예외 발생: {e}")
        continue

# 결과를 DataFrame으로 저장
df = pd.DataFrame(results)
df.to_excel("lklab_g_no_list.xlsx", index=False)

print("✅ 크롤링 완료 및 엑셀 저장 완료.")

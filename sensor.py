dist_log = [56, 22, 8, 91, 44, 15, 77]

dist_log.append(-5)


danger_count = 0        # 危险预警总个数
near_count = 0         # 近距离数据总个数
safe_count = 0         # 安全距离总个数
valid_count = 0        # 有效数据个数
error_count = 0        # 异常数据个数
sum_valid = 0          # 有效距离总和


for dis in dist_log:
    # a：打印距离与数据类型
    print(f"当前检测距离：{dis} cm，数据类型：{type(dis)}")

    # b：异常数据判断，小于0直接continue跳过
    if dis < 0:
        error_count += 1
        print("---->传感器数据异常，跳过本条\n")
        continue

    # 走到这里代表是有效数据
    valid_count += 1
    sum_valid += dis

    # c：分级筛选
    if 0 <= dis <= 10:
        status = "危险预警（紧急避让）"
        danger_count += 1
    elif 11 <= dis <= 30:
        status = "近距离（谨慎行驶）"
        near_count += 1
    else:
        status = "安全距离（正常运行）"
        safe_count += 1
    print(f"---->状态描述：{status}\n")

# e：计算平均距离，处理除零
if valid_count > 0:
    avg_dis = sum_valid / valid_count
else:
    avg_dis = 0

# f：格式化汇总输出报告
print("====================传感器数据分析报告====================")
print(f"危险预警数据次数：{danger_count} 次")
print(f"近距离数据次数：{near_count} 次")
print(f"安全数据次数：{safe_count} 次")
print(f"有效数据次数：{valid_count} 次")
print(f"异常数据次数：{error_count} 次")
print(f"本次检测平均距离：{avg_dis:.2f} cm")
print("==========================================================")
total_seconds  = 12345

hours = total_seconds  // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours}시간 {minutes}분 {seconds}초")

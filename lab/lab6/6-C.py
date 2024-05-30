import cv2

# 打开视频文件
video_path = 'People_Counting.avi'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # 获取总帧数，图像的高和宽
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(f'Total frames: {total_frames}, Width: {frame_width}, Height: {frame_height}')
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # 显示原始图像
        cv2.imshow('Original Frame', frame)
        
        # 将图像缩小为原尺寸的1/2并显示
        resized_frame = cv2.resize(frame, (frame_width // 2, frame_height // 2))
        cv2.imshow('Resized Frame', resized_frame)
        
        # 按位取反图像并显示
        inverted_frame = cv2.bitwise_not(frame)
        cv2.imshow('Inverted Frame', inverted_frame)
        
        # 等待30毫秒再捕获键盘输入
        # 如果用户没按 'Esc' 键退出，就循环逐帧播放动画
        if cv2.waitKey(30) & 0xFF == 27:  # 
            break

    cap.release()
    cv2.destroyAllWindows()

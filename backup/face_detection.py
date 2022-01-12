import cv2
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
vs = cv2.VideoCapture(0)
while True:
	ret, frame = vs.read()
	if frame is None:
		break
	faces = faceCascade.detectMultiScale(frame)
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,0), 2)
	cv2.imshow("Video", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q") or key == 27:
		break
cv2.destroyAllWindows()
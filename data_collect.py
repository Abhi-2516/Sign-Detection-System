import cv2
import os

labels = ['Call Me', 'Good Job', 'Hello', 'Looser', 'Power', 'Rock on', 'ThankYou', 'Victory', 'Yes','No']
directory = 'SignImage128x128/'

print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')

for label in labels:
    if not os.path.exists(f'{directory}/{label}'):
        os.mkdir(f'{directory}/{label}')

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    count = {label.lower(): len(os.listdir(os.path.join(directory, label))) for label in labels}
    count['blank'] = len(os.listdir(os.path.join(directory, 'blank')))

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame, (0, 40), (300, 300), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    frame = frame[40:300, 0:300]
    cv2.imshow("ROI", frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (128, 128))
    interrupt = cv2.waitKey(10)

    for label in labels:
        if interrupt & 0xFF == ord(label[0].lower()):
            cv2.imwrite(os.path.join(directory, label, str(count[label.lower()])) + '.jpg', frame)
            break
    else:
        if interrupt & 0xFF == ord('.'):
            cv2.imwrite(os.path.join(directory, 'blank', str(count['blank'])) + '.jpg', frame)

cap.release()
cv2.destroyAllWindows()

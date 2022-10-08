import cv2

def detectar(foto):
    try:
        cascadeRosto = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
        imagem = cv2.imread(foto)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        face = cascadeRosto.detectMultiScale(imagem_cinza)
        return face
        for(x, y, l, a) in face:
            cv2.rectangle(imagem, (x,y), (x + l, y + a), (0, 0, 255), 2)
        cv2.imshow("Faces", imagem)
        cv2.waitKey()
    except cv2.error as error:
        print("Ocorreu um erro")
        print(error)


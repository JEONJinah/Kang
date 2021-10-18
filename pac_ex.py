import numpy as np
import cv2 as cv
import dlib
import face_recognition as fr

if __name__ == '__main__':
    src = fr.load_image_file("woo2.jpg")

    src = cv.cvtColor(src, cv.COLOR_BGR2RGB)

    faces = fr.face_locations(src)

    face_encord = fr.face_encodings(src)[0]
    face_db = []
    face_name = []
    face_db.append(face_encord)
    face_name.append("WOO")


    for face in faces:
        top, right, bottom, left = face
        cv.rectangle(src, (left, top), (right, bottom), (0, 0, 255), thickness=2)


        cv.imshow("woo2", src)

        ##############################
        # 새로운 이미지가 왔을 때 비교

        input_img = fr.load_image_file("woo.jpg")
        input_img = cv.cvtColor(input_img, cv.COLOR_BGR2RGB)
        faces = fr.face_locations(input_img)
        ext_encord = fr.face_encodings(input_img)[0]
        face_dist = fr.face_distance(face_db, ext_encord)
        best_match = np.argmin(face_dist)
        name = face_name[best_match]

        for face in faces:
            top, right, bottom, left = face


            cv.rectangle(input_img, (left, top), (right, bottom), (0, 0, 255), thickness=2)
            font = cv.FONT_HERSHEY_DUPLEX
            cv.putText(input_img, name, (left+6, top+6), font, 3.0, (255, 255, 0), 2)

        cv.imshow("input", input_img)


        cv.waitKey(0)
        cv.destroyAllWindows()


    # src = cv.imread("woo2.jpg")
    #
    # face_det = dlib.get_frontal_face_detector()
    # lm_model = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    # gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    #
    # faces = face_det(gray)
    #
    # for face in faces:
    #     lm = lm_model(src, face)
    #
    #     lm_point = []
    #     for p in lm.parts():
    #         lm_point.append([p.x, p.y])
    #
    #     lm_point = np.array(lm_point)
    #
    #     for p in lm_point:
    #         cv.circle(src, (p[0], p[1]), radius=2, color=(0, 255, 0), thickness=1)
    #
    #     cv.circle(src, (lm_point[36][0], lm_point[36][1]), radius=2, color=(0, 0, 255), thickness=1)
    #     cv.circle(src, (lm_point[33][0], lm_point[33][1]), radius=2, color=(0, 0, 255), thickness=1)
    #     cv.circle(src, (lm_point[45][0], lm_point[45][1]), radius=2, color=(0, 0, 255), thickness=1)
    #
    #
    #     cv.rectangle(src, (face.left(), face.top()), (face.right(), face.bottom()),
    #                  color=(0, 0, 255), thickness=3)
    #
    # cv.imshow("woo2", src)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

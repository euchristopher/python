#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
using namespace cv;

const string ascii_chars = " .:-=+*%@#";

char mapToAscii(int gray_value) {
    int index = gray_value * (ascii_chars.size() - 1) / 255;
    return ascii_chars[index];
}

void displayFrameAsAscii(Mat& frame) {
    // Reduz a imagem para um tamanho menor
    Mat resized;
    Size new_size(frame.cols / 2, frame.rows / 2);  // Reduzindo pela metade
    resize(frame, resized, new_size);
    
    // Converte a imagem para escala de cinza
    Mat gray;
    cvtColor(resized, gray, COLOR_BGR2GRAY);
    
    // Percorre os pixels da imagem em escala de cinza e mapeia para ASCII
    for (int i = 0; i < gray.rows; i++) {
        for (int j = 0; j < gray.cols; j++) {
            int pixel_value = gray.at<uchar>(i, j);
            cout << mapToAscii(pixel_value);
        }
        cout << endl;
    }
}

int main() {
    // Abra o vídeo
    VideoCapture cap("video.mp4");  // Substitua pelo caminho do seu vídeo

    if (!cap.isOpened()) {
        cerr << "Erro ao abrir o arquivo de vídeo." << endl;
        return -1;
    }

    Mat frame;
    while (true) {
        cap >> frame;  // Capture um quadro do vídeo
        if (frame.empty()) {
            break;  // Se não houver mais quadros, saia do loop
        }

        displayFrameAsAscii(frame);

        // Aguarda um tempo para exibir o próximo quadro (ajuste conforme necessário)
        if (waitKey(30) >= 0) {
            break;
        }
        // Limpa a tela para o próximo quadro
        system("CLS");
    }

    return 0;
}

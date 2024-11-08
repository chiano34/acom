import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.*;
public class Main{
    public static double gaussFun(int x,int y,int a,int b,double sigma){
        return 1/(2*Math.PI*sigma*sigma)*Math.exp(-((x-a)*(x-a)+(y-b)*(y-b))/(2*sigma*sigma));
    }
    public static Mat gaussBlur(Mat img, int size, double sigma) {
        // Создание ядра свёртки
        Mat kernel = new Mat(size, size, CvType.CV_64F);
        double sum = 0.0;
        int a= size/2;
        int b = size / 2;
        // Заполнение ядра свёртки значениями Гаусса
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                kernel.put(i, j, gaussFun(i, j,a,b,sigma));
                sum += gaussFun(i, j,a,b,sigma);
            }
        }
        // Нормализация ядра
        kernel.convertTo(kernel, CvType.CV_64F, 1.0 / sum);
        // Результирующее изображение
        Mat result = img.clone();
        int edge=size/2;
        // Применение свёртки
        for (int i = edge; i < img.rows() - edge; i++) {
            for (int j = edge; j <img.cols()-edge; j++) {
                double res = 0.0;
                for (int k = -edge; k <= edge; k++) {
                    for (int l = -edge; l <= edge; l++) {
                        res += img.get(i + k, j + l)[0] * kernel.get(k + edge, l + edge)[0];
                    }
                }
                result.put(i, j, res);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        String inputImagePath = "image.jpg";
        Mat colorImage = Imgcodecs.imread(inputImagePath);
        Mat grayImage = new Mat();
        Imgproc.cvtColor(colorImage, grayImage, Imgproc.COLOR_BGR2GRAY);
        Imgcodecs.imwrite("outpng.jpg", grayImage);
        Mat blurredImage = gaussBlur(grayImage, 5, 1.6);
        Imgcodecs.imwrite("blured.jpg", blurredImage);
    }
}
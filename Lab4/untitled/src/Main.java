import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.*;
import org.opencv.highgui.HighGui;
public class Main{
    public static Mat grayscale(String imagePath,int size,double sigma, double low,double high) {
        Mat img = Imgcodecs.imread(imagePath, Imgcodecs.IMREAD_GRAYSCALE);
        Mat blur = new Mat();
        Imgproc.GaussianBlur(img, blur, new Size(size, size), sigma);
        Mat lengths = new Mat(blur.size(), CvType.CV_64F);
        Mat angles = new Mat(blur.size(), CvType.CV_64F);
        System.out.println(blur.get(0,0)[0])  ;
        for (int x = 1; x < blur.rows() - 1; x++) {
            for (int y = 1; y < blur.cols() - 1; y++) {
                double Gx = blur.get(x + 1, y + 1)[0] - blur.get(x - 1, y - 1)[0] +
                        blur.get(x + 1, y - 1)[0] - blur.get(x - 1, y + 1)[0] +
                        2 * (blur.get(x + 1, y)[0] - blur.get(x - 1, y)[0]);
                double Gy = blur.get(x+1,y+1)[0]
                        -blur.get(x-1,y-1)[0]
                        +blur.get(x-1,y+1)[0]
                        - blur.get(x+1,y-1)[0]
                        +2*(blur.get(x,y+1)[0] -blur.get(x,y-1)[0]);
                lengths.put(x, y, Math.sqrt(Gx * Gx + Gy * Gy));
                double tan = Math.atan2(Gy, Gx);
                if ((Gx > 0 && Gy < 0 && tan < -2.414) || (Gx < 0 && Gy < 0 && tan > 2.414)) {
                    angles.put(x, y, 0);
                } else if (Gx > 0 && Gy < 0 && tan < -0.414) {
                    angles.put(x, y, 1);
                } else if ((Gx > 0 && Gy < 0 && tan > -0.414) || (Gx > 0 && Gy > 0 && tan < 0.414)) {
                    angles.put(x, y, 2);
                } else if (Gx > 0 && Gy > 0 && tan < 2.414) {
                    angles.put(x, y, 3);
                } else if ((Gx > 0 && Gy > 0 && tan > 2.414) || (Gx < 0 && Gy > 0 && tan < -2.414)) {
                    angles.put(x, y, 4);
                } else if (Gx < 0 && Gy > 0 && tan < -0.414) {
                    angles.put(x, y, 5);
                } else if ((Gx < 0 && Gy > 0 && tan > -0.414) || (Gx < 0 && Gy < 0 && tan < 0.414)) {
                    angles.put(x, y, 6);
                } else if (Gx < 0 && Gy < 0 && tan < 2.414) {
                    angles.put(x, y, 7);
                }
            }
        }

        Mat filt = new Mat(blur.size(), CvType.CV_8UC1);

        for (int x = 1; x < blur.rows() - 1; x++) {
            for (int y = 1; y < blur.cols() - 1; y++) {
                int ix = 0;
                int iy = 0;
                if (angles.get(x,y)[0] == 0){
                iy = -1;}
                if (angles.get(x,y)[0] == 1){
                iy = -1;
                ix = 1;}
                if (angles.get(x,y)[0] == 2){
                ix = 1;}
                if (angles.get(x,y)[0] == 3){
                iy = 1;
                ix = 1;}
                if (angles.get(x,y)[0] == 4){
                iy = 1;}
                if (angles.get(x,y)[0] == 5){
                iy = 1;
                ix = -1;}
                if (angles.get(x,y)[0] == 6){
                ix = -1;}
                if (angles.get(x,y)[0] == 7){
                iy = -1;
                ix = -1;}

                if (lengths.get(x, y)[0] > lengths.get(x + ix, y + iy)[0] &&
                        lengths.get(x, y)[0] > lengths.get(x - ix, y - iy)[0]) {
                    filt.put(x, y, new byte[]{(byte)255});
                } else {
                    filt.put(x, y, new byte[]{(byte)0});
                }
            }
        }
        double maxVal=lengths.get(0,0)[0];
        HighGui.imshow("Image", blur);
        double lowThreshold = maxVal / low;
        double highThreshold = maxVal / high;
        System.out.println(maxVal);
        System.out.println(lowThreshold);
        System.out.println(highThreshold);
        for (int x = 1; x < blur.rows() - 1; x++) {
            for (int y = 1; y < blur.cols() - 1; y++) {
                if (filt.get(x,y)[0] == 255) {
                    if (lengths.get(x,y)[0] < lowThreshold) {
                        filt.put(x,y,0);
                    }
                }
            }
        }

        for (int x = 1; x < blur.rows() - 1; x++) {
            for (int y = 1; y < blur.cols() - 1; y++) {
                if (filt.get(x,y)[0] == 255) {
                    if (lengths.get(x,y)[0] <= highThreshold) {
                        boolean connectedToEdge =
                                filt.get(x-1,y-1)[0] == 255 ||
                                        filt.get(x-1,y)[0] == 255 ||
                                        filt.get(x-1,y+1)[0] == 255 ||
                                        filt.get(x,y+1)[0] == 255 ||
                                        filt.get(x+1,y+1)[0] == 255 ||
                                        filt.get(x+1,y)[0] == 255 ||
                                        filt.get(x+1,y-1)[0] == 255 ||
                                        filt.get(x,y-1)[0] == 255;

                        if (connectedToEdge) {
                            filt.put(x,y,255);
                        } else {
                            filt.put(x,y,0);
                        }
                    }
                }
            }
        }
        HighGui.imshow("filtered",filt);
        HighGui.waitKey(0);
        return filt;
    }

    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        String inputImagePath = "image.jpg";
        Mat filtered=grayscale(inputImagePath,3,1,1.5,1.01);
        HighGui.imshow("filtered",filtered);
    }
}
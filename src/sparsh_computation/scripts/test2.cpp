#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"
#include <iostream>


using namespace std;
using namespace cv;

cv::Mat img, erosion_dst, dilation_dst;

int main(int argc, char const *argv[])
{


    img = cv::imread("picture.png",cv::IMREAD_GRAYSCALE );
    if( img.empty() )
    {
        cout << "Could not open or find the image!\n" << endl;
        return -1;
    }

    cv::erode(img, erosion_dst, cv::Mat(), cv::Point(-1, -1),2, 1, 1);
    cv::dilate(img, dilation_dst, cv::Mat(), cv::Point(-1, -1),2, 1, 1);


    cv::imwrite("img_eroded.png", erosion_dst);
    cv::imwrite("img_dilated.png", dilation_dst);
    return 0;
}

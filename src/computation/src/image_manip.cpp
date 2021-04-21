#include <bits/stdc++.h>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"

class image_manip: public rclcpp::Node
{
    private: 

        // ROS Definitions 
        /* *
         * 
         * smart shared pointer is used to publish data to a certain topic
         * */

    //    rclcpp::Publisher<T>::SharedPtr publisher_;
        // OPENCV Definitions

        /* 
         * Erosion and dilation image definition with original image as well
         */
        cv::Mat image, erosion_dst, dilation_dst;
        /* *
         * erosion size and dilation size are standard kernel size
         * increase them to increase the filter kernel which is being 
         * convoluted for erosion and dilation 
         * */
        
        const uint_fast16_t erosion_elem;
        const uint_fast16_t erosion_size;
        const uint_fast16_t dilation_elem;
        const uint_fast16_t dilation_size;
        const uint_fast16_t count_;

    public: 

        /* *
         * Constructor definition with Node description
         * */
        inline image_manip():
            erosion_elem(3), 
            erosion_size(10), 
            dilation_elem(3),
            dilation_size(10), 
            Node("Image Manipulation Node"), 
            count_(0){};
        
        ~image_manip();

        /* *
         * Basic Erosion with Rectangular Kernel and basic structuring element 
         * 
         * 2 * n + 1 Size and Point setup
         * */
        inline void Erosion(){

            const int erosion_type = cv::MORPH_RECT;

            cv::Mat element = cv::getStructuringElement( erosion_type, cv::Size( 2*erosion_size + 1, 2*erosion_size+1 ), cv::Point( erosion_size, erosion_size ) );

            erode( image, erosion_dst, element );

        };

        /* *
         * Basic Dilation with Rectangular Kernel and basic structuring element 
         * 
         * 2 * n + 1 Size and Point setup
         * 
         * Feeding erosion output image to the structuring element for Dilation
         * */
        inline void Dilation(){
            int dilation_type = cv::MORPH_RECT;

            cv::Mat element = cv::getStructuringElement( dilation_type, cv::Size( 2*dilation_size + 1, 2*dilation_size+1 ), cv::Point( dilation_size, dilation_size ) );
        
            dilate(erosion_dst, dilation_dst, element );
        };
        

};

int main(int argc, char* argv[]){

    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<image_manip>());
    rclcpp::shutdown();
    return 0;
}